from flask import Flask, render_template      
from flask_socketio import SocketIO
from src.sensorDHT import SensorDht
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app)

data = []

def plot_data(sensor: SensorDht, endpoint: str):
    while True:
        time.sleep(0.2)
        data.append(sensor.request_endpoint(endpoint=endpoint))
        if len(data) >= 20:
            data.pop(0)
        socketio.emit('update_chart', {'data': data})

@app.route('/')
def index():
    return render_template('index.html')  

sensor = SensorDht(url='192.168.100.34', port=80, endpoints=['humidity','temperature'])
threading.Thread(target=plot_data, args=(sensor, 'humidity')).start()  

if __name__ == '__main__':
    socketio.run(app)
