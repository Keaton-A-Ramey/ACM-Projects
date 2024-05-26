import pygame

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