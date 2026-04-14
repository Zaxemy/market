from fastapi import FastAPI
import uvicorn
from app.api.v1.api import api_router
from app.core.config import settings


app = FastAPI()


app.include_router(api_router, prefix=settings.api.api_prefix)


@app.get("/")
async def hello():
    return {"status": 200}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
