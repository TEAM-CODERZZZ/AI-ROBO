import asyncio
import importlib
from pyrogram import idle
from EQUROBOT import app
from EQUROBOT.modules import ALL_MODULES
import config
from config import LOGGER_ID

LOGGER_ID = config.LOGGER_ID

loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("EQUROBOT.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await app.send_message(LOGGER_ID, "**𝗜'𝗺 𝗔𝗹𝗶𝘃𝗲 𝗕𝗮𝗯𝘆 , 𝗬𝗼𝘂𝗿 𝗕𝗼𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗗𝗲𝗽𝗹𝗼𝘆𝗲𝗱\n 𝗠𝘆 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿  [ᴵ'ᵐ𝗖𝗢𝗗𝗘𝗥⋆─፝─™](https://t.me/Noob_Coderzzz)**")
    await idle()
    print("𝖻𝖺𝗁𝖺𝗇𝖼𝗁𝗈𝖽 𝖯𝗂𝗋𝗈 𝖢𝗈𝖽𝖾𝗋 𝗄𝗋𝗅𝗈 𝖾𝖽𝗂𝗍 𝖺𝖺 𝗀𝗒𝖺 𝗇 𝖾𝗋𝗋𝗈𝗋 𝖺𝖺𝖻 𝗃𝖺𝗄𝖾 𝗀𝖺𝗇𝖽 𝗆𝖺𝗋𝗐𝖺𝗈 𝗂𝗌𝗌𝖾 @iam_daxx")
  
  
if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())
    
