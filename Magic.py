from WordleGraphics import *

# FIVES are all 5-letter words in English... (if you uncomment this)
# from english import FIVES 
# ... or the 4 example words in Latin (comment this out to use english)
from latin import FIVES
# They are capitalized.

def row_word(n):
    return ""

def word_row(n, word):
    return

def col_word(n):
    return ""

def row_color(n, c):
    return

def col_color(n, c):
    return

def enter_action():
    return       
    
gw = WordleGWindow()
gw.add_enter_listener(enter_action)