import json
import time
from datetime import datetime, timedelta
from flask import Flask, Response, render_template, stream_with_context, request
from src.sensorDHT import SensorDht
from src.pandasData import PandasData

application = Flask(__name__)
base = PandasData(name_run='teste')
sensor = SensorDht(url='http://192.168.100.34', port=80, endpoints=['humidity', 'temperature'])

def generate_sensor_data_with_average(update_interval_minutes):
    humidity_values = []
    temperature_values = []
    
    start_time = datetime.now()
    
    while True:
        time.sleep(0.5)
        humidity_data = sensor.request_endpoint(endpoint='humidity')
        temperature_data = sensor.request_endpoint(endpoint='temperature')

        humidity_values.append(humidity_data)
        temperature_values.append(temperature_data)

        current_time = datetime.now()
        if current_time - start_time >= timedelta(minutes=update_interval_minutes):
            humidity_avg = sum(humidity_values) / len(humidity_values)
            temperature_avg = sum(temperature_values) / len(temperature_values)
            
            humidity_values.clear()
            temperature_values.clear()

            start_time = current_time
            
            humidity_json_data = json.dumps({
                'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'value': humidity_avg,
                'endpoint': 'humidity_avg'
            })
            yield f"data:{humidity_json_data}\n\n"
            
            temperature_json_data = json.dumps({
                'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'value': temperature_avg,
                'endpoint': 'temperature_avg'
            })
            yield f"data:{temperature_json_data}\n\n"
        
      
        
        base.add_line(data=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), temperatura=temperature_data, umidade=humidity_data)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/chart-data')
def chart_data():
    # Obtém o intervalo de atualização enviado pelo usuário
    update_interval_minutes = request.args.get('update_interval', default=1, type=int)
    
    # Stream com o cálculo da média baseado no intervalo especificado
    response = Response(stream_with_context(generate_sensor_data_with_average(update_interval_minutes)), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

if __name__ == '__main__':
    application.run(debug=True, threaded=True, host='0.0.0.0')
