import requests
import schedule
import time
from pytz import timezone
def main():
    #This part is personal part
    token_line = ''
    url_line = ''
    token_aqi = ''
    lat = 0
    lon = 0
    #Api and get a data 
    url_aqi = f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={token_aqi}'
    response = requests.get(url_aqi).json()
    pm2_5_value = response["list"][0]["components"]["pm2_5"]
    header = {'Content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token_line}

    #Condition owe to saftey level
    if pm2_5_value <= 50:
        requests.post(url_line,headers=header,data = {'message':str(pm2_5_value)+' No Mask Day'})
    elif pm2_5_value >51 and pm2_5_value<=100:
        requests.post(url_line,headers=header,data = {'message':str(pm2_5_value)+' Up to you'})
    elif pm2_5_value >101 and pm2_5_value<=150:
        requests.post(url_line,headers=header,data = {'message':str(pm2_5_value)+' recommend to wear a mask'})
    elif pm2_5_value >151 and pm2_5_value<=200:
        requests.post(url_line,headers=header,data = {'message':str(pm2_5_value)+' Must wear a mask'})
    elif pm2_5_value >201 and pm2_5_value<=300:
        requests.post(url_line,headers=header,data = {'message':str(pm2_5_value)+' recommend to stay indoor'})
    elif pm2_5_value >300:
        requests.post(url_line,headers=header,data = {'message':str(pm2_5_value)+' STAY INSIDE!!!'})
#Daily running
schedule.every().day.at("06:30",'Asia/Bangkok').do(main)

while True:
    schedule.run_pending()
    time.sleep(1)