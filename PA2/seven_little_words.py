"""PA2: 7 Little Words Game.

Author Dee A. B. Weikle, Alvin Chao python tranlation
Version 08-01-2018, 10-28-22
"""
import generator
import terminal_ui
import random

CLUE_NUM = 7
MIN_WORD_LENGTH = 2


if __name__ == '__main__':    
    solutions = [] * CLUE_NUM
    clues = [] * CLUE_NUM
    answer = ""
    print("Welcome to Seven Little Words - The Text Version")
    print("What game would you like to play? - default or new?")
    answer = terminal_ui.prompt_for_string("Type \"default\" or \"new\"", 1)
        
    if (answer == "new"):
        solutions = [] * CLUE_NUM
        clues = [] * CLUE_NUM
           
        # fill solutions array from user
        for i in range(0, CLUE_NUM):
            solutions.append(terminal_ui.prompt_for_string(
                "Enter solution word " + str(i + 1), MIN_WORD_LENGTH))
       
        # fill clues array from user
        for i in range(0, CLUE_NUM):
            clues.append(terminal_ui.prompt_for_string("Enter clue " + str(i + 1),
                                                      MIN_WORD_LENGTH))
    else:
        # Using default values
        solutions = ["tofutti", "magnetism", "edifice",
                     "grinder", "groundling", "thesaurus", "bull"]
        clues = ["soy-based frozen treat brand",
                 "charismatic power",
                 "monumental structure",
                 "mincemeat maker",
                 "bottom-dwelling fish",
                 "synonym finder",
                 "upward-trending market"]
    # Create the board and randomize it
    # print(solutions)
    board = generator.word_splicer(solutions)
    random.shuffle(board)
    # print(board)
    print("Now that you have initialized a game, let's see it.\n")
    print(generator.clue_to_string(clues))
    print(generator.board_to_string(board))        
    # play the game
    # for (int currentClue = 0; current_clue < CLUE_NUM; currentClue++) {
    for current_clue in range(0, CLUE_NUM):
        solved = False
        first = int(0)
        second = int(0)   
        while solved is False:
            print(f"Clue {current_clue + 1}: {clues[current_clue]}\n")
            terminal_ui.prompt_n_display_hints(solutions[current_clue])                     
            first = terminal_ui.prompt_for_int("Enter the number of the first slice", CLUE_NUM * 2)
            second = terminal_ui.prompt_for_int("Enter the number of the second slice", CLUE_NUM * 2)
            if (solutions[current_clue] == (board[first - 1] + board[second - 1])):
                solved = True
                board[first - 1] = "-"
                board[second - 1] = "-"
            else:                
                print("Sorry you need to try this clue again.")
            print(generator.board_to_string(board))
        print(f"Congratulations! You solved clue {current_clue + 1}!")       
    print("Congratulations! You solved the puzzle!")
    print(generator.clue_to_string(clues))
    # print()
    print(generator.board_to_string(board))
