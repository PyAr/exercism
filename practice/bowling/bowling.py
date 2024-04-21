class BowlingGame:

    def __init__(self):
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError('Invalid roll')
        
        if self.current_roll > 20 or (self.current_roll == 20 and not self.is_last_frame_strike_or_spare()):
            raise Exception('Game already has 10 frames')

        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        score = 0
        roll_index = 0

        for frame in range(10):
            if self.is_strike(roll_index):
                score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self.rolls[roll_index] + self.rolls[roll_index + 1] 
                roll_index += 2
        
        return score

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10
    
    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
    
    def strike_bonus(self, roll_index):
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2]

    def is_last_frame_strike_or_spare(self):
        return self.is_strike(18) or self.is_spare(18)


        pass
