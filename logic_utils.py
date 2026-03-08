def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 100  # FIX: Hard now has same range as Normal (was 1, 50) with fewer attempts
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    FIX: Secret is now always an integer (no string conversion).
    This prevents alphabetical comparison bugs.
    FIX: Hint messages corrected (were reversed) - Copilot helped debug by tracing game logic
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    #FIX : Hints are logically correct (reversed the old logic)
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        #FIX: Removed +1 to properly reward fast guesses (Copilot helped in tracing the score logic)
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    #FIX: Removed even/odd bonus inconsistency for "Too High" guess - now consistent -5 penalty for incorrect guess
    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
