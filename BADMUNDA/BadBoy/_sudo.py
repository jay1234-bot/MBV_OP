import os
from os import getenv

from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUNDA.Config import *
from .. import sudos

try:
    import heroku3
    HEROKU_AVAILABLE = True
except ImportError:
    HEROKU_AVAILABLE = False


@Client.on_message(filters.user(sudos) & filters.command(["addsudo"], prefixes=HANDLER))
async def _sudo(Badmunda: Client, message: Message):
    # Sirf OWNER hi addsudo kar sakta hai
    if message.from_user.id != int(OWNER_ID):
        await message.reply_text("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
        return

    if not message.reply_to_message:
        await message.reply_text("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")
        return

    target = message.reply_to_message.from_user.id

    # In-memory sudos list mein bhi add karo (runtime ke liye)
    if target not in sudos:
        sudos.append(target)

    ok = await message.reply_text(f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ** ➥ `{target}`\n✦ ʀᴜɴᴛɪᴍᴇ ᴍᴇɪɴ ᴀᴅᴅ ʜᴏ ɢᴀʏᴀ!")

    # Agar Heroku available hai aur configured hai toh permanent save karo
    if HEROKU_AVAILABLE and HEROKU_API_KEY and HEROKU_APP_NAME:
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            app = Heroku.app(HEROKU_APP_NAME)
            heroku_var = app.config()
            sudousers = getenv("SUDO_USERS", default="")
            if str(target) in sudousers.split():
                await ok.edit("✦ ᴛʜɪꜱ ᴜꜱᴇʀ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ !!")
                return
            newsudo = f"{sudousers} {target}".strip()
            heroku_var["SUDO_USERS"] = newsudo
            await ok.edit(f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ** ➥ `{target}`\n✦ Heroku mein bhi save ho gaya!")
        except Exception as ex:
            await ok.edit(f"✦ Runtime mein add hua lekin Heroku save fail: `{ex}`")
    else:
        # Heroku nahi hai toh sirf runtime mein kaam karega
        await ok.edit(
            f"✦ **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ** ➥ `{target}`\n"
            f"✦ Runtime mein add ho gaya! (Restart pe reset hoga)\n"
            f"✦ Permanent ke liye HEROKU_APP_NAME & HEROKU_API_KEY set karo."
        )


@Client.on_message(filters.user(sudos) & filters.command(["delsudo", "removesudo"], prefixes=HANDLER))
async def _delsudo(Badmunda: Client, message: Message):
    if message.from_user.id != int(OWNER_ID):
        await message.reply_text("✦ ꜱᴏʀʀʏ, ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ.")
        return

    if not message.reply_to_message:
        await message.reply_text("✦ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ.")
        return

    target = message.reply_to_message.from_user.id

    if target == int(OWNER_ID):
        await message.reply_text("✦ Owner ko remove nahi kar sakte!")
        return

    if target in sudos:
        sudos.remove(target)
        await message.reply_text(f"✦ `{target}` ꜱᴜᴅᴏ ʟɪꜱᴛ ꜱᴇ ʀᴇᴍᴏᴠᴇ ʜᴏ ɢᴀʏᴀ!")
    else:
        await message.reply_text("✦ ʏᴇ ᴜꜱᴇʀ ꜱᴜᴅᴏ ʟɪꜱᴛ ᴍᴇɪɴ ɴᴀʜɪ ʜᴀɪ!")


@Client.on_message(filters.user(sudos) & filters.command(["sudolist"], prefixes=HANDLER))
async def _sudolist(Badmunda: Client, message: Message):
    if not sudos:
        await message.reply_text("✦ ᴋᴏɪ ꜱᴜᴅᴏ ᴜꜱᴇʀ ɴᴀʜɪ ʜᴀɪ!")
        return
    text = "**✦ Sudo Users List:**\n\n"
    for uid in sudos:
        try:
            u = await Badmunda.get_users(uid)
            text += f"• {u.mention} (`{uid}`)\n"
        except:
            text += f"• [`{uid}`](tg://user?id={uid})\n"
    await message.reply_text(text)
