# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "26697299"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "7326c7f4d7d714d782a130c77b09009c")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8097210742:AAGqs1Jnov8GXVTPFBQM5KWcVPlFI7p0MiE")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Anonymoussuper_Bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "5168669934"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7674725731").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002471569312"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srvter")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002301898161"))

