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

**AI Tool Used:** GitHub Copilot (Agent mode in VS Code)

**Correct Suggestion:**
Copilot suggested using a `game_counter` that increments every time you click "New Game". This counter gets added to the text input field's key, which forces Streamlit to create a completely new input widget instead of reusing the old one. I verified this was correct by clicking "New Game" and seeing the input box completely empty instead of showing the old guess. This fixed the state-caching bug.

**Incorrect/Misleading Suggestion:**
Copilot initially told me the hints were working correctly in the code, but when I tested the game, I found they were backwards on certain difficulty levels. The hints looked correct in the code (Go LOWER when guess > secret), but the suggestion missed that the real issue was sometimes the hints seemed inconsistent. I verified by playing multiple games and checking the debug panel to see what the secret number was compared to my guess.

---

## 3. Debugging and testing your fixes

**How I knew bugs were fixed:**
I tested each bug manually by playing the game in my browser. For each fix, I would click "New Game" and then try different guesses to see if the behavior changed.

**Test 1 - Hints Bug:**
I guessed a number, checked the debug info to see what the secret was, then tested if the hint told me the correct direction. Before the fix, the hints were backwards. After the fix, the hints always matched the correct direction (if I'm too high, it said "Go LOWER").

**Test 2 - Scoring Bug:**
I played a full game and won in 5 attempts. I checked the final score shown on the screen and compared it to what it should be (started at 0, lost 5 points twice for wrong guesses, then gained 50 points for winning on attempt 5 = 40 points). Before the fix, the score showed 30. After the fix, it showed 40. This proved the attempts counter was correct now.

**Test 3 - New Game Reset:**
I clicked "New Game" and checked if the input box was empty and the score reset to 0. Before the fix, the old guess was still in the input box. After the fix, everything was blank and ready for a new game.

**AI Help with Testing:**
Copilot helped me understand what to look for by explaining that I should check the debug info panel and compare the secret number with my guess. It also helped me calculate what the correct score should be.

---

## 4. What did you learn about Streamlit and state?
Streamlit reruns the whole script every time you click something. Without session_state, `random.randint()` runs again and creates a new secret number each time.

**Streamlit reruns and session state explained:**
Imagine Streamlit reads a recipe from top to bottom every time you interact with the app and the Session state is like a sticky note that remembers all the important things between the reads. If you save the secret to this sticky note, it stays the same even after reruns.

---

## 5. Looking ahead: your developer habits

**Habit to reuse:**
Always add a debug info panel during development. Seeing the actual values (secret, score, attempts) made debugging so much faster than guessing.

**What I'd do differently with AI next time:**
Don't trust the AI code is correct just because it looks right. Always test it myself manually to see if it actually solves the problem.

**How this changed my thinking about AI code:**
AI-generated code is a starting point, not the final answer. It needs careful testing and human verification to catch hidden bugs.
