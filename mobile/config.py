import os

from dotenv import load_dotenv

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_config():
    base_env = os.path.join(PROJECT_ROOT, ".env")
    if os.path.exists(base_env):
        load_dotenv(base_env)

    credentials_env = os.path.join(PROJECT_ROOT, ".env.credentials")
    if os.path.exists(credentials_env):
        load_dotenv(credentials_env)

    context = os.getenv("context", "local_emulator")

    context_env = os.path.join(PROJECT_ROOT, f".env.{context}")
    if os.path.exists(context_env):
        load_dotenv(context_env)

    return {
        "context": context,
        "appium_server_url": os.getenv("APPIUM_SERVER_URL"),
        "platformName": os.getenv("PLATFORM_NAME"),
        "platformVersion": os.getenv("PLATFORM_VERSION"),
        "deviceName": os.getenv("DEVICE_NAME"),
        "udid": os.getenv("UDID"),

        "appPackage": os.getenv("APP_PACKAGE"),
        "appActivity": os.getenv("APP_ACTIVITY"),

        "timeout": float(os.getenv("TIMEOUT", "10")),

        "bstack": {
            "user": os.getenv("BSTACK_USER"),
            "key": os.getenv("BSTACK_KEY"),
            "project": os.getenv("BSTACK_PROJECT"),
            "build": os.getenv("BSTACK_BUILD"),
            "session": os.getenv("BSTACK_SESSION"),
            "app": os.getenv("BSTACK_APP"),
        }
    }
