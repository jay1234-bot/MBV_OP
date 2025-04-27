from os import getenv

import heroku3
from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *


@Client.on_message(filters.command(["addsudo"], prefixes=HANDLER))
async def _sudo(Badmunda: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default="")

        ok = await message.reply_text("✦ ᴀᴅᴅɪɴɢ ᴜꜱᴇʀ ᴀꜱ ꜱᴜᴅᴏ...")

        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("✦ `[HEROKU] ➥`\n✦ Please Setup Your **HEROKU_APP_NAME**")
            return

        heroku_var = app.config()

        # Check if user replied to a message
        if not message.reply_to_message:
            await ok.edit("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")
            return

        target = message.reply_to_message.from_user.id

        if str(target) in sudousers.split():
            await ok.edit("✦ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
        else:
            newsudo = f"{sudousers} {target}".strip()
            await ok.edit(f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ** ➥ `{target}`")
            heroku_var["SUDO_USERS"] = newsudo

    else:
        await message.reply_text("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
