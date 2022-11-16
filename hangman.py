import random, os 

while True:
     print("Loading word...")
     
     word_file = "wordlist-german.txt"
     WORDS = open(word_file).read().splitlines()
     word = WORDS[random.randint(0, len(WORDS))]
     
     Health_str = "■"
     Health = Health_str * 15
     Hp = list(Health)

     Elements = list(word.lower())

     print("A word has been chosen. Ready! Steady! GO!")

     number_ltrs = len(word)
     Spaceholder = list("_" * number_ltrs )
 
     print("_ " * number_ltrs)

     while True:
          print("HP: " + "".join([str(i) for i in Hp]))
          
          # Win Check
          if Spaceholder == list(word.lower()):
               os.system('cls')
               print("u succesfully guessed the word!".upper())
               print("Das Wort war: \n> " + str(word))
               break

          # Loose Check
          if Hp == list("□□□□□□□□□□□□□□□"):
               os.system('cls')
               print("unfortunately you lost!")
               print("Das Wort war: \n> " + str(word))
               break
          
          guess = input("guess a letter: \n>").lower()
          os.system('cls')
          if guess in Spaceholder:
                    print("schon erraten!")
          if guess in Elements:
               i = 0
               for char in Elements:
                    if guess == char:
                         Spaceholder.insert(i, guess)
                         Spaceholder.pop(i + 1)
                         
                    i = i + 1
               print("\n" + " ".join([str(i) for i in Spaceholder]))
               
          else:
               print("\n" + " ".join([str(i) for i in Spaceholder]))
               print("Nicht drin!") 
               Hp.pop(0)
               Hp.append("□")

     if input("try again? \n> ").lower() != "yes":
          break