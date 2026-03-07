from fastapi import APIRouter
from app.schemas.route_schema import RouteRequest, RouteResponse
from app.services.routing_service import calculate_route

router = APIRouter()

@router.post("/route")
def get_route(data: RouteRequest):
    return calculate_route(data)