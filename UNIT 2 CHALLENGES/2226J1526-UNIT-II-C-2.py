# Define the base class Player
class Player:
  def play(self):
    print("The Player is Playing Cricket.")
    
# Define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The Batsman is Batting.")

# Define the Derived class Bowler
class Bowler(Player):
  def play(self):
    print("The Bowler is Bowling.")

# Create objects of Batsman and Bowler Classes
batsman = Batsman()
bowler = Bowler()

# Call the Play metod for each object
batsman.play()
bowler.play()