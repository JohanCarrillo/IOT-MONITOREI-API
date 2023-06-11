import requests

dato = {
    "lugar": "Medellin",
    "temperatura": 50,
    "humedad": 67
}

res = requests.post("http://localhost:8000/monitoreo", json=dato)

print(res.text)