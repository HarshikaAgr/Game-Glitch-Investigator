from logic_utils import check_guess, get_range_for_difficulty, parse_guess, update_score

# =====================================================
# Original Tests (FIXED to check full tuple)
# =====================================================

def test_winning_guess():
    """If the secret is 50 and guess is 50, it should be a win"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    """If secret is 50 and guess is 60, hint should be "Too High" """
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "HIGHER" in message

def test_guess_too_low():
    """If secret is 50 and guess is 40, hint should be "Too Low" """
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "LOWER" in message

# =====================================================
# BUG #1 FIX: Hints Backwards on Even Attempts
# =====================================================
# Test that with INTEGER secret, comparison always works correctly
# (Previously failed with string comparison causing backwards hints)

def test_bug1_small_guess_against_large_secret():
    """Bug #1: Secret is 50, guess is 6 should say 'Too Low' (not 'Too High')"""
    outcome, message = check_guess(6, 50)
    assert outcome == "Too Low", f"Expected 'Too Low' but got '{outcome}'"
    assert "LOWER" in message

def test_bug1_single_digit_vs_double_digit():
    """Bug #1: Verify numeric comparison works (not alphabetical)"""
    # Alphabetically: "9" > "10" (9 comes after 1)
    # Numerically: 9 < 10 (correct)
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low", "Should use numeric comparison, not alphabetical"

def test_bug1_numeric_comparison_not_alphabetical():
    """Bug #1: Verify 6 < 50 is correctly evaluated as Too Low"""
    outcome, message = check_guess(6, 50)
    assert outcome == "Too Low"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

# =====================================================
# BUG #2 FIX: Hard Mode Difficulty Range
# =====================================================
# Hard difficulty should have SAME range as Normal (1-100), not smaller (1-50)

def test_bug2_hard_difficulty_range():
    """Bug #2: Hard mode should have range 1-100 (not 1-50)"""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1, f"Hard low should be 1, got {low}"
    assert high == 100, f"Hard high should be 100, got {high}"

def test_bug2_easy_difficulty_range():
    """Easy mode should have range 1-20"""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_bug2_normal_difficulty_range():
    """Normal mode should have range 1-100"""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_bug2_hard_equals_normal_difficulty():
    """Bug #2: Hard should NOT be easier than Normal"""
    hard_low, hard_high = get_range_for_difficulty("Hard")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    assert hard_high >= normal_high, "Hard range should be at least as large as Normal"

# =====================================================
# BUG #3 FIX: Winning Fast Gives Fewer Points
# =====================================================
# Winning on attempt 1 should give MORE points than attempt 2
# Formula: points = 100 - 10 * attempt_number (removed the +1)

def test_bug3_fast_win_more_points_than_slow_win():
    """Bug #3: Winning on attempt 1 should give more points than attempt 2"""
    score1 = update_score(0, "Win", 1)  # Win on attempt 1
    score2 = update_score(0, "Win", 2)  # Win on attempt 2
    assert score1 > score2, f"Attempt 1 points ({score1}) should be > attempt 2 points ({score2})"

def test_bug3_win_on_attempt_1():
    """Bug #3: Winning on first attempt should give 90 points"""
    # Formula: 100 - 10 * 1 = 90
    score = update_score(0, "Win", 1)
    assert score == 90, f"Win on attempt 1 should give 90 points, got {score}"

def test_bug3_win_on_attempt_2():
    """Bug #3: Winning on second attempt should give 80 points"""
    # Formula: 100 - 10 * 2 = 80
    score = update_score(0, "Win", 2)
    assert score == 80, f"Win on attempt 2 should give 80 points, got {score}"

def test_bug3_win_on_attempt_3():
    """Bug #3: Winning on third attempt should give 70 points"""
    # Formula: 100 - 10 * 3 = 70
    score = update_score(0, "Win", 3)
    assert score == 70, f"Win on attempt 3 should give 70 points, got {score}"

def test_bug3_minimum_points_is_10():
    """Minimum winning points should be 10 (not negative)"""
    # Even on attempt 10+, minimum is 10
    score = update_score(0, "Win", 15)
    assert score == 10, f"Minimum points should be 10, got {score}"
