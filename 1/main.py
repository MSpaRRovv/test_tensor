import requests
import time
from datetime import datetime, timedelta
import math


def send_requests():
    url = "https://yandex.com/time/sync.json?geo=213"
    answer = requests.get(url)
    answer.raise_for_status()
    print(answer.text)

def print_time():
    url = "https://yandex.com/time/sync.json?geo=213"
    answer = requests.get(url)
    answer.raise_for_status()
    data = answer.json()

    sec = data["time"] / 1000
    h_time = datetime.fromtimestamp(sec).strftime("%d-%m-%Y %H:%M:%S")
    timezone = data["clocks"]["213"]["name"]
    offset = data["clocks"]["213"]["offsetString"]
    print(f"Текущее время в {timezone}: {h_time} ({offset})")

def get_delta_time():
    url = "https://yandex.com/time/sync.json?geo=213"
    answer = requests.get(url)
    answer.raise_for_status()
    data = answer.json()
    
    local_time = time.time()
    server_time_sec = data["time"] / 1000
    delta = server_time_sec - local_time
    return(abs(delta))

def average_delta():
    results = []
    for _ in range(5):
        delta = get_delta_time()
        results.append(delta)

    avg_delta = sum(results) / 5
    return avg_delta

send_requests()
print_time()
print(get_delta_time())
print(average_delta())