import random
from random import randint
gen = 7
vow_samp = 2
#print("vow: " + str(vow_samp))
gen -= 2
#print("gen: " + str(gen))
com_samp = random.randint(2, (gen-1))
#print("com: " + str(com_samp))
gen -= com_samp
#print("gen: " + str(gen))
uncom_samp = random.randint(1, gen)
#print("uncom: " + str(uncom_samp))
gen -= uncom_samp
#print("gen: " + str(gen))
if gen > 0:
    rare_samp = gen
#    print(gen)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']

vowels = ['a','e','i','o','u']
com_cons = ['c','d','f','g','h','l','m','n','r','s','t']
uncom_cons = ['b','k','p','v','y']
rare_cons = ['z','x','j']
letter_space = random.sample(list(vowels), vow_samp) + random.sample(list(com_cons), com_samp) + random.sample(list(uncom_cons), uncom_samp) 
if len(letter_space) < 7:
    letter_space.append(random.sample(list(rare_cons), 7 - len(letter_space)))
#print(letter_space)
key_letter = random.choice(letter_space)
for x in alphabet:
    for y in letter_space:
        if y in alphabet:
            alphabet.remove(y)
points = 0
game_words = []
print("   " + letter_space[0].upper())
print(letter_space[1].upper() + "     " + letter_space[2].upper())
print("   " + letter_space[3].upper())
print(" " + letter_space[4].upper() + "    " + letter_space[5].upper())
print("    " + letter_space[6].upper())
readable_words = []
word_file = open("words.txt","r", encoding='utf-8')
for line in word_file:
    line = line.strip()
    line = list(line)
    if any(l in alphabet for l in line) == False and key_letter in line:
        game_words.append(line)
        readable_words.append(''.join(line))
#print(len(game_words))
print(readable_words)
print(len(readable_words))          
if len(readable_words) >= 25:
    guess = input("enter your words: ")
#    while guess != "quit game":
    for w in readable_words:
        if w == guess:
            print("correct")
            points += 1
        
