import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8259560745:AAFGaf_is9QeQ4mucLodsw6L6f6M7x5UkCU")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23643076"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "25bf494f099ade9f98697850843d8d0d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8487565900"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://usernotfound7603:3yWa4gxUVKxrIkkp@cluster0.jdgnbaz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
