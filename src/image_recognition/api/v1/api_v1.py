from fastapi import APIRouter
from .endpoints.image_processing import router as image_router

router = APIRouter()
router.include_router(image_router, prefix="/images", tags=["Image Processing"])
