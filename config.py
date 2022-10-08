from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "15462970"))
API_HASH = getenv("API_HASH","818af3b1235f9d87c53fd54e540c886f")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("5791501037:AAEAe93nq-e5PZ-UJc_J6Who8GX84xMzdtg")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "150"))
LOGGER_ID = int(getenv("-1001466357800"))
MONGO_DB_URI = getenv("mongodb+srv://Ziddiboy1762:ziddiboy1762@cluster0.yhk3i4m.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5782714204").split()))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/c5952790fa8235f499749.jpg")
START_IMG = getenv("https://te.legra.ph/file/8183cb3c7ea513300e6d9.jpg")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Agricultura_Queen ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/Shivam_Agro ")

STRING_SESSION = getenv("STRING_SESSION", " BQAd9Xd3WDl87HNrUAk4G2nhP6ygg_aG4sFUYoENTmfXBgwHyMBw4H6n7TDCbyPUUW3mn_yOq_rmx46RzUVOmLt8LhoI2FduIBCyNTIy0b31_2Dbl-g-CbUp8mVoJ6So0cf2jhjIIP0a8geovsl5xJ4oxwyJaJy-ub_iG5eOtwsPgXx2EKr4QcujSHM2-MYeRlg8Btko5aujdUhhqW8Mh2E0m7dCBzt7CjcxYgaQfkv0NkXuYpz-0wtF2Uft8oQOTso8XUcl70p2HxDIjTj2ROzV0QtPealOyg4nX-Tx9tItavSSEy-VCpFDCU6S5OJlSxGqijfdxlK3bg-hoAVAJJguAAAAAThX180A")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1452219013").split()))
