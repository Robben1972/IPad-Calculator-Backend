from fastapi import APIRouter, File, UploadFile, Form
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
# from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(image: UploadFile = File(...)):
    i: int = 0
    while i < 3:
        responses = analyze_image(Image.open(image.file))
        data = []
        for response in responses:
            data.append(response)
        try:
            print('response in route: ', response)
            return {"message": "Image processed", "data": data, "status": "success"}
        except Exception as e:
            print(f"Error in processing image: {e}")
            i += 1
    return {"message": "Failed to process image", "status": "failure"}
