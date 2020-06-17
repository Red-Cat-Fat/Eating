from bot.bot import Bot
from bot.handler import MessageHandler
import secret

bot = Bot(token=secret.TOKEN)

def message_cb(bot, event):
    bot.send_text(chat_id=event.from_chat, text=event.text)


bot.dispatcher.add_handler(MessageHandler(callback=message_cb))
bot.start_polling()
bot.idle()
