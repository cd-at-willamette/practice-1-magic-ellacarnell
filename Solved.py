# N_ROWS is 6 and N_COLS is 5
from WordleGraphics import *

# FIVES are all 5-letter words in English, or the 4 example words in Latin
# They are capitalized.
from latin import FIVES
# from english import FIVES

def row_word(n):
    word = ""
    for i in range(N_COLS):
        word += gw.get_square_letter(n,i)
    return word

def word_row(n, word):
    for i in range(N_COLS):
        gw.set_square_letter(n,i,word[i])

def col_word(n):
    word = ""
    for i in range(gw.get_current_row() + 1):
        word += gw.get_square_letter(i,n)
    return word

def row_color(n, c):
    for i in range(N_COLS):
        gw.set_square_color(n, i, c)

def col_color(n, c): 
    for i in range(N_ROWS):
        gw.set_square_color(i, n, c)

def enter_action():
    row = gw.get_current_row()
    word = row_word(row) 
    color = CORRECT_COLOR
    if row == 0:
        if word not in FIVES or word[::-1] not in FIVES:
            row_color(row, MISSING_COLOR)
            gw.show_message("Either guess or reversal not in dictionary.")
            return
        row_color(row, color)
        gw.set_current_row(1)     
    if row == 1:
        if word not in FIVES and word[::-1] not in FIVES:
            row_color(row, MISSING_COLOR)
            gw.show_message("Neither guess nor reversal in dictionary.")
            return 
        if word[0] != col_word(1)[0] or word[4] != col_word(3)[0]:
            if word[0] != col_word(1)[0]:
                col_color(0, MISSING_COLOR)
            if word[4] != col_word(3)[0]:
                col_color(4, MISSING_COLOR)
            gw.show_message("Guess does not match required columns.")
            return
        if word not in FIVES and word[::-1] in FIVES:
            color = PRESENT_COLOR
            gw.show_message("Accepting as reverse of valid word.")
        row_color(row, color)
        gw.set_current_row(2)   
    if row == 2:
        if word not in FIVES:
            row_color(row, MISSING_COLOR)
            gw.show_message("Word not in dictionary.")
            return
        if word != word[::-1]:
            row_color(row, MISSING_COLOR)
            gw.show_message("Word not palindrome.")
            return 
        if word[:2] != col_word(2)[:2]:
            col_color(2, MISSING_COLOR)
            gw.show_message("Word doesn't match vertical letters.")
            return
        for i in range(2,5):
            row_color(i, color)
        word_row(3, row_word(1)[::-1])
        word_row(4, row_word(0)[::-1]) 
        gw.show_message("Uber slay!")
        gw.set_current_row(N_ROWS)
    
gw = WordleGWindow()
gw.add_enter_listener(enter_action)