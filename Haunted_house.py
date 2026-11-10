health = 100
Fear_level = 0.0
Clues_found = 0

game_play = input("Do you want to experience a haunted house adventure? (Yes/No): ").strip().lower()

if game_play == "no":
    print("Sorry for not playing.")
else:
    username = input("What is your name? ")
    print(f"{username}, you are an explorer.\nIt is an October night, and you have set your eyes on a particular case.\n"
          "Specifically, a paranormal disappearance of the owners of a Victorian house in a Manor.")
    print("You walk through the rusted gates and take many anxious steps toward the door, not helping that you watched"
          " a horror movie of a similar situation you're in.\nStepping up the deteriorated steps, one breaks under you,"
          " and you hear a chilling laugh.\nOpening the creaky doors, you look behind you wondering if you will ever make it back."
          "\nA sudden movement in front of you occurs, you jerk your head forward.\n*Bang* The door slams shut shaking the rotting interior, and you almost black out from fear.")
    print("\nTHE ADVENTURE HAS BEGUN")
    print("Your objective is to find the way out, find clues to the disappearance, or die trying.")

    staircase_explored = False
    drawer_done = False
    books_done = False
    basement_done = False

    while True:
        menu = ""
        if not staircase_explored:
            menu += "\tA: Go up creaking staircase\n"
        if not (drawer_done and books_done):
            menu += "\tB: Explore the mysterious library to your left\n"
        if not basement_done:
            menu += "\tC: Investigate the flickering light coming from the basement\n"

        if menu == "":
            print("\nThere are no places left to explore.")
            break

        decision1 = input(f"\nWhere do you want to go?\n{menu}Choose a listed option: ").strip().upper()

        if decision1 == "A" and not staircase_explored:
            staircase_explored = True
            health -= 20
            print("The stair collapses under you and it creates a cut across your leg, but you continue. (Health -20)")
            print("You see a locked door, and a dusty mirror. The mirror reads, 'Find what's lost to unlock what's trapped.'")
            Door_Back = input("Do you want to try opening the door (risk losing health), or go back down? (Open/Back): ").strip().lower()
            if Door_Back == "open":
                Fear_level += 25
                print("You hear a shuffling sound inside the room, and sprint back down. (Fear +25)")
            elif Door_Back == "back":
                print("You might have prevented a disaster, or missed out on a great discovery.")
            else:
                print("Invalid choice, you head back downstairs.")
        elif decision1 == "B" and not (drawer_done and books_done):
            library_choices = []
            if not drawer_done:
                library_choices.append("Drawer")
            if not books_done:
                library_choices.append("Books")
            library_choices_str = "/".join(library_choices)
            drawer_books = input(f"The library is covered in cobwebs and there is a pungent smell. You see a gleaming light under a desk. Choose ({library_choices_str}): ").strip().capitalize()
            if drawer_books == "Drawer" and not drawer_done:
                drawer_done = True
                # Simulate 50/50 chance
                print("To check your luck, enter a number between 1 and 2:")
                user_luck = input("Your number: ").strip()
                if user_luck == "1":
                    Clues_found += 1
                    print(f"You find a mysterious clue... A photo of the White House. Clues found: {Clues_found}")
                else:
                    print("You find nothing except dust.")
            elif drawer_books == "Books" and not books_done:
                books_done = True
                Clues_found += 1
                print("You find a large and mysterious book. It reveals that the owners of the house participated in witchcraft."
                      " A page is marked, it speaks of a demon named Arnav. You wonder to yourself, could this be what caused the door to shut and the treacherous smell?"
                      f" Clues found: {Clues_found}")
            else:
                print("You take this knowledge with you and head back to the main room.")
        elif decision1 == "C" and not basement_done:
            print("A damp musty smell fills the air, the light coming from an old lantern is all that allows you to see.")
            crates = input("A stack of crates in a corner falls suddenly. Do you investigate or look for an exit (Invest/Exit)? ").strip().lower()
            if crates == "invest":
                basement_done = True
                # Simulate 1 in 4 chance
                print("To check your luck, enter a number between 1 and 4:")
                user_luck = input("Your number: ").strip()
                if user_luck == "3":
                    Fear_level += 75
                    print("You see ARNAV, and he is eating the children of the homeowners (Fear +75)")
                    if Fear_level >= 75:
                        print("You have died from fear and your body is now food for ARNAV.")
                        break
                else:
                    Clues_found += 1
                    print("You have found a decomposing body of the child (identified as 6 year old Sashya) of the homeowners and find a discontinued article."
                          " You see a familiar face... Donald Trump initiating a satanic bond with the homeowners.\nClues found:", Clues_found)
            elif crates == "exit":
                basement_done = True
                print("You go back into the main entrance, but then the pungent smell gets closer.\n"
                      "and then the child that you were supposed to find, kills you and brings you to the nether world.\n"
                      "Gone, and not even remembered by your friends.")
                break
            else:
                print("That basement choice is unavailable or invalid.")
        else:
            print("That choice is unavailable or invalid.")

    if Clues_found >= 4:
        print("You put the pieces together and go back to the book you found in the library, you take the risk and summon ARNAV to where you are right now.")
        fightorhelp = input("It lunges at you, do you fight back, or try to help it? (F/H): ").strip().upper()
        if fightorhelp == "F":
            print("Are you dumb? What kind of idiot tries to fight a demon? He has cursed you with the rest of your life in the house, with no chance of escape.")
        elif fightorhelp == "H":
            print("It somehow understands you want to help, although skeptical, it cooperates.")
            helporescape = input("You notice that the lock on the door that was locked, is now broken off due to the poor engineering.\n"
                                "You can either have the chance to escape with nothing, or you can continue to help the demon. (E/H): ").strip().upper()
            if helporescape == "E":
                # Simulate 1 in 10 chance
                print("To check your luck, enter a number between 1 and 10:")
                user_luck = input("Your number: ").strip()
                if user_luck == "7":
                    print("You have exited the house, missing the evidence, and you have an extreme mental illness for life.")
                else:
                    print("You got caught by Arnav and died.")
            elif helporescape == "H":
                print("It points to a page in the book, it reads RESURRECTING CHARLIE KIRK.\n"
                      "You read the spell and Charlie Kirk comes back as a ghost.\n"
                      "You become startled, but the ghost leads you to a hidden passage out of the house.\n"
                      "You escape the haunted house with all the evidence, and the case is solved!\n"
                      "Congratulations, you survived the haunted house adventure!")
            else:
                print("Invalid choice. The adventure ends in confusion. You wake up outside, unsure if it was real.")
        else:
            print("Indecision leads to your doom. The house claims another victim.")
    else:
        print("\nYou failed to find enough clues to solve the case. The mysteries of the haunted house remain unsolved, and your story ends here.")

print("GAME OVER.")
