import cv2

# カメラデバイスを指定（通常、0は内蔵カメラを示します。外部カメラの場合、1、2、などを試すか、ファイルパスを指定できます）
cap = cv2.VideoCapture(0)

# カメラデバイスが正しくオープンされているか確認
if not cap.isOpened():
    print("カメラデバイスを開けませんでした。")
    exit()

while True:
    # フレームを1つずつ取得
    ret, frame = cap.read()

    if not ret:
        print("フレームを取得できませんでした。")
        break

    # フレームを表示
    cv2.imshow('Video Capture', frame)

    # "q"キーを押してループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 後片付け
cap.release()
cv2.destroyAllWindows()