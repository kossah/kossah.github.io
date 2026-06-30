from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def home(request: Request):
    user_id = request.query_params.get("id")

    if user_id:
        return {
            "status": "ok",
            "user_id": user_id,
            "message": "ID получен"
        }

    return {
        "status": "ok",
        "message": "ID не найден"
    }
