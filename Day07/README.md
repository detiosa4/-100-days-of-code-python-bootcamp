# 🧩 Day 7: Hangman Game | 100 Days of Code (Python Bootcamp)

This repository contains my implementation of the classic **Hangman game** as part of **Day 7** from Angela Yu's [100 Days of Code: The Complete Python Bootcamp].

---

## 📅 What I Learned

- How to use **lists**, **loops**, and **conditional logic** to track game state
- How to **structure code across multiple files** for better organization
- How to **import variables** (like word lists and ASCII art) from external modules
- How to track user guesses, handle wrong inputs, and update the game visually with **ASCII art**

---

## 🚀 Final Project Overview

### 🕹 Features:
- The game randomly selects a word from a word list
- User is prompted to guess one letter at a time
- Tracks and displays correct/incorrect guesses
- Decreases lives with each incorrect guess and shows a corresponding hangman stage using ASCII art
- Ends the game with a win/loss message depending on the number of remaining lives

---

## 🛠 How I Structured the Project

**Files:**

- `hangman.py`: Main game logic and loop
- `hangman_words.py`: Contains the list of possible words
- `hangman_art.py`: Contains the game logo and the ASCII art for each life stage

---

## 💡 Key Takeaways

- Separating logic and assets (like the word list and ASCII art) into different modules made the code cleaner and easier to manage.
- Using lists to represent the word's progress (`_ _ _ a _ _`) taught me how to dynamically update output based on user input.
- This was my first time using **multi-file imports** in Python, which made the project feel like a real-world application.

---

## ✅ Status

✔ Project completed as part of Day 7  
✔ Fully functional  
✔ Refactored for clarity and modularity

---

## 📁 Next Steps

- [ ] Add replay functionality  
- [ ] Prevent repeated wrong guesses from deducting multiple lives  
- [ ] Expand word list by category or difficulty  
