from fastapi import Response, UploadFile, APIRouter,status
import shutil



from app.tasks.tasks import photo_processing

router = APIRouter(
    prefix='/images',
    tags=['images']
)


@router.post('/hotels', status_code=status.HTTP_201_CREATED)
async def download_hotels_images(file: UploadFile, file_id: int, ):
    """."""
    image_path = f'app/static/images/{file_id}.webp'
    with open(image_path, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)
    photo_processing.delay(image_path)
    return 'Файл успешно загружен.'


