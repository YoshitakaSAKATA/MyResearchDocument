#!/usr/bin/python3

import socket
import sys
import pickle
import struct
from picamera2 import Picamera2

picam2=Picamera2()
picam2.options["quality"] = 90
picam2.options["compress_level"] = 1
picam2.configure(picam2.create_video_configuration({"size": (640,480),"format": "RGB888"}, buffer_count=2)) 
picam2.start()
# PCへの接続設定
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.11.19', 12345)) # PCのIPアドレスとポート番号を指定

while True:
    frame = picam2.capture_array()
    # 映像をシリアライズ
    data = pickle.dumps(frame)
    # 映像のサイズをバイトでパック
    message_size = struct.pack("L", len(data))
    
    # 映像のサイズを送信
    client_socket.sendall(message_size)
    # 映像データを送信
    print("sending cameraA now!")
    client_socket.sendall(data)

# 接続をクローズ
client_socket.close()