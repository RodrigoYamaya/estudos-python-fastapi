from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Ola mundo, Hello world'


app.include_router(router)    