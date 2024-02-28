#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcome branch starts here
timeToSleep = 3

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot every 0.5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!\n")


#Gasoline branch starts here
print("***********************************\n")
print("Gasoline Branch\n")

#Function that lists Gas Levels, randomly choosing one and returing its value
def gasLevelGauge():
     gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
     currentGasLevel = random.choice(gasLevelList)
     return currentGasLevel

#Function that lists Gas Stations, randomly choosing one and returning its value
def listOfFasStations():
     gasStation = ["Shell","Speedway","Marathon","Circle K","Mobil","Costco","Meijer","7Eleven"]
     gasStationsNearby = random.choice(gasStation)
     return gasStationsNearby

#Function will call the gasLevelGauge to determine our gas level and then find a close gas station
# by calling the listOfGasStations function if we are on Low or Quarter Tank
def gasLevelAlert():
     milesToGasStationsLow = round(random.uniform(1, 25),1)
     milesToGasStationsQuarterTank = round(random.uniform(25.1, 50),1)
     gasLevelIndicator = gasLevelGauge()
     if gasLevelIndicator == "Empty":
          print("***WARNING - YOU ARE ON EMPTY***")
          sleep(1.75)
          print("\n      Calling Triple AAA")
     elif gasLevelIndicator == "Low": 
          print("Your gas tank is extremely low, checking Google Maps for the closest gas station")
          sleep(1.75)
          print("The closest gas station is",listOfFasStations(),"which is", milesToGasStationsLow,"miles away.")
     elif gasLevelIndicator == "Quarter Tank": 
          print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas station")
          sleep(1.75)
          print("The closest gas station is",listOfFasStations(),"which is", milesToGasStationsQuarterTank,"miles away.") 
     elif gasLevelIndicator == "Half Tank":
          print("Your gas tank is a half of a tank full which is plenty to get to your destination.")
     elif gasLevelIndicator == "Three Quarter Tank":
          print("Your gas tank is at three quarter tank.")
     else:
          print("Your gas tank is full")

gasLevelAlert()

print("\n***********************************\n")

print("Weather Branch")

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

