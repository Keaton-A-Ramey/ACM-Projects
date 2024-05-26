import pygame

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