use std::sync::Arc;

use spicycrab_generated_ms::GeneratedMarker;
use tunnelbana_core::attributes::AttributeMapper;
use tunnelbana_core::plugin::NullHttpClient;
use tunnelbana_core::{
    BuildContext, Context, HttpRequestData, InternalData, MicroService, Registry, Result, State,
};

fn build_generated_marker(bx: &BuildContext) -> Result<Box<dyn MicroService>> {
    Ok(Box::new(GeneratedMarker::new(
        bx.name.clone(),
        "spicycrab-generated".to_string(),
    )))
}

fn build_context() -> BuildContext {
    BuildContext {
        name: "generated_marker_instance".to_string(),
        base_url: "https://proxy.example".to_string(),
        config: serde_json::json!({}),
        attribute_mapper: Arc::new(AttributeMapper::default()),
        http_client: Arc::new(NullHttpClient),
        secret: "test-secret".to_string(),
        previous_secrets: Vec::new(),
    }
}

fn request_context() -> Context {
    Context::new(HttpRequestData::default(), State::new())
}

#[tokio::test]
async fn generated_microservice_builds_and_runs_through_registry() {
    let mut registry = Registry::new();
    registry.register_microservice("generated_marker", build_generated_marker);

    let bx = build_context();
    let service = registry
        .build_microservice("generated_marker", &bx)
        .expect("generated service should build");

    assert_eq!(service.name(), "generated_marker_instance");

    let mut ctx = request_context();
    let data = InternalData::request("https://sp.example/metadata");
    let data = service
        .process_request(&mut ctx, data)
        .await
        .expect("request path should pass");

    assert_eq!(
        ctx.state
            .get_str("generated_marker_instance", "request_seen")
            .as_deref(),
        Some("yes")
    );

    let data = service
        .process_response(&mut ctx, data)
        .await
        .expect("response path should pass");

    assert_eq!(
        data.attr_first("generated-marker"),
        Some("spicycrab-generated")
    );
}
