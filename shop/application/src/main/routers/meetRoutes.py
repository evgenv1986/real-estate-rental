from fastapi import APIRouter
import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))))
sys.path.append(project_root)
from shop.rest.src.main.meet.MakeMeetEndPoint import MakeMeetEndPoint

router = APIRouter(
    prefix="/api/meets/v1",
    tags=["Meets"]
)

@router.get("/")
async def api_meets_v1():
    MakeMeetEndPoint().execute()
    return {"message": "Meets endpoint324234324"}