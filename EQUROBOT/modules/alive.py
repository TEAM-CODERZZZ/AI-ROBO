from pyrogram import Client, filters
from EQUROBOT import app

# ---------------------------
@app.on_message(filters.command("alive", prefixes="."))
def alive(_, message):
    message.reply_text("**🥀 𝐈'𝐦 𝐀𝐥𝐢𝐯𝐞 𝐌𝐲 𝐃𝐞𝐚𝐫 𝐆𝐞𝐧𝐢𝐮𝐬 𝐌𝐚𝐬𝐭𝐞𝐫 💗 ...**")
