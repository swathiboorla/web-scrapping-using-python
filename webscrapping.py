import requests
from bs4 import BeautifulSoup
import smtplib
import ssl

# Email credentials
email_sender = '#sender emailaddress'#ex:jhon@gmail.com
email_password = 'password'  # Replace with App Password
email_receiver = '#receiver address'#ex:ram@gmail.com

# Function to get weather data
def get_weather(city):
    # Example website for weather (you can replace this with any other reliable source)
    url = f'https://www.weather-forecast.com/locations/{city}/forecasts/latest'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example of extracting specific data (this might change based on the website structure)
    weather_info = soup.find('div', class_='b-forecast__table-days-name').get_text()
    temp_info = soup.find('span', class_='temp').get_text()
    return f"Weather: {weather_info}, Temperature: {temp_info}"

# Function to send email
def send_email(subject, body):
    message = f"Subject: {subject}\n\n{body}"
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, message)
    except smtplib.SMTPAuthenticationError as e:
        print(f"Failed to login: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main logic
def main():
    city = 'Hyderabad'  # Replace with your target city
    weather_data = get_weather(city)
    
    # Example condition for an alert (customize based on actual data)
    if 'Rain' in weather_data or 'Snow' or 'Haze' or 'showers'or 'coludy'or'Rain and snow'or 'rainy' in weather_data:
        subject = f"Weather Alert for {city} to carry an umbrella"
        body = f"Alert! The weather in {city} has the following conditions:\n\n{weather_data}"
        send_email(subject, body)
        print("Weather alert sent!")
    else:
        print("No alert needed. Weather is fine.")

if __name__ == '__main__':
    main()
