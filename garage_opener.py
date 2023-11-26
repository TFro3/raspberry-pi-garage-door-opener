from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)

last_operated = time.strftime('%m/%d/%Y %H:%M:%S')

@app.route('/')
def index():
    return render_template('index.html', last_operated=last_operated)

@app.route('/open')
def open():
    global last_operated

    try:
        GPIO.output(18, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(18, GPIO.HIGH)
        last_operated = time.strftime('%m/%d/%Y %H:%M:%S')
        return 'Successfully toggled the garage door'
    except:
        return 'Error: Unable to toggle the garage door'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
