import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Token desde variable de entorno
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Imagen y enlace del botón
IMAGE_URL = 'https://i.postimg.cc/v8xZPMkN/IMG-8499.jpg'
BOTON_URL = 'https://tinyurl.com/TORTILLERAS'

# Crear la botonera
def crear_botonera():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔐𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔐", url=BOTON_URL),
        InlineKeyboardButton("¿𝐂𝐨́𝐦𝐨 𝐝𝐞𝐬𝐛𝐥𝐨𝐪𝐮𝐞𝐚𝐫?", callback_data='ayuda')
    )
    return markup

# Comando /start
@bot.message_handler(commands=['start'])
def enviar_bienvenida(message):
    bot.send_photo(
        chat_id=message.chat.id,
        photo=IMAGE_URL,
        reply_markup=crear_botonera()
    )

# Manejar el botón de ayuda (popup)
@bot.callback_query_handler(func=lambda call: call.data == 'ayuda')
def responder_callback(call):
    bot.answer_callback_query(
        callback_query_id=call.id,
        text="𝐏𝐫𝐞𝐬𝐢𝐨𝐧𝐞 𝐞𝐥 𝐛𝐨𝐭𝐨́𝐧 𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑 𝐲 𝐜𝐨𝐦𝐩𝐚𝐫𝐭𝐞 𝐞𝐥 𝐞𝐧𝐥𝐚𝐜𝐞 𝐜𝐨𝐧 𝟓 𝐚𝐦𝐢𝐠𝐨𝐬 𝐝𝐞 𝗪𝐡𝐚𝐭𝐬𝐀𝐩𝐩 𝐩𝐚𝐫𝐚 𝐝𝐞𝐬𝐛𝐥𝐨𝐪𝐮𝐞𝐚𝐫 𝐞𝐥 𝐜𝐚𝐧𝐚𝐥 𝐓𝐎𝐑𝐓𝐈𝐋𝐋𝐄𝐑𝐀𝐒.",
        show_alert=True
    )

# Mantener el bot activo
bot.infinity_polling()
