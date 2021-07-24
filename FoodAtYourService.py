import googlemaps

gmaps = googlemaps.Client(key='PUT_YOUR_API_KEY_HERE')

score = 0 
print("Welcome to our trivia game! This game will be focused around food and water resources in our community and globally.")
print("Score: " + str(score) + "\n")

water = float(input("Guess how many people (in billions) globally doesn't have access to safely managed drinking water? \n"))

if water == 2.2:
    score += 1 
    print("""You are correct!, About 1 in 3 people in the world doesn't have access to clean water. Drinking water that is not safely managed or cleaned can lead to infections or even deadly diseases.""")
else:
    print("""2.2 billion people do not have safely managed drinking water services and there are huge gaps in the quality of services provided globally.""")
print("Score: " + str(score) + "\n")

purify = input("Which of the following aren't ways that can purify water: cleaning water with household chlorine/bleach, cooling water, and clay vessel filtration. \n")

if purify == "cooling water":
    score += 1
    print("""You are correct! Cooling water isn't an effective way of cleaning water but boiling water is. Boiling water ensures that the bacteria and viruses in the water are killed.""")
elif purify == "cleaning water with household clorine/bleach":
    print("""This is a perfectly viable way to purify water if you don't have access to a boiler. Chlorine/ bleach acts as a disinfectant so it's able to kill disease-causing organisms. 
The correct answer is cooling water. """)
else:
    print("""For developing countries that don't have much access to clean water or resources, clay pots can be used to filter water. These ceramics are able to prevent almost all of the bacteria from getting into the water supply.
The correct answer is cooling water. """)
print("Score: " + str(score) + "\n")

solutions = input("""Out of the list of solutions: increasing food waste, climate smart agriculture, neglecting hygeine and sanitation, which do you think will help solve world hunger? \n""")

if solutions == "climate smart agriculture":
    score += 1
    print("""You are correct! Climate change actually prolongs world hunger. Unpredictable climates like floods, high temperatures, and dry climates can lead to drastic damage on crops, contributing to the shortage of food available. Thus climate smart agriculture includes practices that ensures farmers are prepared for unpredictable climates.""")
elif solutions == "increasing food waste":
    print("""Increasing food waste would further contribute to global hunger because as of now,about 1/3 of all the food produced are wasted. A lot of other natural resources like water are lost in the process of food waste. 
The correct answer is climate smart agriculture. """)
else:
    print("""People and especially children who live in areas that have poor hygeine practices are more likely to contract diarrhea or diseases that prevent them from obtaining their nutrients even if they are eating enough. It's important to drink and use uncontaminated water since doing so can often save a life.
The correct answer is climate smart agriculture.""")
print("Score: " + str(score) + "\n")

pillars = input("""Which one of the the four pillars of food security: food availability, food access, food use, and food stability concerns fluctuating prices of certain foods?\n""")
if pillars == "food stability":
  score += 1
  print("Correct! The fluctuating prices of certain foods due to the changes in demand of urban populations create a barrier to people in food consumption.")
elif pillars == "food availability":
  print("""Food availability concerns the effect on the food supply which may run insufficient due to competition 
between areas used for agricultural production and areas used for expanding urban settlements.
Food stability is the correct answer.""")
elif pillars == "food access":
  print("""Food access concerns high prices that may put up a restriction into consumption of the desired food needs.
Food stability is the correct answer.""")
else:
  print("""Food use concerns the lack of regulations in the urban setting for street stands and commercial workers 
that impact low food security. Food stability is the correct answer.""")
print("Score: " + str(score) + "\n")
print("Your final score: " + str(score) + "\n")

print("Next we will allow you to find services near your whether it be food or health services. \n")

foodservices = input("Do you need with finding a food pantry near you? \n")
if foodservices == "yes":
    foodbank_name = []
    foodbank_address = []
    name = ""
    address = ""
    for place in gmaps.places(query="food bank", type="food bank").get("results"):
        placeid = place["place_id"]
        field = ["name","opening_hours"]
        details = gmaps.place(place_id = placeid, fields = field)

        try:
            for i in details:
                if details["result"]["opening_hours"]["open_now"] == True:
                    name = place.get("name")
                    foodbank_name.append(name) 
                    address = place.get("formatted_address")
                    foodbank_address.append(address)

        except KeyError:
            pass

    print("Here is the closest food pantry near your location that is open now: ")
    foodbank = {foodbank_name:foodbank_address for foodbank_name, foodbank_address in zip(foodbank_name, foodbank_address)}
    for i in foodbank:
        print(" - " + i + ": " + foodbank[i] + "\n")    
else:
    clinic_name = []
    clinic_address = []
    title = ""
    location = ""
    for place in gmaps.places(query= "clinic", type = "clinic").get("results"):
        placeid = place["place_id"]
        field = ["name", "opening_hours"]
        details = gmaps.place(place_id = placeid, fields = field)
        
        try:
            for i in details:
                if details["result"]["opening_hours"]["open_now"] == True:
                    title = place.get("name")
                    clinic_name.append(title)
                    location = place.get("formatted_address")
                    clinic_address.append(location)
        except KeyError:
            pass

    print("Here is the closest clinic near your location that is open now: ")
    clinic = {clinic_name: clinic_address for clinic_name, clinic_address in zip(clinic_name, clinic_address)}
    for i in clinic:
        print(" - " + i + ": " + clinic[i] + "\n")

print("Thank you for playing!")