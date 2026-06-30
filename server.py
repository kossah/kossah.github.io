from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



BOT_TOKEN = "8439897161:AAEkWaO7MZS-pSP1wbLnGN7kqKQ_UTa65Zc"



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



    # отправляем фото в Telegram

    url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    )


    files = {
        "photo": (
            filename,
            data,
            "image/jpeg"
        )
    }


    payload = {
        "chat_id": id,
        "caption": f"Фото от пользователя {id}"
    }


    requests.post(
        url,
        data=payload,
        files=files
    )



    return {
        "status": "photo sent",
        "id": id
    }
