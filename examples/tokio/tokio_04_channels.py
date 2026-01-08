"""Example 04: Communication between tasks using mpsc channels."""

from spicycrab_tokio import spawn, mpsc_channel, sleep, Duration, MpscSender, MpscReceiver
from spicycrab.types import Result


async def producer(tx: MpscSender, id: int) -> None:
    """Send messages through the channel."""
    for i in range(3):
        msg: str = f"Message {i} from producer {id}"
        print(f"Sending: {msg}")
        await tx.send(msg)
        await sleep(Duration.from_millis(50))


async def main() -> None:
    """Main function demonstrating mpsc channel communication."""
    # Create a bounded channel with capacity 10
    # Tuple unpacking: (tx, rx) = channel()
    tx, rx = mpsc_channel(10)

    # Clone tx for second producer
    tx2: MpscSender = tx.clone()

    # Spawn producer tasks
    handle1 = spawn(producer(tx, 1))
    handle2 = spawn(producer(tx2, 2))

    # Receive messages
    count: int = 0
    while count < 6:
        msg = await rx.recv()
        if msg is not None:
            print(f"Received: {msg}")
            count = count + 1

    # Wait for producers to finish
    Result.unwrap(await handle1)
    Result.unwrap(await handle2)

    print("All messages received!")
