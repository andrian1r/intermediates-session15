# intermediates-session15# 🔥 Higher Lower Game (Python)

## 📖 Overview

This project is a Python version of the popular **Higher Lower Game**.

The player must guess which public figure has more social media followers.

Each correct guess increases the score.  
The game ends when the player makes a wrong guess.

---

## 🎮 How The Game Works

1. Two accounts are randomly selected.
2. Player sees:
   - Name
   - Description
   - Country
3. Player guesses:
   - Type `A` if account A has more followers
   - Type `B` if account B has more followers
4. If correct → score increases.
5. If wrong → game ends and final score is shown.

---

## 🧠 Concepts Used

- Functions
- Dictionaries
- Random module
- While loops
- Conditional statements
- Data comparison
- Game loop logic
- Score tracking system

---

## 📂 Project Structure

```
project/
│
├── main.py
├── game_data.py
└── high_logo.py
```

---

## 💻 Full Code (main.py)

```python
from high_logo import logo, vs
from game_data import data
import random


def format_data(account):
    account_name = account["nama"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False
```

---

## 📄 Example Data Format (game_data.py)

```python
data = [
    {
        "nama": "Instagram",
        "follower_count": 600,
        "description": "Social media platform",
        "country": "United States"
    },
    {
        "nama": "Cristiano Ronaldo",
        "follower_count": 500,
        "description": "Footballer",
        "country": "Portugal"
    }
]
```

---

## 🛠 Requirements

- Python 3.x

---

## 🎯 Learning Purpose

This project helps practice:

- Working with dictionaries
- Handling structured data
- Random selection
- Loop-based game logic
- Clean function structure

---

## 👤 Author

Andrian Wijaya

---

## 📜 License

This project is created for educational purposes.
