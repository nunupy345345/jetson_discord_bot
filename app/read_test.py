import Jetson.GPIO as GPIO
import time

PIN = 32  # 物理ピン番号
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("------ lead switch test ------")

try:
    while True:
        state = GPIO.input(PIN)
        if state == GPIO.LOW:
            print("CLOSE（磁石近い）",state)
        else:
            print("OPEN（磁石離れている）")
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
