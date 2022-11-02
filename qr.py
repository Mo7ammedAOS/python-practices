import qrcode

link = input('Write your link here: ')
img = qrcode.make(link)
img.save(f"Qrphotos/{link[10:16:1]}.png")
