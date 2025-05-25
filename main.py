from flask import Flask, Response, request
import io
import time

import pyautogui
import pygetwindow as gw
import qrcode
from PIL import Image
from mss import mss
from pyzbar.pyzbar import decode

app = Flask(__name__)

@app.route('/qrmai')
def qrmai():
    if request.args.get('token') != config['token']:
        return "error"

    wechat = gw.getWindowsWithTitle("微信")[0]
    if wechat.isMinimized:
        wechat.restore()
    wechat.activate()

    def move_click(x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()


    move_click(config["p1"][0], config["p1"][1])

    time.sleep(2)
    move_click(config["p2"][0], config["p2"][1])

    wechat.minimize()
    time.sleep(2)
    with mss() as sct:
        # 截取整个屏幕
        screenshot = sct.grab(sct.monitors[1])  # monitors[1] 表示第一个显示器
        image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

    # 解码二维码
    decoded_objects = decode(image)

    qr_img = qrcode.make(decoded_objects[0].data.decode("utf-8"))

    import os
    # 如果skin.png存在
    img_io = io.BytesIO()
    if "skin.png" in os.listdir():
        skin = Image.open("skin.png")

        skin.paste(qr_img.resize((504,504)), (142, 1096))
        skin.save(img_io, format='PNG')
    else:
        qr_img.save(img_io, format='PNG')

    img_io.seek(0)

    window = gw.getWindowsWithTitle("微信")[0]

    window.close()
    return Response(img_io, mimetype='image/png')

if __name__ == '__main__':
    import json
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    app.run(host=config["host"], port=config["port"])