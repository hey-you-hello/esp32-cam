# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import network

import camera

ap = network.WLAN(network.AP_IF)
ap.active(True)  # 啟用 AP 模式


ap.config(essid="MICROpython_20731", password="12345678")


print("AP 設定完成")
print("AP IP 位址:", ap.ifconfig()[0])
print('開始運行主程式')

