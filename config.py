from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
ADDRESS = os.getenv("ADDRESS")
XMRLANG = os.getenv("XMRLANG") # JP or EN

GREEN = 0x00FF00