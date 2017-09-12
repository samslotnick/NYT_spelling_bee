#==============================================================================
# because there are fewer words that contain every letter in a randomly generated
# list of letters than I was anticipating, let's try it this way:
#==============================================================================
import random
from random import randint
#==============================================================================
# Generate words.txt from wordlist.txt
#==============================================================================
#word_file = open("wordlist.txt","r", encoding='utf-8')
#for line in word_file:
#    if len(line.rstrip()) >= 5 and line.rstrip().isalpha():
#        words = open("words.txt","a", encoding='utf-8')
#        words.write(line)

game_possibilities = []
word_file = open("words.txt","r", encoding='utf-8')
#==============================================================================
# find words that contain 7 unique letters, adding them to game_possibilities list
#==============================================================================
for word in word_file:
    if len(set(word.strip())) == 7:
        game_possibilities.append(word.rstrip())
word_file.close()
#print(game_possibilities)
create = False
while create == False:
    possible_pts = 0
#==============================================================================
#     Choose lettter set from game_possibilities list
#==============================================================================
    game_letters = set(random.choice(game_possibilities))
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for letter in game_letters:
        if letter in alphabet:
            alphabet.remove(letter)
#    print(alphabet)
    game_words = []
#==============================================================================
#     Choose letter for centre of board, required in each answer
#==============================================================================
    obl_letter = random.choice(list(game_letters))
    word_file = open("words.txt","r", encoding='utf-8')
    for line in word_file:
        line = line.strip()
        line = list(line)
        if any(l in alphabet for l in line) == False and obl_letter in line:
            line = ''.join(line)
            game_words.append(line)
#==============================================================================
#    Choose game_letters only if they can be combined to create between 70 and 150
# words of 5+ letters
#==============================================================================
    if len(game_words) >= 70 and len(game_words) < 150:
        create = True
#==============================================================================
# Calculate possible points
#==============================================================================
#print(game_words)
#print("no. of game words: " + str(len(game_words)))
three_pts = []
for w in game_words:
    if len(set(w)) == 7:
        three_pts.append(w)
        possible_pts += 3
    else:
        possible_pts += 1
#==============================================================================
# Make player benchmarks a function of how common game's words are and how many
# there are.
#==============================================================================
common_amt = 0
google_10000 = open("google_10000.txt","r", encoding='utf-8')
for com in google_10000:
    for words in game_words:
        if com.rstrip() == words:
            common_amt += 1
#print("common word: " + str(common_amt))
good = int( common_amt ** 0.5 + possible_pts ** 0.5 + (possible_pts - len(game_words)))
#print("good: " + str(good))
excellent = int(good + (good / 2))
#print("excellent: " + str(excellent))
genius = excellent + common_amt
board = list(game_letters)
board.remove(obl_letter)
h = board[0].upper()
e = board[1].upper()
x = board[2].upper()
a = obl_letter.upper()
g = board[3].upper()
o = board[4].upper()
n = board[5].upper()
print("""  
-----------RULES------------
- EACH WORD MUST BE 5 OR MORE
LETTERS
- EACH WORD MUST CONTAIN THE 
LETTER IN CENTRE OF THE BOARD
- A LETTER CAN BE USED MORE
THAN ONCE
- ALL WORDS ARE WORTH 1PT.
EXCEPT ONES USING EVERY 
LETTER, WHICH ARE WORTH 3PTS.       
-----------POINTS-----------

  GOOD: """ + str(good) + """ ||| EXCELLENT: """ + str(excellent) + """
  ||||||| GENIUS: """ + str(genius) + """ |||||||
            _____
           /     \\
          /       \\
    ,----(    """+h+ """    )----.
   /      \\       /      \\
  /        \\_____/        \\
  \\    """+g+"""   /     \\   """+e+"""    /
   \\      /       \\      /
    )----(    """+a+"""    )----(
   /      \\       /      \\
  /        \\_____/        \\
  \\    """+o+"""   /     \\   """+x+"""    /
   \\      /       \\      /
    `----(    """+n+"""    )----'
          \\       /
           \\_____/
 
      """)
pts = 0
print("ENTER ANSWER: ")
guess = False
while guess != "QUIT GAME":
    guess = input()
    if len(guess.rstrip()) >= 5 and guess.rstrip().isalpha():
        if guess.rstrip() in three_pts:
            pts += 3
        elif guess.rstrip() in game_words:
            pts += 1
        else:
            print("NOT A VALID WORD")
    else:
        print("GUESS IS TOO SHORT!")
        