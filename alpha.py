import datetime
import os
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import dotenv

import Timetable

dotenv.load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

w = {}


@app.get('/', response_class=HTMLResponse)
async def get_timetable_img(request: Request, group: str = "ПИбд-21", version: int = 1398036):
    global w
    response_json = w.get((group, version), None)
    if response_json is None:
        print('GET DATA')
        response = requests.get(
            os.getenv('API_SERVER') + f"/api/diff/{group}/{version}",
            headers={
                "Authorization": os.getenv("ULSTU_API_KEY")
            }
        )
        response_json = response.json()
        w[(group, version)] = response_json

    weeks_json: dict[Any] = response_json['response']['WAS']['weeks']

    weeks_nums = list(weeks_json.keys())

    tt = Timetable.get_timetable_week_from_json(weeks_json.get(weeks_nums[0]))

    tt.number = int(weeks_nums[0]) + 1

    tt.group = group

    tb = Timetable.Bells()
    tb.bells = [
        Timetable.Bell(datetime.time(10, 30), datetime.time(11, 50)),
        Timetable.Bell(datetime.time(10, 30), datetime.time(11, 50)),
        Timetable.Bell(datetime.time(10, 30), datetime.time(11, 50)),
        Timetable.Bell(datetime.time(10, 30), datetime.time(11, 50)),
        Timetable.Bell(datetime.time(10, 30), datetime.time(11, 50)),
        Timetable.Bell(datetime.time(10, 30), datetime.time(11, 50)),
        Timetable.Bell(datetime.time(10, 30), datetime.time(11, 50)),
        Timetable.Bell(datetime.time(10, 30), datetime.time(11, 50)),
    ]

    tt.timetable_bells = tb

    # tt.set_period(datetime.date(2023, 7, 31), datetime.date(2023, 8, 6))

    tt.set_period()

    return templates.TemplateResponse("template.html", {"request": request, "tt": tt})
