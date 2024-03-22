from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import BOT_USERNAME, OWNER_ID
from pyrogram.types import InlineKeyboardButton as ib
import asyncio
from EQUROBOT import app


START_TEXT = """
𝗛𝗶 ,

𝗜 𝗔𝗺 , 
𝗬𝗼𝘂𝗿 𝗔𝗜 𝗖𝗼𝗺𝗽𝗮𝗻𝗶𝗼𝗻. 
𝗟𝗲𝘁'𝘀 𝗖𝗵𝗮𝘁 𝗔𝗻𝗱 𝗘𝘅𝗽𝗹𝗼𝗿𝗲. 
𝗧𝗵𝗲 𝗗𝗲𝗽𝘁𝗵𝘀 𝗢𝗳 𝗖𝗼𝗻𝘃𝗲𝗿𝘀𝗮𝘁𝗶𝗼𝗻 𝗧𝗼𝗴𝗲𝘁𝗵𝗲𝗿!! 
𝗙𝗲𝗲𝗹 𝗙𝗿𝗲𝗲 𝗧𝗼 𝗔𝘀𝗸 𝗠𝗲 𝗔𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗢𝗿 𝗦𝗵𝗮𝗿𝗲 𝗬𝗼𝘂𝗿 𝗧𝗵𝗼𝘂𝗴𝗵𝘁𝘀. 
𝗜'𝗺 𝗛𝗲𝗿𝗲 𝗧𝗼 𝗟𝗶𝘀𝘁𝗲𝗻 𝗔𝗻𝗱 𝗘𝗻𝗴𝗮𝗴𝗲 𝗜𝗻 𝗠𝗲𝗮𝗻𝗶𝗻𝗴𝗳𝘂𝗹 𝗗𝗶𝘀𝗰𝘂𝘀𝘀𝗶𝗼𝗻 𝗪𝗶𝘁𝗵 𝗬𝗼𝘂."
"""



@app.on_message(filters.command("coder") & filters.private)
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton("⦿𝐀𝐝𝐝 𝐌𝐞 𝐁𝐚𝐛𝐲⦿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("⦿𝐆𝐫𝐨𝐮𝐩⦿", url=f"https://t.me/Coderzzz_Support"),
            InlineKeyboardButton("⦿𝐎𝐰𝐧𝐞𝐫⦿", user_id=OWNER_ID)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_video(
        video="https://telegra.ph/file/a03ce0f6022a3b4ee7d80.jpg",
        caption=START_TEXT,
        reply_markup=reply_markup
    )
