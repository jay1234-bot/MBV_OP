import platform

from pyrogram import Client
from pyrogram import __version__ as py_version
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message
from SukhPB.start import start_cmd

from BADMUNDA.Config import *

from ..core.clients import *

# Default START_PIC if not set
if not START_PIC:
    START_PIC = "https://envs.sh/fS5.jpg"


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Badmunda: Client, message: Message):
    global START_MESSAGE
    my_detail = await Badmunda.get_me()
    my_mention = my_detail.mention

    # Default START_MESSAGE if not set
    if not START_MESSAGE:
        START_MESSAGE = (
            f"ʜᴇʏ💫 {message.from_user.mention}🌸\n"
            f"✥ ɪ ᴀᴍ {my_mention}\n\n"
            "❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n"
            f"✥ **__ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ__** = {py_version}\n"
            f"✥ **__ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ__** = {platform.python_version()}\n"
            f"✥ **__ʙᴏᴛsᴘᴀᴍ ᴠᴇʀsɪᴏɴ__** = {version}\n"
            "❖━━━━•❅•°•❈•°•❅•━━━━❖"
        )

    # Getting start buttons
    start_buttons = await start_cmd(Badmunda)

    # Loop through Clients 1 to 25
    for i in range(1, 26):
        client_name = f"Client{i}"
        if client_name in globals():
            lol = globals()[client_name]
            if lol is not None:
                if START_PIC.lower().endswith((".jpg", ".png")):
                    await lol.send_photo(
                        message.chat.id,
                        START_PIC,
                        caption=START_MESSAGE,
                        reply_markup=InlineKeyboardMarkup(start_buttons),
                    )
                elif START_PIC.lower().endswith(".mp4"):
                    await lol.send_video(
                        message.chat.id,
                        START_PIC,
                        caption=START_MESSAGE,
                        reply_markup=InlineKeyboardMarkup(start_buttons),
                    )
                else:
                    await lol.send_message(
                        message.chat.id,
                        START_MESSAGE,
                        reply_markup=InlineKeyboardMarkup(start_buttons),
                    )
