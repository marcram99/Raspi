import json
import uvicorn
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

files_path = Path.home().joinpath('Marc-perso/code/python/Raspi/files')
data_file = files_path.joinpath('data.json')

test_lightcaptor = files_path.joinpath('light.json')
if not test_lightcaptor.exists():
    with open(test_lightcaptor, 'w') as new_file:
        json.dump({'light_mode': 'dark'}, new_file)

test_tempcaptor = files_path.joinpath('temp.json')
if not test_tempcaptor.exists():
    with open(test_tempcaptor, 'w') as new_file:
        json.dump({'temp': 0, 'hum': 0}, new_file)

with open(test_lightcaptor) as json_file:
    light_mode = json.load(json_file)["light_mode"]


class Read_value(BaseModel):
    light_value: str
    last_change: str
    warning_level: int


class Temp_value(BaseModel):
    temp: int
    hum: int


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def test_page(request: Request):
    with open(data_file) as json_file:
        data = json.load(json_file)
    return templates.TemplateResponse("test_page.html",
                                      {"request": request,
                                       "data": data,
                                       "light_mode": light_mode
                                       }
                                      )


@app.get("/API/light_mode")
async def light_mode_r():
    with open(test_lightcaptor) as json_file:
        light_value = json.load(json_file)["light_mode"]
    return {"light_value": light_value}


@app.post("/API/light_mode")
async def light_mode_w(values: Read_value):
    with open(test_lightcaptor, 'w') as json_file:
        data = {"light_mode": values.light_value}
        json.dump(data, json_file)
    return {"light_mode": values}


@app.get("/API/temp_mode")
async def temp_mode_r():
    with open(test_lightcaptor) as json_file:
        temp = json.load(json_file)["temp"]
        hum = json.load(json_file)["hum"]
    return {"temp": temp, "hum": hum}

@app.post("/API/temp_mode")
async def temp_mode_w(values: Temp_value):
    with open(test_lightcaptor, 'w') as json_file:
        data = {"temp": values.temp, "hum": values.hum}
        json.dump(data, json_file)
        print(f'DEBUG@temp_mode_w: {data}')
    return {"temp": values.temp, "hum": values.hum}


@app.post("/API/read_json")
async def read_json():
    with open(data_file) as json_file:
        data = json.load(json_file)
    return data


if __name__ == '__main__':
    uvicorn.run("light_simul:app")
