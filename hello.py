from flask import Flask, render_template, request, jsonify
import requests
import json
from bs4 import BeautifulSoup as bs
import jsonify
import phonenumbers
import random as rand

def countrycode():
    one = phonenumbers.example_number_for_type("ID", phonenumbers.PhoneNumberType.MOBILE)

    # Format nomor telepon menggunakan format internasional
    two = phonenumbers.format_number(one, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    three = two.split(" ")
    country_code = three[0]
    return country_code

def random():
    random_number = ''.join([str(rand.randint(0, 9)) for _ in range(8)])
    return random_number

def phonenumber():
    number = f"{countrycode()}89{random()}"
    return number

app = Flask(__name__)

@app.route('/')
def get_ip():
    url = 'https://whatismyipaddress.com/'
    r = requests.get(url).text
    soup = bs(r, 'html.parser')
    ip = soup.find('p', class_='ip-address').text
    return scamalytics(ip)

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
        rate = "low"
        scr = score
        return vpn_detection(scr, ip, rate)
    elif score in medium:
        rate = "medium"
        scr = score
        return vpn_detection(scr, ip, rate)
    elif score in high:
        rate = "high"
        scr = score
        return vpn_detection(scr, ip, rate)
    else:
        rate = "unknown"
        scr = 'null'
        return vpn_detection(scr, ip, rate)

def vpn_detection(scr, ip, rate):
    api_key = 'CLqNigaNMCMLTON37NyaTW38ukdZDaMY'
    url = f"https://www.ipqualityscore.com/api/json/ip/{api_key}/{ip}"
    r = requests.get(url)
    data = r.json()
    vpn = data['vpn']
    proxy = data['proxy']
    if vpn == "True" or proxy == "True":
        vpn = "IP is a VPN or Proxy"
        color = "red"
        return fake_address(scr, ip, rate, vpn, color)
    else:
        vpn = "IP is not a VPN or Proxy"
        color = "green"
        return fake_address(scr, ip, rate, vpn, color)

def fake_address(scr, ip, rate, vpn, color):
    url = f"http://sanzstores.my.id/fakesz/?loc=id"
    r = requests.get(url).text
    soup = bs(r, 'html.parser')
    jalan = soup.find('input', id='test1')['value']
    kota = soup.findAll('input', id='test2')[0]['value']
    provinsi = soup.findAll('input', id='test2')[1]['value']
    kode_pos = soup.findAll('input', id='test2')[2]['value']
    negara = soup.findAll('input', id='test2')[3]['value']
    fullname = soup.findAll('input', id='test2')[4]['value']
    number = phonenumber()
    return render_template('index.html', score=scr, fullname=fullname, number=number, jalan=jalan, kota=kota, provinsi=provinsi, kode_pos=kode_pos, negara=negara, ip=ip, rate=rate, vpn=vpn, color=color)

# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
