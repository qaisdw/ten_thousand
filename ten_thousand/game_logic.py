import random


class GameLogic:

    def __init__(self):
        pass

    def roll_dice(number=6):
      '''
      return the result of throwing number of dices
      the nubmer of dices based on the input number  
      '''
      if number < 1 or number > 6:
            raise ValueError("Number of dice must be between 1 and 6.")
      if number:
        return tuple(random.randint(1, 6) for _ in range(number))
      

    @staticmethod
    def calculate_score(roll):
        """
        Calculates the score based on the given roll.
    
        Args:
            roll (tuple): A tuple representing the dice roll.
    
        Returns:
            int: The calculated score.
    
        """
        score = 0
        counts = [roll.count(i) for i in range(1, 7)]
    
        if counts == [1, 1, 1, 1, 1, 1]:
            # Check for a straight (1, 2, 3, 4, 5, 6)
            score = 1500
            return score
    
        if counts.count(2) == 3:
            # Check for three pairs
            score += 1500
            return score
    
        if counts[0] <= 2:
            # Check for individual 1s
            score += counts[0] * 100
    
        if counts[4] <= 2:
            # Check for individual 5s
            score += counts[4] * 50
    
        if 3 in counts:
            # Check for three of a kind
            if counts.count(3) == 2:
                # Two sets of three of a kind
                location = counts.index(3) + 1
                location2 = counts[location::1].index(3) + location + 1
                if location == 1:
                    score += location * 1000
                else:
                    score += location * 100
                score += location2 * 100
            else:
                location = counts.index(3) + 1
                if location == 1:
                    score += location * 1000
                else:
                    score += location * 100
    
        elif 4 in counts or 5 in counts or 6 in counts:
            # Check for four, five, or six of a kind
            maxx = max(counts)
            a = 0
            location = counts.index(maxx) + 1
            if location == 1:
                for i in range(3, maxx + 1):
                    a += 1000
            else:
                for i in range(3, maxx + 1):
                    a += (location * 100)
            score += a
    
        return score
    
    
    def string_to_tuple(string):
      """
    Converts a string of digits to a tuple of integers.

    Args:
        string (str): The string of digits.

    Returns:
        tuple: A tuple of integers converted from the string.

      """
      string = string
      tuple_value = tuple(int(digit) for digit in string)
      return tuple_value


    @classmethod
    def startGame(cls):
        """
        Starts the Ten Thousand game.

        The method prompts the user to play the game or decline. If the user chooses to play,
        it initializes the game variables and starts the game loop. The loop allows the player
        to roll dice, keep dice, bank points, and continue playing until they decide to quit.

        Returns:
            None

        Raises:
            None
        """
        print("Welcome to Ten Thousand\n(y)es to play or (n)o to decline")
        userInputs = input('> ')
        while userInputs != 'q':
            if userInputs.strip().lower() == 'y':
                roun = 1
                total = 0
                remaining = 6
                score2 = 0

                while True:
                    score1 = 0
                    if remaining == 6:
                        print(f"Starting round {roun}\nRolling 6 dice...")
                        dice = cls.roll_dice()
                        dices = "*** "
                        for i in dice:
                            dices += str(i) + " "
                        dices += "***"
                        print(f"{dices}\nEnter dice to keep, or (q)uit:")

                    userInputs = input('> ')

                    if userInputs.strip().lower() == 'q':
                        print(f"Thanks for playing. You earned {total} points")
                        break

                    if userInputs.strip().lower() == 'b' and score2 == 0:
                        print('\nYou have no points to bank \nEnter dice to Play or (q)uit\n')
                        continue

                    if userInputs.strip().lower() == "r" and remaining == 6:
                        print("\nYou have to select a dice to re-roll first or (q)uit\n")
                        continue

                    if userInputs.strip().lower() == "r" and remaining != 6:
                        print(f"Starting round {roun}\nRolling {remaining} dice...")
                        dice = cls.roll_dice(remaining)
                        dices = "*** "
                        for i in dice:
                            dices += str(i) + " "
                        dices += "***"
                        print(f"{dices}\nEnter dice to keep, or (q)uit:")
                        continue

                    if userInputs.strip().lower() == 'b' and remaining != 6:
                        print(f"\nYou banked {score2} points in round {roun}\nTotal score is {total} points\n")
                        score2 = 0
                        roun += 1
                        remaining = 6
                        continue


                    if userInputs.isdigit():
                        input_1 = cls.string_to_tuple(userInputs.strip())
                        if all(d in dice for d in input_1):
                            score1 = cls.calculate_score(input_1)
                            remaining -= len(input_1)
                            score2 += score1
                            total += score1
                            print(f"You have {score2} unbanked points and {remaining} dice remaining\n(r)oll again, (b)ank your points or (q)uit:")
                            continue
                        else:
                            print("\nInvalid dice selection. Try again.\n")
                    else:
                        print("\nInvalid input. Try again.\n")
            else:
                print("OK. Maybe another time")
                break

    




      
          
    def mock_roller(self):
        rolls = [(3,2,5,4,3,3),(5,2,3,2,1,4)]
        return rolls.pop(0) if rolls else GameLogic.roll_dice(6)


if __name__ == '__main__':


      GameLogic.startGame()
      # x= GameLogic.roll_dice(6)
      # print(x)
      # print(GameLogic.calculate_score(x))
      # print(GameLogic.string_to_tuple('5568 '))
      # print(GameLogic.calculate_score((5,5)))

      # rolls = [(5,6),(6,1),(1,1),(1,2)]
      # play_dice(mock_roller)

        
      

      
      







