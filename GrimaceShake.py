print("\n*************************************************\n")

print("Weather Branch")

#Import Libraries Here
import random
from time import sleep

#Create a function that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowy","blizzard","raining","foggy","windy","icy","sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call the weather() once VRS(Vehicle Response System)
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        sleep(1.25)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.25)
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.25)
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 25 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.25)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 5 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.25)
        print("VRS has been engaged only allowing you to drive 65mph")
    elif weatherAlert == "icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.25)
        print("VRS has been engaged only allowing you to drive 25mph")
    else:
        print("\nNational Weather Service has updated our alarm by 0 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.25)
        print("VRS has been engaged only allowing you to drive 100mph")


vehicleResponseSystem()