import asyncio
from random import choice

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from SukhPB.raid import RAID, RRAID

from BADMUNDA.Config import *

from .. import sudos
from ..core.clients import *


# Active clients list get karo
def get_active_clients():
    clients = []
    for i in range(1, 26):
        c = globals().get(f"Client{i}")
        if c is not None:
            clients.append((i, c))
    return clients


@Client.on_message(filters.user(sudos) & filters.command(["raid"], prefixes=HANDLER))
async def raid(Badmunda: Client, e: Message):
    usage = (
        f"Command :- {HANDLER}raid (count) (reply to anyone)\n"
        f"Usage :- `{HANDLER}raid 400 <reply to anyone>`\n\n"
        f"Command :- {HANDLER}raid <count> <username>\n"
        f"Usage :- `{HANDLER}raid 400 @username`"
    )
    lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    chat = e.chat
    try:
        counts = int(lol[0])
    except (ValueError, IndexError):
        return await e.reply_text(usage)

    if counts <= 0:
        return await e.reply_text(f"Valid count do bhai! Use `{HANDLER}uraid` for unlimited.")

    # User resolve karo
    if len(lol) == 2:
        try:
            user = await Badmunda.get_users(lol[1])
        except Exception:
            return await e.reply_text("**Error:** User nahi mila!")
    elif e.reply_to_message and e.reply_to_message.from_user:
        try:
            user = await Badmunda.get_users(e.reply_to_message.from_user.id)
        except Exception:
            user = e.reply_to_message.from_user
    else:
        return await e.reply_text(usage)

    mention = user.mention
    active_clients = get_active_clients()

    if not active_clients:
        return await e.reply_text("Koi active bot nahi mila!")

    status_msg = await e.reply_text(f"🔥 Raid shuru! Total: `{counts}` msgs bhejenge...")

    sent = 0
    # Har client se ek ek msg bhejo, aur count track karo
    # Ek iteration = sabhi clients se ek msg = len(active_clients) msgs
    # Lekin hum counts msgs TOTAL bhejenge
    client_index = 0
    while sent < counts:
        idx, client = active_clients[client_index % len(active_clients)]
        raid_msg = choice(RAID)
        try:
            await client.send_message(chat.id, f"{mention} {raid_msg}")
            sent += 1
        except FloodWait as fw:
            await asyncio.sleep(fw.value + 1)
            continue  # Count skip mat karo, wahi msg dobara bhejo
        except Exception as ex:
            print(f"Client{idx} error: {ex}")
            sent += 1  # Error pe agle pe jao

        client_index += 1
        # Har client ke baad thoda wait - event loop block na ho
        await asyncio.sleep(0.05)

        # Progress update har 100 msgs pe
        if sent % 100 == 0 and sent > 0:
            try:
                await status_msg.edit(f"🔥 Raid chal raha hai... `{sent}/{counts}` msgs bheje")
            except Exception:
                pass

    try:
        await status_msg.edit(f"✅ Raid complete! `{sent}` msgs bheje {mention} ko!")
    except Exception:
        pass

    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Raid Done By: {e.from_user.id}\nOn: {mention}\nChat: {e.chat.id}\nCount: {sent}",
            )
        except Exception as a:
            print(a)


USERS = []


@Client.on_message(
    filters.user(sudos) & filters.command(["rraid", "replyraid"], prefixes=HANDLER)
)
async def rraid(Badmunda: Client, e: Message):
    global USERS
    try:
        lol = e.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        lol = None
    if e.reply_to_message and e.reply_to_message.from_user:
        # from_user works for both real users AND bots
        user = e.reply_to_message.from_user
    elif lol:
        user_ = lol[0]
        if user_.isnumeric():
            user_ = int(user_)
        if not user_:
            return await e.reply_text(
                "кιѕ внσѕ∂ιωαℓє кσ ρєℓηα нαι ηααм тσн вαтασ υѕкα !"
            )
        try:
            user = await Badmunda.get_users(user_)
        except (TypeError, ValueError):
            return await e.reply_text(
                "ᴜꜱᴇʀɴᴀᴍᴇ ʏᴀᴀ ɪᴅ ɢᴀʟᴀᴛ ʜᴀɪ ᴅᴜʙᴀʀᴀ ᴋᴏꜱʜɪꜱʜ ᴋᴀʀᴏ"
            )
    else:
        return await e.reply_text(
            "кιѕ внσѕ∂ιωαℓє кσ ρєℓηα нαι ηααм тσн вαтασ υѕкα ...!"
        )
    if int(user.id) in USERS:
        return await e.reply_text("ʏᴇ ᴘᴇʜʟᴇ ꜱᴇ ʟɪꜱᴛ ᴍᴇ ʜᴀɪ")
    USERS.append(user.id)
    mention = user.mention
    await e.reply_text(f"ɪꜱᴋᴏ ᴘᴇʟɴᴇ ᴋᴀ ᴋᴀᴀᴍ ꜱʜᴜʀᴜ ʜᴏ ɢᴀʏᴀ {mention}")
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Reply Raid Activated By: {e.from_user.id}\nOn: {mention}\nChat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["draid", "dreplyraid"], prefixes=HANDLER)
)
async def draid(Badmunda: Client, e: Message):
    global USERS
    try:
        lol = e.text.split(" ", 1)[1].split(" ", 1)
    except IndexError:
        lol = None
    if e.reply_to_message and e.reply_to_message.from_user:
        user = e.reply_to_message.from_user
    elif lol:
        user_ = lol[0]
        if user_.isnumeric():
            user_ = int(user_)
        if not user_:
            return await e.reply_text("User specify karo!")
        try:
            user = await Badmunda.get_users(user_)
        except (TypeError, ValueError):
            return await e.reply_text("Invalid user ID/username!")
    else:
        return await e.reply_text("User specify karo!")

    if int(user.id) not in USERS:
        return await e.reply_text("User raid list mein nahi hai!")
    USERS.remove(user.id)
    mention = user.mention
    await e.reply_text(f"Reply Raid Deactivated On {mention}")
    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Reply Raid Deactivated By: {e.from_user.id}\nUser: {mention}\nChat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["rlist", "raidlist"], prefixes=HANDLER)
)
async def rlist(Badmunda: Client, e: Message):
    global USERS
    _reply = "**Raid users list** \n\n"
    if len(USERS) > 0:
        for x in USERS:
            try:
                user = await Badmunda.get_users(x)
                _reply += f" ✨ {user.mention} \n"
            except Exception:
                _reply += f" ✨ [{x}](tg://user?id={x}) \n"
    else:
        await e.reply_text("Abhi koi nahi list mein!")
        return
    await e.reply_text(_reply)


@Client.on_message(filters.all)
async def checkraid(Badmunda: Client, msg: Message):
    global USERS
    # from_user None hota hai channel posts / anonymous messages mein
    # Bots ke liye from_user exist karta hai, toh bots pe bhi kaam karega
    if not msg.from_user:
        return
    if int(msg.from_user.id) in USERS:
        try:
            await msg.reply_text(choice(RRAID))
        except Exception as ex:
            print(f"checkraid reply error: {ex}")
