# import requests

# api_key = '16dc43258ccf9e5450dd23b561fbe83b'

# city = input('Enter city name: ')

# url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     temp = data['main']['temp']
#     desc = data['weather'][0]['description']
#     print(f'Temperature: {temp} K')
#     print(f'Description: {desc}')
# else:
#     print('Error fetching weather data')



from flask import Flask
import os,requests

app = Flask(__name__)
  
@app.route('/', methods =['GET'])
def home():
    construct_url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=" + "16dc43258ccf9e5450dd23b561fbe83b"
    response = requests.get(construct_url)

    list_of_data = response.json()
    
    html_data = f"""
    <table border="1">
    <tr>
        <td>country_code</td>
        <td>coordinate</td>
        <td>temp</td>
        <td>pressure</td>
        <td>humidity</td>
    </tr>
    <tr>
        <td>{str(list_of_data['sys']['country'])}</td>
        <td>{str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat'])}</td>
        <td>{str(list_of_data['main']['temp']) + 'k'}</td>
        <td>{str(list_of_data['main']['pressure'])}</td>
        <td>{str(list_of_data['main']['humidity'])}</td>
    </tr>

</table>
    """
    return html_data

if __name__ == "__main__":
    app.run(port = 8080,debug=True)