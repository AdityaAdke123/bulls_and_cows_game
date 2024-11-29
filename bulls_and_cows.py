import random
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


# Generate a random 4-digit number with unique digits
def generate_secret_number():
    """
    Generates a random 4-digit number with unique digits.
    This serves as the secret number for the game.
    """
    digits = list(range(10))  # Generate digits 0-9
    random.shuffle(digits)  # Shuffle the digits randomly
    return ''.join(map(str, digits[:4]))  # Select the first 4 digits and convert to a string


# Calculate Bulls and Cows
def calculate_bulls_and_cows(secret, guess):
    """
    Calculates the number of bulls and cows for a given guess.
    Bulls: Correct digit in the correct position.
    Cows: Correct digit but in the wrong position.
    """
    bulls = sum([1 for s, g in zip(secret, guess) if s == g])  # Count digits in the correct position
    cows = sum([1 for g in guess if g in secret]) - bulls  # Count digits in the wrong position
    return bulls, cows


# Calculate entropy of the current state
def calculate_entropy(valid_guesses):
    """
    Calculates the entropy based on the remaining valid guesses.
    Entropy helps measure the uncertainty or randomness in the remaining guesses.
    """
    total = len(valid_guesses)
    if total <= 1:  # Prevent invalid log operations when guesses are exhausted
        return 0, total  # Return entropy as 0 when there are no guesses left
    probs = [1 / total for _ in valid_guesses]  # Equal probability for each guess
    entropy = -sum(p * np.log2(p) for p in probs)  # Shannon entropy formula
    return entropy, total


# Filter valid guesses based on feedback
def filter_valid_guesses(guess, bulls, cows, valid_guesses):
    """
    Filters the list of valid guesses based on the feedback (bulls and cows).
    Only guesses that produce the same bulls and cows when compared with the
    current guess are retained.
    """
    return [
        num for num in valid_guesses
        if calculate_bulls_and_cows(num, guess) == (bulls, cows)
    ]


# Add custom CSS for styling
def add_custom_styles():
    """
    Adds custom CSS for styling the Streamlit app, such as changing colors
    of the header, sidebar, and buttons, and applying a background image.
    """
    st.markdown(
        """
        <style>
        /* Change header background color */
        header[data-testid="stHeader"] {
            background-color: #663300; /* Maroon background */
            color: white; /* Header text in white */
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #ffd11a; /* Yellow background */
            color: black; /* Black text */
        }

        /* Sidebar labels and buttons */
        [data-testid="stSidebar"] label {
            color: black; /* Black text */
            font-weight: bold;
        }

        [data-testid="stSidebar"] button {
            background-color: #000000; /* Black button */
            color: white; /* White text */
            border-radius: 5px;
        }

        /* Fixed background image and transparent main container */
        .main {
            background-image: url("https://cdn6.aptoide.com/imgs/9/6/c/96c1ef777ce2b1eb2e435f35cc139742_fgraphic.png");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .block-container {
            background: rgba(0, 0, 0, 0.6); /* Transparent container */
            padding: 2rem;
            border-radius: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# Streamlit UI
def main():
    # Apply custom styles
    add_custom_styles()

    # Title
    st.title("🐮 Bulls and Cows Game 🐂")

    # Sidebar
    st.sidebar.title("Game Controls")

    # Initialize game state
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = generate_secret_number()  # Generate a new secret number
        st.session_state.valid_guesses = [
            str(i).zfill(4) for i in range(10000) if len(set(str(i).zfill(4))) == 4
        ]  # Generate all possible guesses with unique digits
        st.session_state.history = []  # Store the history of attempts

    # Input and feedback
    guess = st.sidebar.text_input("Enter your 4-digit guess:", max_chars=4)
    if st.sidebar.button("Submit Guess"):
        # Validate the input (must be 4 unique digits)
        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == len(guess):
            secret = st.session_state.secret_number
            bulls, cows = calculate_bulls_and_cows(secret, guess)  # Calculate feedback

            # Update valid guesses and calculate entropy
            st.session_state.valid_guesses = filter_valid_guesses(
                guess, bulls, cows, st.session_state.valid_guesses
            )
            entropy, total = calculate_entropy(st.session_state.valid_guesses)
            st.session_state.history.append((guess, bulls, cows, entropy, total))  # Log the attempt

            # Check if the game is won
            if bulls == 4:
                st.markdown(
                    f"""
                    <div style="text-align: center; background-color: black; color: white; padding: 20px;">
                        <h1>🎉 Congratulations!</h1>
                        <h2>You guessed the number!</h2>
                        <h3>The secret number was: <b>{secret}</b></h3>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    # Restart game logic
    if st.sidebar.button("Restart Game"):
        st.session_state.clear()  # Clear all session state
        st.experimental_rerun()  # Refresh the app entirely

    # Display game history
    st.header("📜 Game History")
    if st.session_state.history:
        for i, (g, b, c, e, t) in enumerate(st.session_state.history, 1):
            st.write(
                f"**Attempt {i}**: Guess: `{g}`, Bulls: {'🐂' * b}, Cows: {'🐮' * c}, Entropy: {e:.2f}, Valid Guesses: {t}"
            )


    # Reveal the correct number
    with st.expander("🔍 Reveal the Correct Number"):
        st.info(f"The secret number is: `{st.session_state.secret_number}`")

    # Display entropy graph
    st.header("📊 Entropy Visualization")

    if st.session_state.history:
        entropy_values = [h[3] for h in st.session_state.history]
        fig, ax = plt.subplots()

        # Set background color to green
        fig.patch.set_facecolor('white')  # Figure background
        ax.set_facecolor('green')  # Axes background

        # Plot entropy values
        ax.plot(range(1, len(entropy_values) + 1), entropy_values, marker='o', color='white')
        ax.set_title("Entropy Over Time", color='green')
        ax.set_xlabel("Attempts", color='green')
        ax.set_ylabel("Entropy", color='green')

        # Grid and tick visibility adjustments
        plt.grid(True, linestyle="--", alpha=0.7)
        ax.tick_params(axis='x', colors='green')
        ax.tick_params(axis='y', colors='green')

        st.pyplot(fig)


if __name__ == "__main__":
    main()
