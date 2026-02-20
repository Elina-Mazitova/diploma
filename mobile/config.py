from dotenv import load_dotenv
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_config():
    load_dotenv(os.path.join(PROJECT_ROOT, ".env"))
    load_dotenv(os.path.join(PROJECT_ROOT, ".env.credentials"))

    context = os.getenv("context", "local_emulator")

    env_file = os.path.join(PROJECT_ROOT, f".env.{context}")
    load_dotenv(env_file)

    print("\n=== CONFIG DEBUG ===")
    print(f"Loaded context: {context}")
    print(f"Loaded env file: {env_file}")
    print(f"UDID = {os.getenv('UDID')}")
    print(f"DeviceName = {os.getenv('DEVICE_NAME')}")
    print(f"Platform = {os.getenv('PLATFORM_NAME')}")
    print(f"BSTACK_USER = {os.getenv('BSTACK_USER')}")
    print(f"BSTACK_KEY = {os.getenv('BSTACK_KEY')}")
    print(f"BSTACK_APP = {os.getenv('BSTACK_APP')}")
    print("====================\n")

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
