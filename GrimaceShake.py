print("***********************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

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

print(gasLevelGauge())
print(listOfFasStations())
