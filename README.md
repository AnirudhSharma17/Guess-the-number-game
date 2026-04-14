# Guess-the-number-game
Guess the Number is a simple yet engaging game where the player tries to guess a hidden number between 1 and 100. At the start of the game, the computer randomly selects a secret number (the “jackpot”). The player enters guesses, and the game provides hints after each attempt.
# Guess the Number Game

A simple interactive game built with **Streamlit** where the player tries to guess a hidden number between 1 and 100. The app provides hints after each guess and tracks the number of attempts until the correct answer is found.

---

## Description
At the start of the game, the computer randomly selects a secret number (the “jackpot”).  
The player enters guesses, and the app responds with helpful hints:

- If the guess is **too high**, the app says the number is smaller.  
- If the guess is **too low**, the app says the number is larger.  
- When the guess is correct, the app congratulates the player and shows the total number of attempts.

This project demonstrates how to use **Streamlit widgets** (`st.number_input`, `st.button`) and **session state** to build interactive web apps with Python.

---

##  How to Run

1. Clone or download this repository.  
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate # On macOS/Linux
