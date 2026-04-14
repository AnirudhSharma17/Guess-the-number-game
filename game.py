import random
import streamlit as st

st.title("Guess the Number Game")
st.write("Try to guess the number between 1 and 100!")

# Generate a random number (jackpot)
if "jackpot" not in st.session_state:
    st.session_state.jackpot = random.randint(1, 100)
    st.session_state.attempts = 0

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Button to submit guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess == st.session_state.jackpot:
        st.success(f"🎉 Correct! The number was {st.session_state.jackpot}.")
        st.write(f"You guessed it in {st.session_state.attempts} attempts.")
        # Reset game
        if st.button("Play Again"):
            st.session_state.jackpot = random.randint(1, 100)
            st.session_state.attempts = 0
    elif guess > st.session_state.jackpot:
        st.warning("The number is smaller than your guess.")
    else:
        st.warning("The number is larger than your guess.")
