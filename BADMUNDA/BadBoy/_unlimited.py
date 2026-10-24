import asyncio
from random import choice

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from SukhPB.raid import RAID as galia
from SukhPB.get_user import user_only
from SukhPB.raid import RAID

from BADMUNDA.Config import *

from .. import sudos
from ..core.clients import *

# Global flag - /stop se False hoga
unlimited = False


def get_active_clients():
    """Sabhi active (non-None) clients return karo"""
    clients = []
    for i in range(1, 26):
        c = globals().get(f"Client{i}")
        if c is not None:
            clients.append((i, c))
    return clients


async def send_to_all(chat_id: int, text: str):
    """Sare active clients se message bhejo"""
    active = get_active_clients()
    for idx, client in active:
        try:
            await client.send_message(chat_id, text)
        except FloodWait as fw:
            await asyncio.sleep(fw.value + 1)
            try:
                await client.send_message(chat_id, text)
            except Exception as ex:
                print(f"Client{idx} retry failed: {ex}")
        except Exception as ex:
            print(f"Client{idx} error: {ex}")


@Client.on_message(filters.user(sudos) & filters.command(["stop"], prefixes=HANDLER))
async def stop(_, e: Message):
    global unlimited
    unlimited = False
    await e.reply_text("⛔ Stopped! Spam/Raid/Abuse band ho gaya.")


@Client.on_message(filters.user(sudos) & filters.command(["uspam"], prefixes=HANDLER))
async def uspam(Badmunda: Client, e: Message):
    global unlimited
    msg = str(e.text[6:]).strip()
    if not msg:
        await e.reply("Spam message bhi do bhai! Usage: `/uspam <message>`")
        return

    unlimited = True
    await e.reply_text(f"🔥 Unlimited Spam shuru! `/stop` se band karo.")

    target_mention = None
    if e.reply_to_message and e.reply_to_message.from_user:
        target_mention = e.reply_to_message.from_user.mention

    while unlimited:
        if target_mention:
            text = f"{target_mention} {msg}"
        else:
            text = msg

        await send_to_all(e.chat.id, text)
        # ZARURI: Ye sleep event loop ko dusre commands process karne deta hai
        await asyncio.sleep(0.3)

    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Unlimited Spam By: {e.from_user.id}\nChat: {e.chat.id}\nMsg: {msg}",
            )
        except Exception as a:
            print(a)


@Client.on_message(filters.user(sudos) & filters.command(["uraid"], prefixes=HANDLER))
async def uraid(Badmunda: Client, e: Message):
    global unlimited

    # User resolve karo
    if e.reply_to_message and e.reply_to_message.from_user:
        user = e.reply_to_message.from_user
        mention = user.mention
    else:
        try:
            user = await user_only(Badmunda, e)
            mention = user.mention
        except Exception:
            return await e.reply_text("User reply karo ya username/id do!")

    unlimited = True
    await e.reply_text(f"🔥 Unlimited Raid shuru on {mention}! `/stop` se band karo.")

    while unlimited:
        reply = choice(RAID)
        raid_msg = f"{mention} {reply}"
        await send_to_all(e.chat.id, raid_msg)
        # ZARURI: Event loop ko breathe karne do - /stop kaam kar sake
        await asyncio.sleep(0.3)

    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Unlimited Raid By: {e.from_user.id}\nOn: {mention}\nChat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["abuse", "gali"], prefixes=HANDLER)
)
async def abuse(Badmunda: Client, e: Message):
    global unlimited

    target_mention = None
    if e.reply_to_message and e.reply_to_message.from_user:
        target_mention = e.reply_to_message.from_user.mention

    unlimited = True
    await e.reply_text(f"🔥 Unlimited Abuse shuru! `/stop` se band karo.")

    while unlimited:
        msg = choice(galia)
        if target_mention:
            text = f"{target_mention} {msg}"
        else:
            text = msg
        await send_to_all(e.chat.id, text)
        await asyncio.sleep(0.3)

    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Unlimited Abuse By: {e.from_user.id}\nChat: {e.chat.id}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["echo", "repeat"], prefixes=HANDLER)
)
async def echo_(Badmunda: Client, message: Message):
    txt = " ".join(message.command[1:])
    if message.reply_to_message:
        msg = message.reply_to_message.text.markdown
    elif txt:
        msg = str(txt)
    else:
        await message.reply_text(
            f"**Wrong Usage!**\n\nSyntax: {HANDLER}echo (message or reply to message)"
        )
        return

    try:
        await message.delete()
        await Badmunda.send_message(message.chat.id, msg)
    except Exception as a:
        await Badmunda.send_message(message.chat.id, msg)
        print(str(a))
