from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery

@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""❓ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @tg_video_stream to your group.
4.) turn on the voice chat first before start to stream video.
5.) type /stream (reply to video) to start streaming.
6.) type /stop to end the video streaming.

⚡ __Maintained by Veez Project Team__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ))

@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
  await query.edit_message_text(f"✨ **Hello, I am a telegram video streaming bot.**\n\n💭 **I was created to stream videos in group video chats easily.**\n\n❔ **To find out how to use me, please press the help button below** 👇🏻",
                                reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "❔ HOW TO USE THIS BOT", callback_data="cbguide")
                       ],[
                          InlineKeyboardButton(
                             "🌐 Terms & Condition", callback_data="cbinfo")
                       ],[
                          InlineKeyboardButton(
                             "👩🏻‍💻 Developer", url="https://t.me/dlwrml")
                       ],[
                          InlineKeyboardButton(
                             "💭 Group", url="https://t.me/VeezSupportGroup"),
                          InlineKeyboardButton(
                             "✨ Channel", url="https://t.me/levinachannel")
                       ]]
                    ))

@Client.on_callback_query(filters.regex("cbinfo"))
async def cbinfo(_, query: CallbackQuery):
  await query.edit_message_text(
    f"""🌐 **bot information**

🤖 __This bot was created to stream video in telegram group video chats using several methods from WebRTC.__

💡 __Powered by PyTgcalls the Async client API for the Telegram Group Calls, and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots.__

👨🏻‍💻 __Thanks to the developers who participated in the development of this bot, the list of devs can be seen below:__

👩🏻‍✈️ » [Levina](https://github.com/levina-lab)
🤵🏻 » [Sammy-XD](https://github.com/Sammy-XD)
🤵🏻 » [Achu](https://github.com/Achu2234)

__This bot licensed under GNU-GPL 3.0 License__""",
    reply_markup=InlineKeyboardMarkup(
      [[
        InlineKeyboardButton(
          "🏡 Go Back", callback_data="cbstart")
      ]]
    ),
    disable_web_page_preview=True
  )
