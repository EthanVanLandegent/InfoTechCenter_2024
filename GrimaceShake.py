print("***********************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random
from time import sleep

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



gasLevelAlert()

