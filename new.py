import qrcode # type: ignore

qr_img =qrcode.make("I LOVE YOU")


qr_img.save("qr-img.jpg")
