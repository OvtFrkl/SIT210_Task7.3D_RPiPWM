import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24
BUZZ = 13

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZ, GPIO.OUT)

GPIO.output(BUZZ, True)
buzzer = GPIO.PWM(BUZZ, 0.25)
buzzer.start(1)


def getDistance():
    GPIO.output(TRIG, True)

    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    stop = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        stop = time.time()

    timeDiffernce = stop - start
    distance = (timeDiffernce * 34300) / 2
    return distance


def getFrequency(distance):
    if distance > 500:
        return 0.25
    elif distance > 400:
        return 2
    elif distance > 300:
        return 3
    elif distance > 200:
        return 4
    elif distance > 100:
        return 5
    else:
        return 6


if __name__ == '__main__':
    try:
        while True:
            dist = getDistance()
            freq = getFrequency(dist)
            buzzer.ChangeFrequency(freq)
            time.sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()
        buzzer.stop()
