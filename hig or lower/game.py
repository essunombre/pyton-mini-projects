import random
from game_data import data as dt
# from art import logo
#from art import vs
# print(logo)
# print(dt)
# print(len(dt))
score = 0


def get_celebrity():
    random_celebrity = random.randint(0, 50-1)
    return dt[random_celebrity]


def get_bio(celebrity):
    name = (celebrity["name"])
    description = (celebrity["description"])
    country = (celebrity["country"])
    return(f"{name}, a {description}, from {country}.")\



def compare(selection):
    if selection == "a" and celebrity_a["follower_count"] > celebrity_b["follower_count"]:
        return True
    elif selection == "b" and celebrity_b["follower_count"] > celebrity_a["follower_count"]:
        return True
    else:
        return False


winning = True
while winning:
    celebrity_a = get_celebrity()
    celebrity_b = get_celebrity()
    print(f"Compare A: {get_bio(celebrity_a)}")
    print(f"Against B: {get_bio(celebrity_b)}")
    selection = input("Who has more followes? Type A or B: ").lower()
    if (compare(selection)):
        score += 1
        # clear
        print(f"You're right current score: {score}.")
    else:
        winning = False
        # clear
        print(f"Sorry, that's wrong. Final score: {score}")
