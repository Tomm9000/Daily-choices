def start():

  print("\nJe word wakker wat doe je? stap je uit bed Y/N")

  answer = input(">")
  
  if answer == "y":

    Yes()
  elif answer == "n":

    Insert()

  else:

    game_over("Dat is geen optie")

def game_over(reason):

  print("\n" + reason)
  print("Game Over!")

  Opnieuw()

def Opnieuw():
  print("\nWil je opnieuw proberen? (y or n)")
  

  answer = input(">").lower()

  if "y" in answer:
    start()
  else:
    exit()

def Yes():

  print("\nJe bent klaar met douchen ga je eten? Y/N")

  answer = input(">")
  
  if answer == "y":

    Yes2()
  elif answer == "n":

    Insert()

  else:

    game_over("Dat is geen optie")

def start():

  print("\nJe word wakker wat doe je? stap je uit bed Y/N")

  answer = input(">")
  
  if answer == "y":

    insert()
  elif answer == "n":

    Insert()

  else:

    game_over("Dat is geen optie")