import pyinputplus as pyip
import sys

'''
POTENTIAL TODO:
-
'''

# Welcome message
print(
    "When it comes to large numbers, they are often very hard to imagine.\n",
    "For example roughly 8 billion people live on this planet.\n",
    "One way to illustrate this would be by imagining the size of the area it",
    "would take to put each of these persons on 1 square meter.\n"
    "The size of this area can then be illustrated by comparing it to a"
    "certain entity (e.g a country).\n", 
    "This is exactly what this program does.")


'''
(((OPTIONAL TODO: Let user decide if user wants to see some examples for 
inpsiration of what can be calcualted with this program. Some examples 
can be:
- Roughly 100 billion humans have existed so far (including the ones 
currentl y allive). If each needs 2 square meters as a grave how much 
space would this mean?

- Let's say you possess a property of 1000 m². If everyone of the 
currently roughly 8 billion people had such a property, 
how large would this area be?

- (In Germany 232 people live per square kilometer)
- (There are rougly X cows globally. If each needs 10 square meters as a 
grave how much space would this mean?) )))
'''


# Size of countries and other entities in km² for comparison. They
# represent a great variety of sizes on purpose.
vatican_city_size = 0.49
malta_size = 316
saarland_size = 2571.11
mallorca_size = 3603.72
israel_size = 20770
bavaria_size = 70541.57
austria_size = 83871
germany_size = 357114
japan_size = 377976
egypt_size = 1002450
china_size = 9596961
usa_size = 9525067
russia_size = 17098246
moon_surface = 37300000
earth_land_surface_size = 148940000
earth_water_surface_size = 361132000
earth_surface_size = 510072000
sun_surface_size = 6090000000000


while True:
    # User makes 3 decisions
    print(
        "Please decide on an entity that you want to be represented",
        "(e.g. type 'person').")
    entity = pyip.inputStr(prompt='>>> ')

    print(
        "Please decide how many entities you want to be represented",
        "(e.g. type '1000000' for 1 million).")
    entity_amount = pyip.inputInt(
        prompt='>>> ', min=10000, max=1000000000000000)

    
    # (((OPTIONAL-TODO: Let user decide if user's input is in m² or km². 
    # However then the  following 2 print statements and the calculation 
    # of "combined_are" needs to be adjusted. So it might not be worth 
    # it because I'll probably end up with many if/else statements. )))
    
    print("Please decide by how many m² 1", entity,
          "should be represented (e.g. type '1' for 1 m² per", entity, ").")
    square_meter_per_entity = pyip.inputFloat(prompt='>>>', min=1, max=1000000)

    print(
        "You chose the following:",
        round(square_meter_per_entity),
        "m² will represent 1",
        entity,
        "and you want to know how large the area would be for",
        f"{entity_amount:,}",
        "of them.")

    # calculate the area (in km²) the user has asked for
    combined_area = entity_amount * square_meter_per_entity / 1000000
    print("This area would be", f"{combined_area:,}", "km² which is...")

    # calculate the amount of times the asked for area fits into the 
    # countries and other entities
    '''
    (((OPTIONAL-TODO: The variables below can probably easier (with less 
    code and less dependencies) be calculated with a class. But I did 
    not know how I can proceed with the list and the dictionary 
    afterwards if I do so.)))
    '''
    '''
    TODO: below it should be calculated by deviding it by the variables 
    (so instead of "/0.49" it should be "/vatican_city_size)
    '''
    vatican_city_amount = combined_area / 0.49
    malta_amount = combined_area / 316
    saarland_amount = combined_area / 2571.11
    mallorca_amount = combined_area / 3603.72
    israel_amount = combined_area / 20770
    bavaria_amount = combined_area / 70541.57
    austria_amount = combined_area / 83871
    germany_amount = combined_area / 357114
    japan_amount = combined_area / 377976
    egypt_amount = combined_area / 1002450
    china_amount = combined_area / 9596961
    usa_amount = combined_area / 9525067
    russia_amount = combined_area / 17098246
    moon_surface_amount = combined_area / 37300000
    earth_land_surface_amount = combined_area / 148940000
    earth_water_surface_amount = combined_area / 361132000
    earth_surface_amount = combined_area / 510072000
    sun_surface_amount = combined_area / 6090000000000

    '''((( OPTIOINAL-TODO: Ideally the amount_list and the amount_dict 
    below would have its elements the other way round. Then later
    the numbers would be listed more appropriately, start with the 
    country/entity with the least amounts. I can probably do this
    by using the built-in "reversed"-function. )))
    '''

    # create an amount list in order to iterate over it later
    amount_list = [
        vatican_city_amount,
        malta_amount,
        saarland_amount,
        mallorca_amount,
        israel_amount,
        bavaria_amount,
        austria_amount,
        germany_amount,
        japan_amount,
        egypt_amount,
        china_amount,
        usa_amount,
        russia_amount,
        moon_surface_amount,
        earth_land_surface_amount,
        earth_water_surface_amount,
        earth_surface_amount,
        sun_surface_amount]

    '''
    ((( OPTIONAL-TODO: It might make more sense to call the dictionary 
    "grammar_dict" but I am not sure. I think I can leave it like 
    this at the moment._1.5.22 )))
    '''

    # create a dictionary in order to use it for the print statements 
    # later to have the countries etc. written correctly
    amount_dict = {
        vatican_city_amount: 'Vatican City',
        malta_amount: 'Malta',
        saarland_amount: 'Saarland',
        mallorca_amount: 'Mallorca',
        israel_amount: 'Israel',
        bavaria_amount: 'Bavaria',
        austria_amount: 'Austria',
        germany_amount: 'Germany',
        japan_amount: 'Japan',
        egypt_amount: 'Egypt',
        china_amount: 'China',
        usa_amount: 'the USA',
        russia_amount: 'Russia',
        moon_surface_amount: 'the surface of the moon',
        earth_land_surface_amount: 'the land surface of the earth',
        earth_water_surface_amount: 'the water surface of the earth',
        earth_surface_amount: 'the surface of the earth',
        sun_surface_amount: 'the surface of the sun'}

    # Displaying the user only the appropriate size comparisons:
    counter = 0
    for amount in amount_list:
        if amount >= 0.5 and amount <= 1000:
            print(
                "                -",
                round(
                    amount,
                    2),
                "times the area of",
                amount_dict[amount],
                ".")
            counter += 1

    if counter == 0:
        for amount in amount_list:
            if amount >= 0.01 and amount <= 10000:
                print(
                    "                -",
                    round(
                        amount,
                        2),
                    "times the area of",
                    amount_dict[amount],
                    ".")
                counter += 1

    '''TODO_Get rid of the follwing  break-statement as soon as the 
    Program is finished. If I get rid of it before the game will often 
    have issues because of an eternal loop which might raise the 
    exit-condition at some point or not'''
    # break

    # User can make another calculation or quit the program
    print("Do you want to make another calculation or quit the program?")

    proceed_how = pyip.inputMenu(
        ['AGAIN', 'QUIT'], lettered=True, numbered=False)
    print(proceed_how)

    if proceed_how == 'AGAIN':
        continue

    if proceed_how == 'QUIT':
        print("Thanks for using the program!")
        sys.exit()
