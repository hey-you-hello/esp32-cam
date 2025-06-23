## 韌體 ##
就那個 firamwarm.bin
> 這個韌體是esp32-cam專用的韌體
> 通用版本的拍照要自己寫
## 驅動 ##
[driver](https://github.com/hey-you-hello/esp32-cam/blob/main/drriver.zip)

## main.py ##
介紹
- 透過udp進行極高效傳輸
- 一開機就會偵聽所有連線已確認電腦位址 (偵聽0.0.0.0,8080)
- camera.framesize(10) 可以往下填，不能往上 10代表的是800x600巷素 範圍:1-14
- camera.quality(60)  可以往下填到30，範圍:1-63 數字越高品質越低
> 圖片品質太高 像素太多 或者變化太快都有可能崩潰
## requ.py ##
介紹
- 對所有192.168.4.x進行掃描來確認晶片位址
- 使用cv2進行自動解碼
- tkinter 做及時串流顯示
- 監聽鍵盤按鍵w來模擬操控馬達供電（現在先用LED)
> 可以自行家上a s d然後加裝馬達模組實現遙控車




