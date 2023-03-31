import requests
from bs4 import BeautifulSoup as bs
import json

def get_ip():
    url = 'http://ip-api.com/json'
    r = requests.get(url)
    data = r.json()
    ip = data['query']
    scamalytics(ip)

def scamalytics(ip):
    url = f"https://scamalytics.com/ip/{ip}"
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    risk = soup.find('div', class_='high_risk')
    score = soup.find('div', class_='score').text
    score = score.split(':')[1]
    score = score.replace(' ', '')
    score = int(score)
    low = range(0, 30)
    medium = range(30, 70)
    high = range(70, 100)
    if score in low:
        print("low")
    elif score in medium:
        print("medium")
    elif score in high:
        print("high")
    else:
        print("unknown")

get_ip()