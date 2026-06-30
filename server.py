from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


# разрешаем GitHub Pages обращаться к Render
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def home(id: str = None):

    if id is None:
        return {
            "status": "ok",
            "message": "Server works"
        }

    return {
        "status": "ok",
        "user_id": id,
        "message": "ID получен"
    }



@app.post("/photo")
async def photo(
    id: str = Form(...),
    photo: UploadFile = File(...)
):

    data = await photo.read()


    filename = f"{id}.jpg"


    with open(filename, "wb") as f:
        f.write(data)


    return {
        "status": "photo saved",
        "id": id,
        "file": filename
    }
