import asyncio
import random

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import *
from SukhPB.porn import pornlinks
from SukhPB.raid import RAID

from BADMUNDA.Config import *

from .. import sudos
from ..core.clients import *


def get_active_clients():
    """Sabhi active (non-None) clients return karo"""
    clients = []
    for i in range(1, 26):
        c = globals().get(f"Client{i}")
        if c is not None:
            clients.append((i, c))
    return clients


@Client.on_message(
    filters.user(sudos) & filters.command(["spam", "bigspam"], prefixes=HANDLER)
)
async def spam(Badmunda: Client, e: Message):
    usage = (
        f"Command :- {HANDLER}spam (count) (text)\n"
        f"Example :- `{HANDLER}spam 100 SpamBot OP`\n\n"
        f"{HANDLER}bigspam (count) (text)\n"
        f"Example :- `{HANDLER}bigspam 500 Pb Spam Bot`"
    )
    try:
        lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
        counts = int(lol[0])
        spam_text = str(lol[1])
    except (IndexError, ValueError):
        return await e.reply_text(usage)

    if counts <= 0:
        return await e.reply_text("Valid count do!")

    chat = e.chat
    active_clients = get_active_clients()
    if not active_clients:
        return await e.reply_text("Koi active bot nahi mila!")

    target_mention = None
    if e.reply_to_message and e.reply_to_message.from_user:
        target_mention = e.reply_to_message.from_user.mention

    status_msg = await e.reply_text(f"🔥 Spam shuru! `{counts}` msgs bhejenge...")

    sent = 0
    client_index = 0
    while sent < counts:
        idx, client = active_clients[client_index % len(active_clients)]
        if target_mention:
            text = f"{target_mention} {spam_text}"
        else:
            text = spam_text
        try:
            await client.send_message(chat.id, text)
            sent += 1
        except FloodWait as fw:
            await asyncio.sleep(fw.value + 1)
            continue  # Count skip mat karo
        except Exception as ex:
            print(f"Client{idx} spam error: {ex}")
            sent += 1

        client_index += 1
        await asyncio.sleep(0.05)

        if sent % 100 == 0:
            try:
                await status_msg.edit(f"🔥 Spam chal raha... `{sent}/{counts}`")
            except Exception:
                pass

    try:
        await status_msg.edit(f"✅ Spam complete! `{sent}` msgs bheje!")
    except Exception:
        pass

    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Spam By: {e.from_user.id}\nChat: {e.chat.id}\nCount: {sent}\nMsg: {spam_text}",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["dspam", "delayspam"], prefixes=HANDLER)
)
async def delayspam(Badmunda: Client, e: Message):
    usage = (
        f"Command :- {HANDLER}dspam (count) (sleeptime) (text)\n"
        f"Example :- `{HANDLER}dspam 25 8 PbBot`"
    )
    try:
        parts = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        counts = int(parts[0])
        sleeptime = float(parts[1])
        spam_text = str(parts[2])
    except (IndexError, ValueError):
        return await e.reply_text(usage)

    chat = e.chat
    active_clients = get_active_clients()
    if not active_clients:
        return await e.reply_text("Koi active bot nahi mila!")

    target_mention = None
    if e.reply_to_message and e.reply_to_message.from_user:
        target_mention = e.reply_to_message.from_user.mention

    status_msg = await e.reply_text(f"🔥 Delay Spam shuru! `{counts}` rounds, `{sleeptime}s` delay each...")

    for round_num in range(counts):
        # Har round mein sabhi bots message bhejein
        for idx, client in active_clients:
            if target_mention:
                text = f"{target_mention} {spam_text}"
            else:
                text = spam_text
            try:
                await client.send_message(chat.id, text)
            except FloodWait as fw:
                await asyncio.sleep(fw.value + 1)
                try:
                    await client.send_message(chat.id, text)
                except Exception as ex:
                    print(f"Client{idx} retry failed: {ex}")
            except Exception as ex:
                print(f"Client{idx} dspam error: {ex}")

        await asyncio.sleep(sleeptime)

        if (round_num + 1) % 10 == 0:
            try:
                await status_msg.edit(f"🔥 Delay Spam: `{round_num+1}/{counts}` rounds done")
            except Exception:
                pass

    try:
        await status_msg.edit(f"✅ Delay Spam complete! `{counts}` rounds bheje!")
    except Exception:
        pass

    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Delay Spam By: {e.from_user.id}\nChat: {e.chat.id}\nCount: {counts}\nMsg: {spam_text}\nSleep: {sleeptime}s",
            )
        except Exception as a:
            print(a)


@Client.on_message(
    filters.user(sudos) & filters.command(["pspam", "pornspam"], prefixes=HANDLER)
)
async def _pornspam(Badmunda: Client, e: Message):
    usage = f"Command :- {HANDLER}pspam (count)\nExample :- `{HANDLER}pspam 23`"
    try:
        lol = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 1)
        counts = int(lol[0])
    except (IndexError, ValueError):
        return await e.reply_text(usage)

    chat = e.chat
    active_clients = get_active_clients()
    if not active_clients:
        return await e.reply_text("Koi active bot nahi mila!")

    target_mention = None
    if e.reply_to_message and e.reply_to_message.from_user:
        target_mention = e.reply_to_message.from_user.mention

    status_msg = await e.reply_text(f"🔥 Porn Spam shuru! `{counts}` msgs...")

    sent = 0
    client_index = 0
    while sent < counts:
        idx, client = active_clients[client_index % len(active_clients)]
        porn = random.choice(pornlinks)
        caption = f"{target_mention} {random.choice(RAID)}" if target_mention else random.choice(RAID)

        try:
            if ".jpg" in porn or ".png" in porn:
                await client.send_photo(chat.id, porn, caption=caption)
            elif ".mp4" in porn.lower():
                await client.send_video(chat.id, porn, caption=caption)
            else:
                await client.send_message(chat.id, caption)
            sent += 1
        except FloodWait as fw:
            await asyncio.sleep(fw.value + 1)
            continue
        except Exception as ex:
            print(f"Client{idx} pspam error: {ex}")
            sent += 1

        client_index += 1
        await asyncio.sleep(0.1)

    try:
        await status_msg.edit(f"✅ Porn Spam complete! `{sent}` msgs bheje!")
    except Exception:
        pass

    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Porn Spam By: {e.from_user.id}\nChat: {e.chat.id}\nCount: {sent}",
            )
        except Exception as a:
            print(a)


@Client.on_message(filters.user(sudos) & filters.command(["hang"], prefixes=HANDLER))
async def _hangchat(Badmunda: Client, e: Message):
    usage = f"Command: {HANDLER}hang (count)"
    try:
        count = int(e.text[5:].strip())
    except (ValueError, IndexError):
        return await e.reply_text(usage)

    if count <= 0:
        return await e.reply_text("Valid count do!")

    active_clients = get_active_clients()
    if not active_clients:
        return await e.reply_text("Koi active bot nahi mila!")

    messhang = "⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰😈꙰꙰꙰꙰꙰꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰"

    status_msg = await e.reply_text(f"💥 Hang shuru! `{count}` msgs bhejenge...")
    sent = 0
    client_index = 0

    while sent < count:
        idx, client = active_clients[client_index % len(active_clients)]
        try:
            await client.send_message(e.chat.id, messhang)
            sent += 1
        except FloodWait as fw:
            await asyncio.sleep(fw.value + 1)
            continue
        except Exception as ex:
            print(f"Client{idx} hang error: {ex}")
            sent += 1

        client_index += 1
        await asyncio.sleep(0.05)

    try:
        await status_msg.edit(f"✅ Hang complete! `{sent}` msgs bheje!")
    except Exception:
        pass

    if LOG_CHANNEL:
        try:
            await Badmunda.send_message(
                LOG_CHANNEL,
                f"Hang By: {e.from_user.id}\nChat: {e.chat.id}\nCount: {sent}",
            )
        except Exception as a:
            print(a)
