# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25545302"))
API_HASH = getenv("API_HASH", "6d8a23b3f0fda43411b3f12305f56d8f")
BOT_TOKEN = getenv("BOT_TOKEN", "7464232630:AAFKubeR667vBY_4HFQNs0oT6wBfEd87lOQ")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6232350467").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "-1002179112500")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002179112500"))
