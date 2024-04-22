# Score categories.
YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    """
    Calculate the score of a roll of dice in the game of Yacht.

    The game of Yacht is a dice game similar to Poker Dice, Generala and others.
    The task is to score a throw according to these rules.

    Args:
        dice (list): A list of five integers representing the dice roll.
        category (str or int): The category in which the dice roll is to be scored.

    Returns:
        int: The score of the dice roll in the given category.

    Examples:
        >>> score([2, 3, 4, 5, 6], BIG_STRAIGHT)
        30
        >>> score([1, 1, 1, 1, 1], YACHT)
        50
    """
    # Check for categories that are scored by the number of dice showing the category number
    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return dice.count(category) * category
    # Check for full house
    elif category == FULL_HOUSE:
        if len(set(dice)) == 2 and dice.count(dice[0]) in [2, 3]:
            return sum(dice)
    # Check for four of a kind
    elif category == FOUR_OF_A_KIND:
        if dice[0] == dice[3] or dice[1] == dice[4]:
            return dice[1] * 4
    # Check for little straight
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]: 
            return 30
    # Check for big straight
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
    # Check for yacht
    elif category == YACHT:
        if all(num == dice[0] for num in dice):
            return 50
    # Check for choice
    elif category == CHOICE:
        return sum(dice)
    # If none of the above conditions are met, the score is 0
    return 0