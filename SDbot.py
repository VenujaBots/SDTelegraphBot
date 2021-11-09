#    This file is part of the ChannelAutoForwarder distribution (https://github.com/VenujaBots/SDTelegraphBot).
#    Copyright (c) 2021 Venuja

import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,InlineKeyboardMarkup, InlineKeyboardButton,CallbackQuery, InlineQuery)

SDBots = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.BOT_TOKEN,
)

@SDBots.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Proccesing...`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("Uploading...`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`Something went wrong`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@SDBots.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`Proccesing...`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`Uploading...`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb")

@SDBots.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Proccesing...`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Uploading...")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Something really Happend Wrong...") 
  else:
    await message.reply_text("Size Should Be Less Than 5 MB")

STICKER = "CAACAgUAAxkBAAEBT4Bhih3lL3FSMYx1pFvEwwwplJfqhQACJgQAAgjSKFSQdidotfevrCIE"
      
@SDBots.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('Help ❓', callback_data='help'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('Channel 🙋‍♀️', url='https://t.me/vndtranslatebotsupport'),
        InlineKeyboardButton('Subscribe 🙂', url='https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await SDBots.send_message(
        chat_id=message.chat.id,
        text="""👋 Hey there,
        
Im a Vnd Telegraph Uploader I can Upload Photo.Video & Gif
        
First Send me photo, video or gif to upload Telegraph
Made By @Venuja_Sadew. 🔥""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@SDBots.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('Home ', callback_data='home'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ],
    [
        InlineKeyboardButton('Channel 🙋‍♀️', url='https://t.me/vndtranslatebotsupport')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await SDBots.send_message(
        chat_id=message.chat.id,
        text="""There Is Nothung To KnowMore,
        
Just Send me Photo, Video or Gif Upto 5MB
I Can Upload to telegraph and Give You The Direct Link""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@SDBots.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)

SDBots.run()
