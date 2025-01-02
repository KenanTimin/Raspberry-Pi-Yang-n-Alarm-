import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
import warnings

warnings.filterwarnings("ignore")

def mail():

    from_email_addr = "xyangin.alarmi@gmail.com"
    from_email_pass = "smoqyrrwlftnnmcp"
    to_email_addr = "kutlaykenantimin@yandex.com"

    msg = EmailMessage()

    body = "Yangın var! Yangın var! Ben Yanıyorum. Yetişine Dostlar, Tutuşuyorum!"
    msg.set_content(body)

    msg['From'] = from_email_addr
    msg['To'] = to_email_addr

    msg['Subject'] = "Yangın var!"

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(from_email_addr, from_email_pass)
    server.send_message(msg)
    server.quit()


Pin = 22
buzzer = 7
led = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Pin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)

def blink():
    GPIO.output(buzzer,GPIO.HIGH)
    GPIO.output(led,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer,GPIO.LOW)
    GPIO.output(led,GPIO.LOW)
    time.sleep(0.5)


def alert(x):
    print("Yangın var! Yangın var! Ben Yanıyorum. Yetişine Dostlar, Tutuşuyorum!")
    blink()
    mail()


def loop():
    GPIO.add_event_detect(Pin,GPIO.FALLING,callback=alert)
    while True:
        pass


try:
    loop()
except KeyboardInterrupt:
    GPIO.cleanup()
