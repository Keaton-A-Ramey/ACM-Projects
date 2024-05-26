import pygame

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