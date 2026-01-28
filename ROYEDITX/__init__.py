import asyncio
import logging
import time

from motor.motor_asyncio import AsyncIOMotorClient
from pyrogram import Client

import config

# -------------------- EVENT LOOP FIX (MOST IMPORTANT) --------------------
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())
# -------------------------------------------------------------------------

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

boot = time.time()

# -------------------- MONGO SAFE INIT --------------------
mongo = AsyncIOMotorClient(config.MONGO_URL)
db = mongo.Anonymous
# --------------------------------------------------------

OWNER = config.OWNER_ID


class LOCOPILOT(Client):
    def __init__(self):
        super().__init__(
            name="LOCOPILOT",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            plugins=dict(root="ROYEDITX.modules"),
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.id = me.id
        self.name = me.first_name
        self.username = me.username
        LOGGER.info("Bot started successfully")

    async def stop(self):
        await super().stop()
        LOGGER.info("Bot stopped")


app = LOCOPILOT()

# -------------------- MAIN RUN --------------------
if __name__ == "__main__":
    app.run()
