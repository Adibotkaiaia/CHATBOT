
from pyrogram.enums import ChatMemberStatus as CMS
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup

from ROYEDITX import LOCOPILOT
from ROYEDITX.database import vick
from ROYEDITX.modules.helpers import (
    CLOSE_BTN,
    BACK,
    CHATBOT_BACK,
    DEV_OP,
    HELP_BTN,
)


@LOCOPILOT.on_callback_query()
async def cb_handler(_, query: CallbackQuery):
    # Get bot info at runtime
    bot_username = _.username
    bot_name = _.name

    if query.data == "HELP":
        await query.message.edit_text(
            text=f"""❖ ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ꜰᴏʀ {bot_name}\n\n⬤ /ping ➥ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.\n⬤ /stats ➥ ᴄʜᴇᴄᴋ ᴍʏ ᴄʜᴀᴛs sᴛᴀᴛs.\n⬤ /chatbot ➥ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ [ᴡᴏʀᴋ ᴏɴʟʏ ɢʀᴏᴜᴘ]\n\n❖ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➥ /""",
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
            disable_web_page_preview=True,
        )

    elif query.data == "CLOSE":
        await query.message.delete()
        await query.answer("❖ ᴄʟᴏsᴇᴅ ᴍᴇɴᴜ...", show_alert=True)

    elif query.data == "BACK":
        await query.message.edit(
            text=f"""❖ ʜᴇʏ ʙᴀʙʏ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ♥︎\n\n⬤ ɪ ᴀᴍ {bot_name}, ᴀɪ ʙᴀsᴇ ᴄʜᴀᴛʙᴏᴛ.\n⬤ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ғᴏʀ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ.\n\n❖ ᴛᴀᴘ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ sᴇᴇ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )

    elif query.data == "SOURCE":
        await query.message.edit(
            text=f"""❖ ʜᴇʏ ʙᴀʙʏ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ♥︎\n\n⬤ ɪ ᴀᴍ {bot_name},  ᴀɪ ʙᴀsᴇ ᴄʜᴀᴛʙᴏᴛ.\n\n❖ ɪғ ʏᴏᴜ ᴡᴀɴᴛ {bot_name} ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.""",
            reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
            disable_web_page_preview=True,
        )

    elif query.data == "BACK_HELP" or query.data == "CHATBOT_BACK":
        await query.message.edit(
            text=f"""❖ ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ꜰᴏʀ {bot_name}\n\n⬤ /ping ➥ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.\n⬤ /stats ➥ ᴄʜᴇᴄᴋ ᴍʏ ᴄʜᴀᴛs sᴛᴀᴛs.\n⬤ /chatbot ➥ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ [ᴡᴏʀᴋ ᴏɴʟʏ ɢʀᴏᴜᴘ]\n\n❖ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➥ /""",
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )

    elif query.data in ["addchat", "rmchat"]:
        user_id = query.from_user.id
        user_status = (await query.message.chat.get_member(user_id)).status

        if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            return await query.answer(
                "❖ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ !",
                show_alert=True,
            )

        is_vick = vick.find_one({"chat_id": query.message.chat.id})

        if query.data == "addchat":
            if not is_vick:
                await query.edit_message_text("❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.")
            else:
                vick.delete_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(
                    f"❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ʙʏ ➥ {query.from_user.mention}."
                )

        elif query.data == "rmchat":
            if not is_vick:
                vick.insert_one({"chat_id": query.message.chat.id})
                await query.edit_message_text(
                    f"❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ ʙʏ ➥ {query.from_user.mention}."
                )
            else:
                await query.edit_message_text("❖ ᴄʜᴀᴛ-ʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.")
