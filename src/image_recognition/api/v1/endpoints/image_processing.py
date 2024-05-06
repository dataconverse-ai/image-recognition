from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import cv2
import numpy as np

router = APIRouter()

@router.post("/upload-image/", status_code=201)
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File uploaded is not an image.")
    
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Placeholder for image processing logic
    processed_image = img  # This would be your processed image

    # Respond with a confirmation or further data
    return JSONResponse(content={"message": "Image processed and de-identified successfully"})

@router.get("/test/", status_code=200)
def test_api():
    return {"message": "Test API endpoint is working"}
