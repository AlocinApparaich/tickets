from email import message
from importlib.resources import path
import telebot
from PIL import Image, ImageFont, ImageDraw
import os




my_image=Image.open('frame.png')
fontnumero=ImageFont.truetype('HarmoniaSansProCyr-Bold.ttf',44)
fontdata=ImageFont.truetype('HarmoniaSansProCyr-Regular.ttf',46)
fontorario=ImageFont.truetype('HarmoniaSansProCyr-Bold.ttf',55)

orariopartenza=''
orarioarrivo=''
miadata=''
numerotreno=''

numero=False
orariop=False
orarioa=False
datab=False
API_TOKEN = '5191321319:AAFn4RJaYv78RCYpdNxb80UxyuS0_vz_AqA'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    global numerotreno
    global miadata
    global orarioarrivo
    global orariopartenza
    global my_image
    
    
    bot.reply_to(message, """Ciao con questo bot puoi creare biglietti trenord!""")
    

@bot.message_handler(commands='numero')
def inseriscinumero(message):
    global numero
    numero=True
    bot.reply_to(message, "Inserisci numero treno")
    

@bot.message_handler(commands='orarioa')
def inseriscinumero(message):
    global orarioa
    orarioa=True
    bot.reply_to(message, "Inserisci orario arrivo")
    
    


@bot.message_handler(commands='orariop')
def inseriscinumero(message):
    global orariop
    orariop=True
    bot.reply_to(message, "Inserisci orario partenza")
    

@bot.message_handler(commands='data')
def inseriscinumero(message):
    global datab
    datab=True
    bot.reply_to(message, "Inserisci data")
    


@bot.message_handler(commands='stampa')
def stampa(message):
    
    global numerotreno
    global miadata
    global orarioarrivo
    global orariopartenza
    my_image=Image.open('frame.png')
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((380,640), miadata, (42, 99, 100), font=fontdata)
    image_editable.text((893,640), orarioarrivo, (42, 99, 100), font=fontorario)
    image_editable.text((98,640), orariopartenza, (42, 99, 100), font=fontorario)
    image_editable.text((194,522), numerotreno, (0, 0, 1), font=fontnumero)
    my_image.save(str(message.chat.id)+".png")
    
    
    bot.send_document(chat_id=message.chat.id, document=open(str(message.chat.id)+".png", "rb"))
    os.remove(str(message.chat.id)+".png")
    
    
    
    

    



@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global numero
    global orarioa
    global orariop
    global datab
    global numerotreno
    global miadata
    global orarioarrivo
    global orariopartenza
    if(numero==True):
        numerotreno=message.text    
        numero=False
    if(orarioa==True):
        orarioarrivo=message.text
        orarioa=False
    if(orariop==True):
        orariopartenza=message.text
        orariop=False
    if(datab==True):
        miadata=message.text
        orariop=False
        

    
    
    


bot.infinity_polling()