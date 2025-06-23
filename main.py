import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔐 Token del bot
TOKEN = '7552009219:AAELDHnqw1wDz5u1RXrRv0mzYAHvhlzVugw'
bot = telebot.TeleBot(TOKEN)

# 🖼️ Imagen a mostrar
IMAGE_URL = 'https://i.postimg.cc/Y9PWK0q4/photo-output.jpg'

# 🔗 URL del botón principal
BOTON_URL = 'https://t.me/share/url?url=https://t.me/tortillerass'

# 🎯 Crear la botonera
def crear_botonera():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🔐𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔐", url=BOTON_URL),
        InlineKeyboardButton("¿Cómo desbloquear?", callback_data="mostrar_info")
    )
    return markup

# 👤 Responder solo en chats privados (incluye /start u otros mensajes)
@bot.message_handler(func=lambda msg: msg.chat.type == "private")
def responder_privado(msg):
    bot.send_photo(
        chat_id=msg.chat.id,
        photo=IMAGE_URL,
        reply_markup=crear_botonera()
    )

# ℹ️ Acción cuando se pulsa el segundo botón
@bot.callback_query_handler(func=lambda call: call.data == "mostrar_info")
def mostrar_info(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, "Para desbloquear, tocá el botón 🔐𝐃𝐄𝐒𝐁𝐋𝐎𝐐𝐔𝐄𝐀𝐑🔐 y comparta con 5 buenos amigos por WhatsApp")

# ▶️ Iniciar polling
bot.polling()
