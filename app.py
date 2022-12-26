from flask import Flask, render_template, jsonify
from bme_module import BME280Module

app = Flask(__name__)

bme280_module = BME280Module()

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/sensorReadings")
def get_sensor_readings():
    temperature, pressure, humidity, altitude = bme280_module.get_sensor_readings()
    return jsonify(
        {
            "status": "OK",
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
            "altitude": altitude,
        }
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
