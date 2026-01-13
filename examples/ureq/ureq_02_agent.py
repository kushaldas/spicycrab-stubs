"""Using an agent example.

Demonstrates:
- Creating a ureq agent
"""

from spicycrab_ureq import agent


def main() -> None:
    """Create and use an agent."""
    ag = agent()
    print("Created HTTP agent")
