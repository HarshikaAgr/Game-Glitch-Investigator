"""
Specific test cases for the 3 bugs fixed:
Bug 1: Hints Are Backwards on Every Other Guess
Bug 2: Hard Mode is Easier Than Normal Mode
Bug 3: Winning Fast Actually Gives You Fewer Points
"""
#Co-pilot helped in identifying the specific logic issues 
#Helped in creating targeted test cases for each bug. 
#The tests verify that the fixes are working as intended and prevent regressions.

import pytest
from logic_utils import check_guess, get_range_for_difficulty, update_score


#BUG 1 TEST: Verify hint directions are ALWAYS correct
#(No more string comparison on even attempts)

def test_bug1_guess_too_high_correct_hint():
    """When guess > secret, hint should be 'Too High' (regardless of attempt number)"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "HIGHER" in message


def test_bug1_guess_too_low_correct_hint():
    """When guess < secret, hint should be 'Too Low' (regardless of attempt number)"""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "LOWER" in message


def test_bug1_small_guess_vs_large_secret():
    """Single digit guess (6) vs larger secret (50) should give 'Too Low' hint"""
    outcome, message = check_guess(6, 50)
    assert outcome == "Too Low", "6 should be too low when secret is 50"


#BUG 2 TEST: Verify Hard mode has harder difficulty than Normal

def test_bug2_hard_range_equals_normal_range():
    """Hard difficulty should have the same range as Normal (1-100), not smaller"""
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    
    assert normal_high == hard_high == 100, "Hard and Normal should both go up to 100"
    assert hard_low == 1 and normal_low == 1


def test_bug2_hard_is_not_easier_than_normal():
    """Hard should NOT be easier than Normal"""
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")
    
    easy_range = easy_high - easy_low
    normal_range = normal_high - normal_low
    hard_range = hard_high - hard_low
    
    assert hard_range >= normal_range, "Hard range should not be smaller than Normal"


#BUG 3 TEST: Verify winning quickly gives MORE points

def test_bug3_first_win_better_points_than_second():
    """Winning on attempt 1 should give MORE points than winning on attempt 2"""
    points_attempt_1 = update_score(0, "Win", 1)
    points_attempt_2 = update_score(0, "Win", 2)
    
    assert points_attempt_1 > points_attempt_2, "First win should have more points than second"


def test_bug3_fast_win_rewards():
    """Verify points decrease as attempts increase (reward for speed)"""
    score_0 = 0
    
    points_1 = update_score(score_0, "Win", 1)
    points_2 = update_score(score_0, "Win", 2)
    points_3 = update_score(score_0, "Win", 3)
    points_4 = update_score(score_0, "Win", 4)
    
    # Each successive attempt should give fewer points
    assert points_1 > points_2 > points_3 > points_4, "Points should decrease per attempt"
    
    # First guess should give high points (90)
    assert points_1 == 90
    
    # Second guess should give 80 points
    assert points_2 == 80


def test_bug3_first_guess_minimum_points():
    """Verify first guess doesn't get penalized, but gets max points"""
    points = update_score(0, "Win", 1)
    # Should be 100 - 10*1 = 90 (not 80 which was the buggy version: 100 - 10*(1+1))
    assert points == 90, f"First win should be 90 points, got {points}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
