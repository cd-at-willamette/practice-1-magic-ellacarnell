from WordleGraphics import *

# FIVES are all 5-letter words in English... (if you uncomment this)
from english import FIVES 
# english list of 5 letter words is above
# ... or the 4 example words in Latin (comment this out to use english)
#from latin import FIVES 
#Latin word list is above
# They are capitalized.

def row_word(n):
    s = "" # Start with an empty string
    for i in range(N_COLS): 
        s += gw.get_square_letter(n , i)
    return s

def word_row(n, word):
    for i in range(N_COLS):
        gw.set_square_letter(n , i, word[i])

def col_word(n):
    return ""

def row_color(n, c):
    for i in range(N_COLS):
        gw.set_square_color(n , i, c)
   

def col_color(n, c):
    for i in range(N_ROWS):
        gw.set_square_color(i , n, c)
    

def enter_action():
    row = gw.get_current_row()
    word = row_word(row)
    print(word)
    if row == 0: 
        if word in FIVES and word [::-1] in FIVES:
            gw.show_message("+1")
            row_color(row, CORRECT_COLOR)
            gw.set_current_row(row + 1)
            return
        else:
            gw.show_message("Cringe")
            row_color(row, MISSING_COLOR)
            return 
    if row == 1:
        if word [::-1] in FIVES:
            if word in FIVES:
                color = CORRECT_COLOR
            else:
                color = PRESENT_COLOR
            # Check Columns
            if word[0] == gw.get_square_letter(0 , 1) and word[4] == gw.get_square_letter(0 , 3): # You are working on the first word here. The letter is row zero column 1 and the letter in row zero column 4
                #Good case I think
                #code not tested
                row_color(0, CORRECT_COLOR)
                row_color(row, color)
                for i in range (3 , N_ROWS):
                    row_color(i, UNKNOWN_COLOR)
                gw.show_message("+1")
                gw.set_current_row(row + 1)
                return
            else:
                if word [0] != gw.get_square_letter(0,1):
                    col_color(0, MISSING_COLOR)
                if word [4] != gw.get_square_letter(0 , 3):
                    col_color(4, MISSING_COLOR)
                gw.show_message("Yer Cols r cooked!")

                return
        else:
            gw.show_message("Not a word!")
            return
    if row == 2:
        if word in FIVES and word[::-1] == word:
            if word[0] == gw.get_square_letter(0,2) and word[1] == gw.get_square_letter(1,2):
               row_color(0, CORRECT_COLOR)
               if row_word(1) in FIVES:
                   row_color(1, CORRECT_COLOR)
               else:
                   row_color(1, PRESENT_COLOR)
               for i in range(2, N_COLS):
                   row_color(i, CORRECT_COLOR)
               row_color(5, "pink")
               word_row(3, row_word(1)[::-1])
               word_row(4, row_word(0)[::-1])
               gw.show_message("That is a W")
            else:
                col_color(2, MISSING_COLOR)
                gw.show_message("Wrong letters Nerd!")
        else:
            row_color(2, MISSING_COLOR)
            gw.show_message("Not Palindrome")




    return None   
    
gw = WordleGWindow()
gw.add_enter_listener(enter_action)
