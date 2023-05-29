import logging
from telegram.ext import Updater, CommandHandler
import youtube_dl
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! Please enter the YouTube video URL to download music.")
def download_audio(update, context):
    url = update.message.text
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info['title']
        ydl.download([url])
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Downloaded: {title}")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token='6054021931:AAHCMiCAdS5XJM4z2mPe1g0gVS7tOoWy6Uk', use_context=True)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(MessageHandler(Filters.text, download_audio))
updater.start_polling()

