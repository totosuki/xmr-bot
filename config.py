from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
ADDRESS = os.getenv("ADDRESS")
LANG = os.getenv("LANG") # JP or EN

GREEN = 0x00FF00