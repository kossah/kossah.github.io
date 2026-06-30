from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI()


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

    with open(f"{id}.jpg", "wb") as f:
        f.write(data)

    return {
        "status": "photo saved",
        "id": id
    }
