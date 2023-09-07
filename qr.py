# import qrcode

# open_app = "https://chat.openai.com/"

# img = qrcode

# img.save("open_app.png")

import segno

open_app="https://chat.openai.com/"

qr_code=segno.make(open_app)

qr_code.save("open_ai.png",dark="yellow",scale=10)