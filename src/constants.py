from dotenv import load_dotenv
import os

load_dotenv()
env = os.environ.get

token = env("TODOIST_TOKEN")
inbox_project_id = 2169583011

color_dict = {
    "purple": 42,
    "green": 34,
    "pink": 44,
    "brown": 49,
    "red": 31,
    "yellow": 33,
    "blue": 41,
}
