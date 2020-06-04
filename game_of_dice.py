'''




'''


import random

coin_side = ['heads', 'tails']
win_count = 0
loose_count = 0

while True:
    rdm_side = random.choice(coin_side)
    usr_sel = input("Guess heads or tails \n"
                    "If you no longer want to play select 'done':")
    if usr_sel == "heads" or usr_sel == "tails" or usr_sel == "done":
        if usr_sel == "done":
            print("Game Over!")
            break
        elif usr_sel == rdm_side:
            print("You Win")
            win_count += 1
        elif usr_sel != rdm_side:
            print("You Loose")
            loose_count += 1
    else:
        print("Incorrect Value selected")

print("Game Result: \n"
      "Win Count: ", win_count,
      "\nLoose Count", loose_count)

