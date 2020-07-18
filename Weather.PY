"""Author: Karen "Segan" Reed 59 """
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#My API key: 4681e9fc94f46077b5d88b8286613e55
import tkinter as tk
import requests
import json

#Create a function that will convert our farenheit temperatures to celcius so both results can be displayed.
def convert_celcius(temp):
    celcius=round((temp-32)*5 / 9, 2)
    return(celcius)

def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        celcius = convert_celcius(temp)
        feels = weather['main']['feels_like']
        feelsC=convert_celcius(feels)
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']

        # final_str = 'City: %s, %s \nConditions: %s \nTemperature (°F): %s \n Feels Like: %s' % (name, country, desc, temp, celcius, feels)
        final_str = '%s, %s \nConditions: %s \nTemperature: %s°F | %s°C\n Feels Like: %s°F | %s °C\n Humidity: %s\n Wind Speed: %sm/h' % (
        name, country, desc, temp,celcius, feels, feelsC, humidity, wind)
    except:
        final_str = 'An Error has Occurred, please try again!'

    return final_str


def get_weather(city):
    weather_key = '4681e9fc94f46077b5d88b8286613e55'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    print(weather)
    format_response(weather)

    label['text'] = format_response(weather)


"""city=input("Please input your city!\n")
get_weather(city)"""
height = 700
width = 700
frameColor = "#340B8D"
bgColor = "#BFDFEC"

root = tk.Tk()

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

background_image = tk.PhotoImage(file='storm.png')
bgLabel = tk.Label(root, bd=5, bg="black", image=background_image)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# create the frame for where the user instructions will go and add a label that has those instructions.
instructionFrame = tk.Frame(root, bg=frameColor, bd=20)
instructionFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.15, anchor='n')
instructionLabel = tk.Label(instructionFrame, bg=bgColor, font=24,
                            text="Please enter your city or zip code and the \n2 letter country code to get the current weather! \n(Ex: New York, US or 33098, DE)")
instructionLabel.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg=frameColor, bd=10)
frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

input = tk.Entry(frame, bg=bgColor, font=40)
input.place(relx=.025, relwidth=0.65, relheight=1)
#make the button execute weather search function by retriving
button = tk.Button(frame, text="Search", activebackground='#CBEEB6', font=24, command=lambda: get_weather(input.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

resultsFrame = tk.Frame(root, bg=frameColor, bd=20)
resultsFrame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.50, anchor='n')

label = tk.Label(resultsFrame, bg=bgColor, font=1000)
label.place(relwidth=1, relheight=1)

root.mainloop()
