import sys

from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        # Check to see if the monster attacks
        if self.monster.attack():
            # If so, tell the player
            print("{} is attacking!".format(self.monster))
            # Check if the player wants to dodge
            if input("Dodge? Y/N").lower() == 'y':
            # If so, see if dodge is successful
                if self.player.dodge():
                    # If it is, move on
                    print("You dodged the attack!")
                else:
                    print("You got hit anyway!")
                    # If its not, remove one player hp.
                    self.player.hit_points -= 1
            else:
                # If player doesn't dodge, minus hp
                print("{} hit you for 1 hp!".format(self.monster))
        else:
            # If the monster doesn't attack, let the player know
            print("{} isn't attacking this turn".format(self.monster))

    def player_turn(self):
        # Let the player attack, rest or quit
        player_choice = input("[A]ttack, [R]est, [Q]uit? ").lower()
        # If player attacks:
        if player_choice == 'a':
            print("You're attacking {}!".format(self.monster))

            # See if attack is successful
            if self.player.attack():
                # See if the monster dodges
                if self.monster.dodge():
                    # If dodged, print that
                    print("{} dodged your attack!".format(self.monster))
                else:
                    # If not dodged, subtract right number of hp from the monster
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                print("You hit {} with your {} !".format(self.monster, self.player.weapon))
            else:
                print("You missed!")

        # If player rests:
        elif player_choice == 'r':
            print("You rested and recovered some hp")
            self.player.rest()
        # If player quits:
        elif player_choice == 'q':
            #quit the game
               sys.exit()
        else:
            # If player chooses anything else, rerun this method
           self.player_turn()

    def cleanup(self):
        # If the monster has no more hp:
        if self.monster.hit_points <= 0:
            # up the player's experience
            self.player.experience += self.monster.experience
            # print a message
            print("You killed {} and received {} xp!".format(self.monster, self.monster.experience))
            # Get a new monster
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            # new line with 20 = signs to make nice breaks in console
            print("\n"+"="*20)
            print(self.player)
            self.monster_turn()
            print("-"*20)
            self.player_turn()
            self.cleanup()
            print("\n" + "=" * 20)


        if self.player.hit_points:
            print("Congratulations, you have defeated all the monsters!")
        elif self.monsters or self.monster:
            print("The monsters defeated you.")
        # Quit the game when over
        sys.exit()

Game()

