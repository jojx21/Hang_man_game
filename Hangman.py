import random
import requests

class Hangman:
    def __init__ (self,word, a_guess , guesses_left):
        self.word = word
        self.a_guess = a_guess
        self.guesses_left = guesses_left
       
    
class main_game:
    def play(self):
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        WORDS = response.content.splitlines()
        word = random.choice(WORDS)
        self.word = word.decode()
     
        print("Welcome to hangman ")
        games_to_play = int(input("Do you wish to play 1: Yes or 2:No : "))

        if games_to_play ==1:
            games_to_play = True
        else:
            print("GoodBye :( ")
            quit()
            
        while games_to_play == True:
            guesses_left = ""
            turns = len(self.word)
            while turns > 0:
                failed = 0
                for char in self.word:
                    if char in guesses_left:
                        print(char,end=" ")
                    else:
                        print("*", end = "")
                        failed +=1
               

                if failed ==0:
                    print("You won")
                    break
                guess = str(input(" Guess a character: "))
               
                    
                guesses_left += guess

                if guess not in self.word:
                    turns -=1
                    print("wrong")
                    print(f"You have {turns} left")

                if turns == 0:
                    print("You loose")


            

            try:
                games_to_play = int(input("Do you wish to play 1 again: Yes or 2:No : "))
            except:
                print("You must enter an integer")

            if games_to_play == 1 : 
                games_to_play = True

            else:
                games_to_play = False
                print("Thanks for playing! ")
                quit()


s = main_game()
s.play()