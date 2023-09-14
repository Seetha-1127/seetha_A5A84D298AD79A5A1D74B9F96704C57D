#Defining the base class for Player
class Player:
  def play(self):
    print("The player is playing cricket.")

#Defining the derived class for Batman
class Batsman(Player):
   def play(self):
     print("The batsman is batting.")

#Defining the derived class for Bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

#Creating object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#Call the play() method for each object
batsman.play()
bowler.play()