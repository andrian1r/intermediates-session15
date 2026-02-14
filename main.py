from high_logo import logo , vs
from game_data import data
import random
def format_data(account):
    account_name = account["nama"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name} a {account_descr} from {account_country}"

def check_answer(user_guess , a_follower , b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return  user_guess == "b"
print(logo)
score = 0
game_should_countinue =  True
account_b = random.choice(data)

while game_should_countinue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A:{ format_data(account_a)}")
    print(vs)
    print(f"against b: {format_data(account_b)}")

    guess = input("who has more followers? type 'A' OR 'B'").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)


    if is_correct:
        score += 1
        print(f"youre right! current score{score}")
    else:
        print(f"sorry thats wrong. final score: {score}")
        game_should_countinue = False
