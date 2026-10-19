# Q8. Create a class Player with:
# • a class variable player_count
# • instance variables name and level
# Track how many players were created.

class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

        Player.player_count+=1


player1 = Player("John", 45)
player2 = Player("Robin", 32)
player3 = Player("Juwel", 20)

print(f"{player1.name} has {player1.level} level.")
print(f"{player2.name} has {player2.level} level.")
print(f"{player3.name} has {player3.level} level.")

print(f"Total player count {Player.player_count}")