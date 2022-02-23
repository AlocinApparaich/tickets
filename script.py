from PIL import Image, ImageFont, ImageDraw




my_image=Image.open('frame.png')
fontnumero=ImageFont.truetype('HarmoniaSansProCyr-Bold.ttf',44)
fontdata=ImageFont.truetype('HarmoniaSansProCyr-Regular.ttf',46)
fontorario=ImageFont.truetype('HarmoniaSansProCyr-Bold.ttf',55)

orariopartenza='09:34'
orarioarrivo='10:06'
miadata='22 Febbraio 2022'
numerotreno='0001'
image_editable = ImageDraw.Draw(my_image)

image_editable.text((380,640), miadata, (42, 99, 100), font=fontdata)
image_editable.text((893,640), orarioarrivo, (42, 99, 100), font=fontorario)
image_editable.text((98,640), orariopartenza, (42, 99, 100), font=fontorario)
image_editable.text((194,522), numerotreno, (0, 0, 1), font=fontnumero)
my_image.save("result.png")