
import platform

from urllib.parse import quote
from pyrogram import Client, filters
from pyrogram import __version__ as py_version
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message,
)

from BADMUNDA.Config import *
from ..core.clients import *


# Default START_PIC if not set
if not START_PIC:
    START_PIC = "https://i.pinimg.com/736x/e9/c7/f7/e9c7f78ec4180885cd0ce4bf95197c40.jpg"


# Custom start buttons
START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "🌸 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🌸",
                url="https://t.me/censored_politics",
            ),
            InlineKeyboardButton(
                "💫 sᴜᴘᴘᴏʀᴛ 💫",
                url="https://t.me/censoredkrishan",
            ),
        ],
        [
            InlineKeyboardButton(
                "👻 ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 👻",
                url=f"https://t.me/{bot_username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                "📢 ᴄʜᴀɴɴᴇʟ 📢",
                url="https://t.me/censoredkrishan",
            ),
            InlineKeyboardButton(
                "📂 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 📂",
                url="https://t.me/censored_politics",
            ),
        ],
        [
            InlineKeyboardButton(
                "✨ ᴜᴘᴅᴀᴛᴇ ✨",
                url="https://t.me/censoredkrishan",
            ),
        ],
    ]
)


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Badmunda: Client, message: Message):
    global START_MESSAGE

    my_detail = await Badmunda.get_me()
    my_mention = my_detail.mention

    # Default welcome message
    if not START_MESSAGE:
        user_mention = (
            message.from_user.mention
            if message.from_user
            else "there"
        )

        START_MESSAGE = (
            f"ʜᴇʏ💫 {user_mention}🌸\n"
            f"✥ ɪ ᴀᴍ {my_mention}\n\n"
            "❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n"
            f"✥ **__ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ__** = {py_version}\n"
            f"✥ **__ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ__** = "
            f"{platform.python_version()}\n"
            f"✥ **__ʙᴏᴛsᴘᴀᴍ ᴠᴇʀsɪᴏɴ__** = {version}\n"
            "❖━━━━•❅•°•❈•°•❅•━━━━❖"
        )

    # Send start message using configured clients
    for i in range(1, 26):
        client_name = f"Client{i}"
        lol = globals().get(client_name)

        if lol is None:
            continue

        try:
            if START_PIC.lower().endswith((".jpg", ".jpeg", ".png")):
                await lol.send_photo(
                    chat_id=message.chat.id,
                    photo=START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=START_BUTTONS,
                )

            elif START_PIC.lower().endswith(".mp4"):
                await lol.send_video(
                    chat_id=message.chat.id,
                    video=START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=START_BUTTONS,
                )

            else:
                await lol.send_message(
                    chat_id=message.chat.id,
                    text=START_MESSAGE,
                    reply_markup=START_BUTTONS,
                )

        except Exception as e:
            print(
                f"Failed to send start message with "
                f"{client_name}: {e}"
            )
