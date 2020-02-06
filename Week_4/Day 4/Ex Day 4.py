# 1.
# import random
# def get_random_temp(season):
#     if season == 'winter':
#         temp = float(random.randint(-10, 12))
#     elif season == 'Spring' or season == 'Autumn':
#         temp = float(random.randint(13, 25))
#     else:
#         temp = float(random.randint(26, 40))
#     print(temp)

# 2. Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature, together with a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# def main():
#     season = input("What season is it? ")
#     rand_temp = (get_random_temp(season.capitalize()))
#     print(f"The temperature right now is {rand_temp} degrees Celsius.")
#     if rand_temp < 0:
#         print("Brrr, that’s freezing! Wear some extra layers today.")
#     if 0 <= rand_temp <= 16:
#         print("Quite chilly! Don’t forget your coat.")
#     if 16 < rand_temp <= 23:
#         print("still not enough warm to me.")
#     if 23 < rand_temp <= 32:
#         print("Nice day and weather!")
#     if 32 < rand_temp <= 40:
#         print("Dont forget your bikini!")
#
# main()


