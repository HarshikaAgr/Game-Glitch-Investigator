# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

**Bug #1: Hints Are Backwards on Every Other Guess**
When you make your 2nd, 4th, 6th, or 8th guess, the game tells you the opposite direction to go. For example, if the secret number is 50 and you guess 6, the game says "Go HIGHER!" when you should actually go lower. This makes it nearly impossible to play correctly after your first guess because the hints are completely wrong. The game is giving you bad directions instead of helping with the hints.

**Bug #2: "Hard" Mode is Easier Than "Normal" Mode**
The "Hard" difficulty setting makes you guess a number between 1-50 with 5 attempts allowed. The "Normal" difficulty makes you guess between 1-100 with 8 attempts allowed. This is wrong! Hard mode should be harder, not easier. A smaller number range with fewer attempts should not be the "hard" option, it's actually the easiest. Players expect "Hard" to be more challenging, but it's the opposite.

**Bug #3: Winning Fast Actually Gives You Fewer Points**
If you guess the correct number on your first try, you only get 80 points. If you win on your second try, you get 70 points. If you win on your third try, you get 60 points. This is broken logic, you're being punished for winning quickly and in fewer attempts instead of rewarded! Players expect to get more points for winning faster, not fewer points.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
