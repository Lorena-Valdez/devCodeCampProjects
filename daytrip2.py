
import random

destinations = ["New York", "Chicago", "Miami", "Los Angeles", "Seattle"]

transportations = ["by train", "by bus", "via teleportation", "by automobile"]

restaurants = ["Mexican restaurant", "Greek restaurant", "Food Truck", "French restaurant"]

entertainments =["a museum", " the waterfront", "a spa day", "hiking", "sightseeing"]

def randomly_select (choices_list):
    bool = True
    while bool:
        selection = random.choice (choices_list)
        print (f"{selection} has been randomly selected for you.")
        user_input = input ("Are you happy with this selection? y/n ")
        if user_input == "y":
            bool = False

    return selection


destination = randomly_select (destinations)
transportation = randomly_select (transportations)
restaurant = randomly_select (restaurants)
entertainment = randomly_select (entertainments)


user_imput = input ("Ready to confirm your choices? y/n ")

if user_imput == "y":
    print ("Your day trip is confirmed!") 
        
if user_imput =="n":
    print ("Sorry to hear that. Let's try again!") 
    destination = randomly_select (destinations)
    transportation = randomly_select (transportations)
    restaurant = randomly_select (restaurants)
    entertainment = randomly_select (entertainments)
    
    user_input = input ("Are you ready to confirm your trip? y/n ")
    if user_input == "y":

        print (f"Enjoy your trip to {destination}, arriving {transportation}, after a day of {entertainment}, you will have dinner at a {restaurant}. Thank you for using Day Trip Planner!")
          

    

