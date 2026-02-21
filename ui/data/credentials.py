import os

from dotenv import load_dotenv

load_dotenv()

TODOIST_LOGIN = os.getenv("TODOIST_LOGIN")
TODOIST_PASSWORD = os.getenv("TODOIST_PASSWORD")
