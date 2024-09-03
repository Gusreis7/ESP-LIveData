import json
import time
from datetime import datetime
from flask import Flask, Response, render_template, stream_with_context
from src.sensorDHT import SensorDht

application = Flask(__name__)
sensor = SensorDht(url='http://192.168.100.34', port=80, endpoints=['humidity', 'temperature'])

def generate_sensor_data():
    while True:
        time.sleep(0.2)
        
        # Coleta os dados de ambos os endpoints
        humidity_data = sensor.request_endpoint(endpoint='humidity')
        temperature_data = sensor.request_endpoint(endpoint='temperature')
        
        # Gera JSON para o endpoint de "humidity"
        humidity_json_data = json.dumps({
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'value': humidity_data,
            'endpoint': 'humidity'
        })
        yield f"data:{humidity_json_data}\n\n"
        
        # Gera JSON para o endpoint de "temperature"
        temperature_json_data = json.dumps({
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'value': temperature_data,
            'endpoint': 'temperature'
        })
        yield f"data:{temperature_json_data}\n\n"

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/chart-data')
def chart_data():
    response = Response(stream_with_context(generate_sensor_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

if __name__ == '__main__':
    application.run(debug=True, threaded=True,host='0.0.0.0')
