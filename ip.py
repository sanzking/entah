import requests
import json
from bs4 import BeautifulSoup as bs
import jsonify
import phonenumbers
import random as rand

def get_ip():
    url = 'http://ip-api.com/json'
    r = requests.get(url)
    data = r.json()
    ip = data['query']
    return ip

def scamalytics():
    url = f"https://scamalytics.com/ip/{get_ip()}"
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    risk = soup.find('div', class_='high_risk').text
    score = soup.find('div', class_='score').text
    score = score.split(':')[1]
    score = score.replace(' ', '')
    json_data = {
        'ip': get_ip(),
        'risk': risk,
        'score': score
    }
    print(json_data)
    return json_data

def vpn_detection():
    api_key = 'CLqNigaNMCMLTON37NyaTW38ukdZDaMY'
    url = f"https://www.ipqualityscore.com/api/json/ip/{api_key}/{get_ip()}"
    r = requests.get(url)
    data = r.json()
    vpn = data['vpn']
    proxy = data['proxy']
    if vpn == "True" or proxy == "True":
        return "IP is a VPN or Proxy"
    else:
        return "IP is not a VPN or Proxy"

def countrycode():
    one = phonenumbers.example_number_for_type("ID", phonenumbers.PhoneNumberType.MOBILE)

    # Format nomor telepon menggunakan format internasional
    two = phonenumbers.format_number(one, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    three = two.split(" ")
    country_code = three[0]
    return country_code

def random():
    random_number = ''.join([str(rand.randint(0, 9)) for _ in range(10)])
    return random_number

def phonenumber():
    number = f"{countrycode()}{random()}"
    return number

def fake_address():
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
    json_data = {
        'fullname': fullname,
        'number': number,
        'address': jalan,
        'city': kota,
        'province': provinsi,
        'postal_code': kode_pos,
        'country': negara
    }
    return json_data

if __name__ == '__main__':
    scamalytics()