# check the weather condition

def weather_condition(season):
    if season == "Autumn":
        print("The weather is medium in autumn")
        
    elif season == "Spring":
        print("the weather is good in spring")
    else :
        print("wrong input")

season = input("Type your season")
weather_condition(season)