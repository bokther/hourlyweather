import datetime
import requests

locations = {
        "Newark, DE": '337531',
        "Wilmington, DE": '327535',
        "Clementon, NJ": '2175028',
        "West Berlin, NJ": '2208734'
    }

parameters = {"apikey": ''} # <- Your API key goes here
hourly = requests.get('http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/'
                      +locations["Wilmington, DE"],
                      params=parameters)
data = hourly.json()

if __name__ == "__main__":
    for i in data:
        time_tag = datetime.datetime.fromtimestamp(i['EpochDateTime'])
        time_tag = time_tag.strftime("%I:%M %p")
        print('[{}] Weather: {}, Precipitation: {}%, Type: {}'.format(
            time_tag, i['Temperature']['Value'],
            i['PrecipitationProbability'], i['IconPhrase']))

	
