import shutil
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app2 import *
import uvicorn
from pathlib import Path
from fastapi.staticfiles import StaticFiles

# python -m uvicorn uploadfile:app

app = FastAPI()

templates = Jinja2Templates(directory="htmldirectory")


@app.get("/", response_class=HTMLResponse)
async def write_home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open('sound.wav', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"Added", add()}