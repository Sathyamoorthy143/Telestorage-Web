use actix_web::{web, HttpResponse, Responder};

pub async fn get_stream_token() -> impl Responder {
    HttpResponse::Ok().json("mock-token")
}
