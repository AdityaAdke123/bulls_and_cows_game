# UF_Mathematics_Term_Project_bulls_and_cows_game_entropy
![Screenshot (1897)](https://github.com/user-attachments/assets/3a7e012d-57be-437e-99b5-ffd958bd67e4)

🐮 Bulls and Cows Game 🐂
Welcome to the Bulls and Cows Game, a classic code-breaking game brought to life with Python and Streamlit! This repository contains a fun and interactive game where you use logic and deduction to guess a secret 4-digit number.

🎯 About the Game
Bulls and Cows is a logic-based number-guessing game:

A Bull 🐂 means a digit in your guess is in the correct position.
A Cow 🐮 means a digit in your guess is in the secret number but in the wrong position.
Your goal is to correctly guess the 4-digit secret number with unique digits using as few attempts as possible.

🚀 Features
Random Secret Number Generation: The game generates a new 4-digit secret number with unique digits every time.
Interactive UI: Play the game via an interactive interface powered by Streamlit.
Feedback on Every Guess: Get instant feedback with the number of Bulls and Cows.
Game History Tracking: View your previous attempts, including Bulls, Cows, entropy, and remaining valid guesses.
Entropy Visualization: Monitor your progress with a graph that visualizes entropy over time.
Customizable Styles: The app features custom CSS for a sleek look, including a maroon header, yellow sidebar, and a dynamic background image.
Game Controls: Restart the game or reveal the secret number if you're stuck.
🛠 How to Run
Clone this repository:
bash
Copy code
git clone https://github.com/<your-username>/bulls-and-cows-game.git
Navigate to the project directory:
bash
Copy code
cd bulls-and-cows-game
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Run the app:
bash
Copy code
streamlit run app.py
🖥 Screenshots
Main Interface
Showcase the interactive gameplay, including the input field and feedback area.

Entropy Visualization
Display the graph tracking entropy across attempts.

📋 Game Mechanics
Secret Number Generation
A random 4-digit number with unique digits is generated at the start of the game.
Bulls and Cows Calculation
Bulls: Digits that are correct and in the right position.
Cows: Digits that are correct but in the wrong position.
Entropy Calculation
Entropy helps measure uncertainty in the remaining valid guesses, providing insights into how close you are to guessing the secret number.
Valid Guesses Filtering
After each guess, the game updates the list of valid guesses based on the Bulls and Cows feedback.
🧑‍💻 Customization
You can modify the game to:

Change the number of digits in the secret number.
Implement different themes using the add_custom_styles function.
Extend functionality, like adding a timer or scoring system.
🌟 Contributing
Feel free to contribute to this project! Fork the repository, create a feature branch, and submit a pull request.

Enjoy breaking codes and solving the mystery! 🎉
