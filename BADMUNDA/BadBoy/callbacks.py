from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from BADMUNDA.cmd_help import *
from Data import Data


@Client.on_callback_query()
async def _callbacks(Badmunda: Client, callback_query: CallbackQuery):
    user = await Badmunda.get_me()
    user.mention
    query = callback_query.data.lower()
    if query.startswith("helpmenu1"):
        if query == "helpmenu1":
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.id
            await Badmunda.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="🚬 ʜᴇʟᴘ ᴍᴇɴᴜ 🚬\n\n   Powered By @CENSORED_POLITICSSS",
                reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
            )
    elif query == "close":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Badmunda.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="ʜᴇʟᴘ ᴍᴇɴᴜ ʜᴀs ʙᴇᴇɴ ᴄʟᴏsᴇᴅ \n\n          © @CENSORED_POLITICSS",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.REVERT),
        )
    elif query == "banall":
        await callback_query.answer(banall_help, show_alert=True)
    elif query == "birthday":
        await callback_query.answer(birthday_help, show_alert=True)
    elif query == "core_help1":
        await callback_query.answer(core_help1, show_alert=True)
    elif query == "core_help2":
        await callback_query.answer(core_help2, show_alert=True)
    elif query == "evaluators_help1":
        await callback_query.answer(evaluators_help1, show_alert=True)
    elif query == "evaluators_help2":
        await callback_query.answer(evaluators_help2, show_alert=True)
    elif query == "gwish_help1":
        await callback_query.answer(gwish_help1, show_alert=True)
    elif query == "gwish_help2":
        await callback_query.answer(gwish_help2, show_alert=True)
    elif query == "gwish_help3":
        await callback_query.answer(gwish_help3, show_alert=True)
    elif query == "lslove_help1":
        await callback_query.answer(lslove_help1, show_alert=True)
    elif query == "lslove_help2":
        await callback_query.answer(lslove_help2, show_alert=True)
    elif query == "lslove_help3":
        await callback_query.answer(lslove_help3, show_alert=True)
    elif query == "lslove_help4":
        await callback_query.answer(lslove_help4, show_alert=True)
    elif query == "raid_help1":
        await callback_query.answer(raid_help1, show_alert=True)
    elif query == "raid_help2":
        await callback_query.answer(raid_help2, show_alert=True)
    elif query == "raid_help3":
        await callback_query.answer(raid_help3, show_alert=True)
    elif query == "raid_help4":
        await callback_query.answer(raid_help4, show_alert=True)
    elif query == "shayri_help1":
        await callback_query.answer(shayri_help1, show_alert=True)
    elif query == "shayri_help2":
        await callback_query.answer(shayri_help2, show_alert=True)
    elif query == "spam_help1":
        await callback_query.answer(spam_help1, show_alert=True)
    elif query == "spam_help2":
        await callback_query.answer(spam_help2, show_alert=True)
    elif query == "spam_help3":
        await callback_query.answer(spam_help3, show_alert=True)
    elif query == "spam_help4":
        await callback_query.answer(spam_help4, show_alert=True)
    elif query == "unlimited_help1":
        await callback_query.answer(unlimited_help1, show_alert=True)
    elif query == "unlimited_help2":
        await callback_query.answer(unlimited_help2, show_alert=True)
    elif query == "unlimited_help3":
        await callback_query.answer(unlimited_help3, show_alert=True)
    elif query == "unlimited_help4":
        await callback_query.answer(unlimited_help4, show_alert=True)
    elif query == "unlimited_help5":
        await callback_query.answer(unlimited_help5, show_alert=True)

    # For Future Use
    elif query == "helpmenu2":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Badmunda.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  @CENSORED_POLITICSSS",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU2),
        )
    elif query == "helpmenu3":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.id
        await Badmunda.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="ʜᴇʟᴘ ᴍᴇɴᴜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ  @CENSORED_POLITICSSS",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU3),
        )
