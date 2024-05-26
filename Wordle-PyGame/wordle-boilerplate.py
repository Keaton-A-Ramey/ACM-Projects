import pygame
import sys
import random
from words import *
 
pygame.init()
 
# Order of things: 
## Letters, then event, then creating/deleting, checking guess, play again, indicators

# Constants
 
# Window dimensions
WIDTH, HEIGHT = 633, 900
 
# Prepping screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND = pygame.image.load("assets/Starting Tiles.png")
BACKGROUND_RECT = BACKGROUND.get_rect(center=(317, 300))
ICON = pygame.image.load("assets/Icon.png")
 
# Display caption + icon
pygame.display.set_caption("Wordle!")
pygame.display.set_icon(ICON)
 
# Relevant colors
GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"
 
CORRECT_WORD = "coder"
 
# How we will color keyboard below board
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)
 
SCREEN.fill("white")
SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
pygame.display.update()
 
# Space between letters
LETTER_X_SPACING = 85
LETTER_Y_SPACING = 12
LETTER_SIZE = 75
 
# Global variables
 
guesses_count = 0
 
# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[]] * 6
 
current_guess = []
current_guess_string = ""
current_letter_bg_x = 110
 
# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = []
 
# W/L/Draw
game_result = ""
 
class Letter:
    def __init__(self, text, bg_position):
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x+36, self.bg_position[1]+34)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)
 
    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(SCREEN, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(SCREEN, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()
 
    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(SCREEN, "white", self.bg_rect)
        pygame.draw.rect(SCREEN, OUTLINE, self.bg_rect, 3)
        pygame.display.update()
 
# This is for drawing 
class Indicator:
    def __init__(self, x, y, letter):
        # Initializes variables such as color, size, position, and letter.
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_color = OUTLINE
 
    def draw(self):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(SCREEN, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
        SCREEN.blit(self.text_surface, self.text_rect)
        pygame.display.update()
 
# Drawing the indicators on the screen.
indicator_x, indicator_y = 20, 600

for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 60
    indicator_y += 100
    # Moves in the indicators in lower rows
    if i == 0:
        indicator_x = 50
    elif i == 1:
        indicator_x = 105



def check_guess(guess_to_check):
    # Goes through each letter and checks if it should be green, yellow, or grey.
    # We need these
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    # Local var checks if/how game ended
    game_decided = False
    # Going through 5 letters
    for i in range(5):
        # Convert our letter to lowercase
        lowercase_letter = guess_to_check[i].text.lower()
        # If it's in the correct word...
        if lowercase_letter in CORRECT_WORD:
            # If it is in the right spot
            if lowercase_letter == CORRECT_WORD[i]:
                # Set background to be green
                guess_to_check[i].bg_color = GREEN
                
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                # Make font white
                guess_to_check[i].text_color = "white"
                # Keeping it as "W" bc it will be handled later to make it easier
                if not game_decided:
                    game_result = "W"
            else:
                # If it is not in the right spot, but in word
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                # Make it yellow with white font
                guess_to_check[i].text_color = "white"
                # We have not won, but we don't know that we lost
                game_result = ""
                game_decided = True
        # Otherwise blahblah
        else:
            guess_to_check[i].bg_color = GREY
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GREY
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        # Draw the letter
        guess_to_check[i].draw()
        # Update screen
        pygame.display.update()
    
    # Reset for next guess
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110
 
    # If we haven't won and the game_result isn't w, we lose
    if guesses_count == 6 and game_result == "":
        game_result = "L"
 
def play_again():
    # Puts the play again text on the screen.
    pygame.draw.rect(SCREEN, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
    word_was_text = play_again_font.render(f"The word was {CORRECT_WORD}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 650))
    SCREEN.blit(word_was_text, word_was_rect)
    SCREEN.blit(play_again_text, play_again_rect)
    pygame.display.update()
 
def reset():
    # Resets all global variables to their default states.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result
    SCREEN.fill("white")
    SCREEN.blit(BACKGROUND, BACKGROUND_RECT)
    guesses_count = 0
    CORRECT_WORD = random.choice(WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()
 
def create_new_letter():
    # Creates a new letter and adds it to the guess.
    # Our current guess and the x pos of the letter (background)
    global current_guess_string, current_letter_bg_x
    # Add our key that is pressed to our string
    current_guess_string += key_pressed
    # Create Letter with letter, position, setting y according to how many guesses done
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count*100+LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING
    # 2D list of our guess (holds all guesses letter by letter)
    guesses[guesses_count].append(new_letter)
    # Append our new letter to it
    current_guess.append(new_letter)
    # For each guess
    for guess in guesses:
        # For every letter
        for letter in guess:
            # Draw it
            letter.draw()
 
def delete_letter():
    # Deletes the last letter from the guess.
    # Need our current guess and the x pos
    global current_guess_string, current_letter_bg_x
    # Delete last letter on screen (-1 is last element, -2 second to last, etc.)
    guesses[guesses_count][-1].delete()
    # Delete last letter from our guess
    guesses[guesses_count].pop()
    # Gets our string, SLICES our string from 0 to -1 (excludes last letter)
    current_guess_string = current_guess_string[:-1]
    # Removes the last element from our current guesses
    current_guess.pop()
    # Adjust our current x position for future letter
    current_letter_bg_x -= LETTER_X_SPACING
 
while True:
    if game_result != "":
        play_again()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # If we're typing...
        if event.type == pygame.KEYDOWN:
            # If we hit return
            if event.key == pygame.K_RETURN:
                # If the game is over, reset
                if game_result != "":
                    reset()
                # Otherwise see if guess valid and then check
                else:
                    if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                        check_guess(current_guess)
            # If we hit backspace
            elif event.key == pygame.K_BACKSPACE:
                # If there is something to delete, delete
                if len(current_guess_string) > 0:
                    delete_letter()
            # If another key...
            else:
                # Convert to uppercase
                key_pressed = event.unicode.upper()
                # If it's in the alphabet and not nothing (it helps with special chars)
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    # If word can fit the letter, add it
                    if len(current_guess_string) < 5:
                        create_new_letter()