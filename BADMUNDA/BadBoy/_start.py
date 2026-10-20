
import platform

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
    START_PIC = (
        "https://i.pinimg.com/736x/e9/c7/f7/"
        "e9c7f78ec4180885cd0ce4bf95197c40.jpg"
    )


# Create buttons dynamically for each bot
def get_start_buttons(bot_username: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
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

    # Get the identity of the bot handling this command
    my_detail = await Badmunda.get_me()
    my_mention = my_detail.mention

    # Build buttons using this bot's own username
    if not my_detail.username:
        print("Cannot create group link: bot has no public username.")
        start_buttons = get_start_buttons("")
    else:
        start_buttons = get_start_buttons(my_detail.username)

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

    # Send the start message using configured clients
    for i in range(1, 26):
        client_name = f"Client{i}"
        client = globals().get(client_name)

        if client is None:
            continue

        try:
            if START_PIC.lower().endswith(
                (".jpg", ".jpeg", ".png")
            ):
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=start_buttons,
                )

            elif START_PIC.lower().endswith(".mp4"):
                await client.send_video(
                    chat_id=message.chat.id,
                    video=START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=start_buttons,
                )

            else:
                await client.send_message(
                    chat_id=message.chat.id,
                    text=START_MESSAGE,
                    reply_markup=start_buttons,
                )

        except Exception as e:
            print(
                f"Failed to send start message with "
                f"{client_name}: {e}"
            )
