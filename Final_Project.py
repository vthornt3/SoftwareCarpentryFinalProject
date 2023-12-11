import pygame
import sys
# Initialize Pygame
pygame.init()
# Screen dimensions and setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokémon: A New Age")
# Load background images
title_page_image = pygame.image.load('TitlePage.png')
title_page_image = pygame.transform.scale(title_page_image, (screen_width, screen_height))
name_prompt_image = pygame.image.load('Name_Prompt.jpg')
name_prompt_image = pygame.transform.scale(name_prompt_image, (screen_width, screen_height))
Route1_image = pygame.image.load("Route1.gif")
Route1_image = pygame.transform.scale(Route1_image, (screen_width, screen_height))
# Load images for boy and girl selection
boy_image = pygame.image.load('Red_Image.webp')
girl_image = pygame.image.load('Dawn_Image.webp')
boy_image = pygame.transform.scale(boy_image, (100, 100))  # Adjust size as needed
girl_image = pygame.transform.scale(girl_image, (100, 100))  # Adjust size as needed
# Load the "Police_Station.png" image
police_station_image = pygame.image.load('Police_Station.png')
police_station_image = pygame.transform.scale(police_station_image, (screen_width, screen_height))
# Load the "Red_Bedroom.png" image
red_bedroom_image = pygame.image.load('Red_Bedroom.png')
red_bedroom_image = pygame.transform.scale(red_bedroom_image, (screen_width, screen_height))
# Load the "Red_LivingRoom.jpg" image
red_livingroom_image = pygame.image.load('Red_LivingRoom1.jpg')
red_livingroom_image = pygame.transform.scale(red_livingroom_image, (screen_width, screen_height))
# Load new images for the battle sequence
battle_vs_villain_image = pygame.image.load('Battle1VSVillain.webp')
battle_vs_villain_image = pygame.transform.scale(battle_vs_villain_image, (screen_width, screen_height))
riolu_battle_image = pygame.image.load('RioluVillainBattle1.png')
riolu_battle_image = pygame.transform.scale(riolu_battle_image, (screen_width, screen_height))
# Load the "Villain_Image1.jpg" image
villain_image1 = pygame.image.load('Villain_Image1.jpg')
villain_image1 = pygame.transform.scale(villain_image1, (screen_width, screen_height))
# Load the "Going_Back_Home.png" image
going_back_home_image = pygame.image.load('Going_Back_Home.png')
going_back_home_image = pygame.transform.scale(going_back_home_image, (screen_width, screen_height))
# Load the "Choice3Image.png" image
choice3_image = pygame.image.load('Choice3Image.png')
choice3_image = pygame.transform.scale(choice3_image, (screen_width, screen_height))
Riolu_Battle1_image = pygame.image.load("RioluVillainBattle1.png")
Riolu_Battle1_image = pygame.transform.scale(Riolu_Battle1_image, (screen_width, screen_height))
riolu_pokemon_battle_image = pygame.image.load("Riolu_Pokemon_Battle.png")
riolu_pokemon_battle_image = pygame.transform.scale(riolu_pokemon_battle_image, (screen_width, screen_height))
riolu_trainer_battle_image = pygame.image.load("RioluBattleTrainer1.png")
riolu_trainer_battle_image = pygame.transform.scale(riolu_trainer_battle_image, (screen_width, screen_height))
# Load battle images for Gible and Lapras
gible_battle_images = [pygame.image.load('Gible_Battle1.png'), pygame.image.load('Gible_Battle1END.png'),
                       pygame.image.load('Gible_Battle2.png'), pygame.image.load('Gible_Battle2END.png')]
lapras_battle_images = [pygame.image.load('Lapras_Battle_1.png'), pygame.image.load('Lapras_Battle_1END.png'),
                        pygame.image.load('Lapras_Battle_2.png'), pygame.image.load('Lapras_Battle_2END.png')]
tournament_image_riolu = pygame.image.load("Tournament_Image_Riolu.png")
tournament_image_riolu = pygame.transform.scale(tournament_image_riolu, (screen_width, screen_height))
# Load tournament battle images
riolu_tournament1_image = pygame.image.load("RioluTournament1.png")
riolu_tournament1_image = pygame.transform.scale(riolu_tournament1_image, (screen_width, screen_height))
riolu_tournament1_end_image = pygame.image.load("RioluTournament1End.png")
riolu_tournament1_end_image = pygame.transform.scale(riolu_tournament1_end_image, (screen_width, screen_height))
riolu_tournament_final_image = pygame.image.load("RioluTournamentFinal.png")
riolu_tournament_final_image = pygame.transform.scale(riolu_tournament_final_image, (screen_width, screen_height))
riolu_tournament_final_end_image = pygame.image.load("RioluTournamentFinalFaintEnd.png")
riolu_tournament_final_end_image = pygame.transform.scale(riolu_tournament_final_end_image, (screen_width, screen_height))
# New variables for the tournament sequence
lapras_tournament_part = 0
gible_tournament_part = 0
riolu_final_part = 0
gible_final_part = 0
tournament_over = False
tournament_winner_declared = False
# New variables for the final battle sequence
final_battle_started = False
final_battle_dialogue_shown = False
villain_defeated = False
# Load the final battle image
final_battle_image = pygame.image.load('Final_Battle.png')
final_battle_image = pygame.transform.scale(final_battle_image, (screen_width, screen_height))
# Load tournament battle images
lapras_tournament_image = pygame.image.load("LaprasTournament.png")
lapras_tournament_image = pygame.transform.scale(lapras_tournament_image, (screen_width, screen_height))
lapras_tournament_end_image = pygame.image.load("LaprasTournamentEND.png")
lapras_tournament_end_image = pygame.transform.scale(lapras_tournament_end_image,(screen_width, screen_height))
gible_tournament1_image = pygame.image.load("GibleTournament1.png")
gible_tournament1_image = pygame.transform.scale(gible_tournament1_image, (screen_width, screen_height))
gible_tournament1_end_image = pygame.image.load("GibleTournament1END.png")
gible_tournament1_end_image = pygame.transform.scale(gible_tournament1_end_image,(screen_width, screen_height))
riolu_tournament_final_image = pygame.image.load("RioluTournamentFinal.png")
riolu_tournament_final_image = pygame.transform.scale(riolu_tournament_final_image, (screen_width, screen_height))
riolu_tournament_final_faint_end_image = pygame.image.load("RioluTournamentFinalFaintEnd.png")
riolu_tournament_final_faint_end_image = pygame.transform.scale(riolu_tournament_final_faint_end_image, (screen_width, screen_height))
gible_tournament_final_image = pygame.image.load("GibleTournamentFinal.png")
gible_tournament_final_image = pygame.transform.scale(gible_tournament_final_image, (screen_width, screen_height))
# New game state variables for the tournament sequence
in_tournament = False
current_tournament_part = 0
game_over = False

# Scale images
gible_battle_images = [pygame.transform.scale(img, (screen_width, screen_height)) for img in gible_battle_images]
lapras_battle_images = [pygame.transform.scale(img, (screen_width, screen_height)) for img in lapras_battle_images]

# New game states
training_gible = False
training_lapras = False
current_gible_part = 0
current_lapras_part = 0
# Before the game loop, declare and initialize the new flags
gible_battle1_end = False
gible_battle2_end = False
lapras_battle1_end = False
lapras_battle2_end = False
# Load the "NewPokemonDialogue.png" image
new_pokemon_dialogue_image = pygame.image.load('NewPokemonDialogue.png')
new_pokemon_dialogue_image = pygame.transform.scale(new_pokemon_dialogue_image, (screen_width, screen_height))
# New game states
catching_pokemon_sequence = False
caught_pokemon_dialogue_shown = False
# New variables for the training sequence
training_sequence_started = False
current_training_part = 0
# New dialogue variables
riolu_battle_dialogue = ""
villain_image1_dialogue = ""
villain_image1_shown = False
# New game states
tracking_sequence = False
on_route1 = False
battle_vs_villain_shown = False
villain_encounter = False
riolu_battle_shown = False
villain_dialogue = ""
# At the beginning of your script, initialize a flag for the uncle dialogue
uncle_dialogue_shown = False
# Flag to determine if the choice should be shown
show_choice = False
choice_selected = None  # Store the player's choice
training_completed = False
# Colors, Fonts, and Texts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)  # Adjust size as needed
input_box_color = pygame.Color('lightskyblue3')
active_input_box_color = pygame.Color('dodgerblue2')
# Text input box
input_box = pygame.Rect(300, 300, 200, 40)  # Adjust size and position as needed
color = input_box_color
active = False
text = ''
entered_name = False
selected_gender = None  # None, 'boy', or 'girl'
show_title_screen = True  # Flag to show the title screen initially
# New dialogue variables
police_station_dialogue = ""
police_station_dialogue_shown = False
# Initialize variables for different game states
show_chapter_screen = False
chapter_text_displayed = False
dialogue_start_time = 0
dialogue_text = "*crash* AAAAAAAAAA"
show_dialogue = False
show_choice = False
choice_selected = None
new_choice_displayed = False
new_choice_selected = None
in_living_room = False  # Define in_living_room here
# New variable for the Riolu exchange game-over state
riolu_exchange_game_over = False
dialogue_after_choice = ""
at_police_station = False
going_back_home = False
back_home_dialogue_shown = False
post_tournament_scene = False
# Flags for post-tournament sequence
tournament_won = False
post_tournament_dialogue_shown = False
# Load the "OutsidePoliceStation.png" image
outside_police_station_image = pygame.image.load('OutsidePoliceStation.png')
outside_police_station_image = pygame.transform.scale(outside_police_station_image, (screen_width, screen_height))
# New variables for the outside police station scene
outside_police_station_shown = False
outside_police_station_choice = None
# Before the game loop, declare and initialize the new variable
show_training_choice = False
catching_pokemon_sequence = False
# Initialization (before the game loop)
training_sequence_started = False
current_training_part = 0
training_completed = False
tournament_started = False
showing_tournament_prompt = False
tournament_dialogue_shown = False
tournament_battles_started = False
# Define tournament states
T_STATE_LAPRAS_1 = 1
T_STATE_LAPRAS_2 = 2
T_STATE_GIBLE_1 = 3
T_STATE_GIBLE_2 = 4
T_STATE_RIOLU_FINAL = 5
T_STATE_GIBLE_FINAL_1 = 6
T_STATE_GIBLE_FINAL_2 = 7
T_STATE_WINNER = 8
# Dialogue box settings
dialogue_box_height = 120
dialogue_box_y = screen_height - dialogue_box_height
dialogue_box_rect = pygame.Rect(50, dialogue_box_y, screen_width - 100, dialogue_box_height)
current_dialogue_part = 0  # Tracks which part of the dialogue is currently being displayed
current_riolu_dialogue_part = 0
current_villain_dialogue_part = 0
# New game state variables for Chapter 2
waiting_for_keypress = False
chapter2_start_time = 0
show_chapter2_screen = False
chapter2_text_displayed = False
show_choice3 = False
choice3_selected = None
game_state = 'normal'
# Add these variables at the beginning of your script
last_keypress_time = 0
keypress_delay = 1000  # Delay in milliseconds (1000 ms = 1 second)
def display_dialogue(screen, font, text, box_rect, active):
    if active:
        # Draw the dialogue box
        pygame.draw.rect(screen, WHITE, box_rect)
        pygame.draw.rect(screen, BLACK, box_rect, 2)
        # Split the dialogue text into lines that fit in the dialogue box
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = current_line + word + ' '
            if font.size(test_line)[0] <= box_rect.width - 20:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '
        lines.append(current_line)
        # Render each line of text within the dialogue box
        y_offset = 10
        for line in lines:
            line_surface = font.render(line, True, BLACK)
            screen.blit(line_surface, (box_rect.x + 10, box_rect.y + y_offset))
            y_offset += font.get_linesize()
# Dialogue box settings
dialogue_box_rect = pygame.Rect(50, screen_height - 150, screen_width - 100, 100)
# Initialize tournament state
tournament_state = T_STATE_LAPRAS_1

# Game loop
running = True
while running:
    current_time = pygame.time.get_ticks()
    police_station_dialogue_parts = [
        " ",
        "Uncle: There you are! Before I give you any details I need to make sure that you can take care of yourself.",
        f"{text}: Okay, name it.",
        "Uncle: If you win the Pokemon Tournament in town, I will know you can handle getting your sister back.",
        f"{text}: Sounds easy enough.",
        "Uncle: Okay while you do that I will gather more intel on Team Vultron and them having kidnapped your sister."
    ]
    riolu_battle_dialogue_parts = [
        f"{text}: Alright Riolu, do quick attack!",
        "Riolu: *ignores " + text + "*",
        f"{text}: Riolu! I need you to attack!",
        "Riolu: *sits down in the grass*"
    ]
    villain_encounter_dialogue_parts = [
        "Vultron Boss: HAHAHAHA you're not even worth my time. Go back home."
    ]
    training_dialogues = [
        "Okay Riolu, let's do this! Use Force Palm!",
        "Riolu, use Quick Attack!",
        "Riolu, use Counter!",
        "Riolu, let's finish this with Force Palm!"
    ]
    police_station_dialogue = [
        "Uncle: Well done, you won the tournament",
        f"{text}: Thanks have you been able to find out anymore of my sister's kidnapping?",
        "Uncle: Yes, Team Vultron is holding her as ransom in exchange for your Riolu."
    ]
    riolu_training_images = [Riolu_Battle1_image, riolu_pokemon_battle_image, riolu_trainer_battle_image]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if show_title_screen:
            # Any key press will continue to the loading screen
            if event.type == pygame.KEYDOWN:
                show_title_screen = False
        elif not entered_name:
            # If the user clicks on the input box, activate it
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = active_input_box_color if active else input_box_color
            # Handle typing in the input box
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        entered_name = True
                        active = False
                        color = input_box_color
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        elif entered_name and selected_gender is None:
            # Handle gender selection
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boy_image.get_rect(topleft=(100, 400)).collidepoint(event.pos):
                    selected_gender = 'boy'
                    chapter_start_time = current_time  # Set the time for "CHAPTER 1" display
                elif girl_image.get_rect(topleft=(300, 400)).collidepoint(event.pos):
                    selected_gender = 'girl'
                    chapter_start_time = current_time  # Set the time for "CHAPTER 1" display
        if selected_gender and not show_chapter_screen and not chapter_text_displayed:
            # User has selected gender, now show "CHAPTER 1"
            show_chapter_screen = True
            chapter_text_displayed = True
            chapter_start_time = current_time  # Record the start time for "CHAPTER 1"
        # Once "CHAPTER 1" has been displayed for 2 seconds, show the initial dialogue
        elif show_chapter_screen and current_time - chapter_start_time >= 2000:
            show_chapter_screen = False
            show_dialogue = True
        if show_dialogue:
            # Render dialogue
            display_dialogue(screen, font, dialogue_text, dialogue_box_rect, True)

            # Check for key press to continue from the dialogue
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Handle the dialogue progression
                if dialogue_text == "*crash* AAAAAAAAAA":
                    dialogue_text = "Mom: " + text + ", someone just kidnapped your sister!"
                    show_choice = True  # Present the choice to the player
                    show_dialogue = False
                elif dialogue_text == "Mom: " + text + ", someone just kidnapped your sister!":
                    dialogue_text = text + ": WHAT!? I am going to go after her!"
                elif dialogue_text == text + ": WHAT!? I am going to go after her!":
                    dialogue_text = "Mom: No! I cannot lose two kids today. We should call your uncle, the police chief at Lexington."
                elif dialogue_text == "Mom: No! I cannot lose two kids today. We should call your uncle, the police chief at Lexington.":
                    dialogue_text = text + ": We have to do something, we can't just sit around."
                elif dialogue_text == text + ": We have to do something, we can't just sit around.":
                    new_choice_displayed = True
                    show_dialogue = False
                    new_choice_selected = None
                    screen.blit(red_livingroom_image, (0, 0))
                    # Add new conditions here for further dialogue lines
                else:
                    show_dialogue = False  # End of this dialogue sequence

        if show_choice and not choice_selected:
            # Display the options for the player to choose
            choice_text = font.render("1: Investigate, 2: Stay in your bedroom", True, WHITE)
            screen.blit(choice_text, (100, screen_height // 2))  # Adjust position as needed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_2:  # Both choices lead to the same path
                    choice_selected = "investigate" if event.key == pygame.K_1 else "stay"
                    in_living_room = True  # Move to living room scene
                    dialogue_text = "Mom: " + text + ", someone just kidnapped your sister!"
                    show_dialogue = True
                    show_choice = False
                elif event.key == pygame.K_2:  # Stay in bedroom
                    choice_selected = "stay"
                    dialogue_text = text + ": WHAT!? I am going to go after her!"
                    show_dialogue = True
                    show_choice = False
        if new_choice_displayed and not new_choice_selected:
            # Display the new choices here
            screen.blit(red_livingroom_image, (0,0))
            new_choice_text = font.render("1: Steal Dad's Pokemon, 2: Call Uncle", True, BLACK)
            screen.blit(new_choice_text, (100, screen_height // 3))  # Adjust position as needed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    new_choice_selected = "steal"
                    dialogue_after_choice = f"{text}: We don't have time to wait around, Dad won't mind me taking his new pokemon to save sis."
                    screen.blit(Route1_image, (0,0))
                elif event.key == pygame.K_2:
                    new_choice_selected = "call_for_help"
                    dialogue_after_choice = "Mom: *on phone with uncle* I need you " + text + ", to go to see your uncle. He needs your help because his unit is spread too thin. Take your Dad's new pokemon."
        if new_choice_selected == "steal":
            if not on_route1:
                screen.blit(Route1_image, (0, 0))  # Display Route1 background
                display_dialogue(screen, font, dialogue_after_choice, dialogue_box_rect, True)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    on_route1 = True  # Transition to the next scene after key press

            elif on_route1 and not villain_encounter:
                screen.blit(battle_vs_villain_image, (0, 0))  # Display Villain encounter background
                villain_dialogue = "*after three hours of tracking footprints*\n" + \
                                   f"{text}: Hey! That's my sister's backpack, where did you get it?\n" + \
                                   "Vultron Boss: What? Your sister you say? Might as well kidnap both kids if we can"
                display_dialogue(screen, font, villain_dialogue, dialogue_box_rect, True)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    villain_encounter = True  # Transition to the next scene after key press
            elif villain_encounter and not riolu_battle_shown:
                screen.blit(riolu_battle_image, (0, 0))  # Display RioluBattle background
                if current_riolu_dialogue_part < len(riolu_battle_dialogue_parts):
                    display_dialogue(screen, font, riolu_battle_dialogue_parts[current_riolu_dialogue_part],
                                     dialogue_box_rect, True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_riolu_dialogue_part += 1
                elif current_villain_dialogue_part < len(villain_encounter_dialogue_parts):
                    screen.blit(villain_image1, (0, 0))  # Display Villain Image
                    display_dialogue(screen, font, villain_encounter_dialogue_parts[current_villain_dialogue_part],
                                     dialogue_box_rect, True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_villain_dialogue_part += 1
                    if current_riolu_dialogue_part >= len(riolu_battle_dialogue_parts) and not villain_image1_shown:
                        screen.blit(villain_image1, (0, 0))  # Display Villain Image
                        display_dialogue(screen, font, villain_encounter_dialogue_parts[0], dialogue_box_rect, True)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            riolu_battle_shown = True
            elif riolu_battle_shown and not going_back_home:
                screen.blit(going_back_home_image, (0, 0))  # Display Going Back Home background
                back_home_dialogue = f"{text}: I need to go back home and figure out what to do next..."
                display_dialogue(screen, font, back_home_dialogue, dialogue_box_rect, True)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    going_back_home = True

            elif going_back_home and not back_home_dialogue_shown:
                # This block now mirrors the 'call_for_help' option
                screen.blit(red_livingroom_image, (0, 0))  # Display Red Living Room background
                dialogue_after_choice = "Mom: *on phone with uncle* I need you " + text + ", to go to see your uncle. He needs your help because his unit is spread too thin. Take your Dad's new pokemon."
                display_dialogue(screen, font, dialogue_after_choice, dialogue_box_rect, True)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    on_route1 = True
                    back_home_dialogue_shown = True
            elif on_route1 and not at_police_station:
                # Display Route1 scene
                screen.blit(Route1_image, (0, 0))
                route1_dialogue = f"{text}: Let's hurry up and get to my Uncle's police station."
                display_dialogue(screen, font, route1_dialogue, dialogue_box_rect, True)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    at_police_station = True
            if at_police_station and not police_station_dialogue_shown:
                screen.blit(police_station_image, (0, 0))  # Display Police Station background
                # Check if there are more dialogue parts to display
                if current_dialogue_part < len(police_station_dialogue_parts):
                    display_dialogue(screen, font, police_station_dialogue_parts[current_dialogue_part],
                                     dialogue_box_rect, True)

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_dialogue_part += 1  # Move to the next part of the dialogue
                if current_dialogue_part >= len(police_station_dialogue_parts):
                            police_station_dialogue_shown = True
                            show_chapter2_screen = True
                            chapter2_start_time = pygame.time.get_ticks()
            if show_chapter2_screen and not chapter2_text_displayed:
                    screen.fill(BLACK)
                    chapter2_text = font.render("CHAPTER 2", True, WHITE)
                    screen.blit(chapter2_text, (screen_width // 2 - chapter2_text.get_width() // 2,
                                            screen_height // 2 - chapter2_text.get_height() // 2))
                    if pygame.time.get_ticks() - chapter2_start_time > 2000:  # Display "Chapter 2" for 2 seconds
                        show_chapter2_screen = False
                        chapter2_text_displayed = True
                        show_choice3 = True

            if show_choice3 and not choice3_selected:
                    screen.blit(choice3_image, (0, 0))  # Display Choice3 background
                    choice3_text = font.render("1: Train with Riolu, 2: Catch New Pokemon", True, BLACK)
                    screen.blit(choice3_text, (100, screen_height // 2 + 50))
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            choice3_selected = "train_riolu"
                            #Add logic for training with Riolu
                        elif event.key == pygame.K_2:
                            choice3_selected = "catch_pokemon"
                            # Add logic for catching new Pokemon
            # Inside the game loop
            if choice3_selected == "train_riolu":
                if not training_sequence_started:
                    training_sequence_started = True  # Start the training sequence

                if training_sequence_started and not training_completed:
                    if current_training_part < len(riolu_training_images):
                        screen.blit(riolu_training_images[current_training_part], (0, 0))
                        display_dialogue(screen, font, training_dialogues[current_training_part], dialogue_box_rect,
                                         True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_training_part += 1
                        if current_training_part >= len(riolu_training_images):
                            training_completed = True
                            tournament_started = True
                            current_training_part = 0  # Reset for the tournament sequence

                if tournament_started and not showing_tournament_prompt:
                    screen.blit(tournament_image_riolu, (0, 0))
                    tournament_dialogue = "Time for the tournament. Let's do this, Riolu!"
                    display_dialogue(screen, font, tournament_dialogue, dialogue_box_rect, True)
                    showing_tournament_prompt = True

                elif showing_tournament_prompt:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        showing_tournament_prompt = False
                        tournament_battles_started = True  # Now ready to start the battles

                if tournament_battles_started:
                    if current_tournament_part == 0:
                        screen.blit(riolu_tournament1_image, (0, 0))
                        display_dialogue(screen, font, "Riolu use Aura Sphere!", dialogue_box_rect, True)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            current_tournament_part = 1
                    elif current_tournament_part == 1:
                        screen.blit(riolu_tournament1_end_image, (0, 0))
                        display_dialogue(screen, font, "Let's go Riolu, we won our first match!", dialogue_box_rect,
                                         True)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            current_tournament_part = 2
                    elif current_tournament_part == 2:
                        screen.blit(riolu_tournament_final_image, (0, 0))
                        display_dialogue(screen, font,
                                         "This is it Riolu, we have made it to the final! Let's use Aura Sphere!",
                                         dialogue_box_rect, True)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            current_tournament_part = 3
                    elif current_tournament_part == 3:
                        screen.blit(riolu_tournament_final_end_image, (0, 0))
                        display_dialogue(screen, font, "Announcer: Riolu has lost! 1 hit KO!", dialogue_box_rect, True)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                            game_over = True

                if game_over:
                    screen.fill(BLACK)
                    game_over_text = font.render("GAME OVER", True, WHITE)
                    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2,
                                                 screen_height // 2 - game_over_text.get_height() // 2))

            # Inside your game loop
            if choice3_selected == "catch_pokemon":
                if not catching_pokemon_sequence:
                    catching_pokemon_sequence = True
                    training_choice_shown = False  # To display the training choice once

                if catching_pokemon_sequence and not training_choice_shown:
                    screen.blit(new_pokemon_dialogue_image, (0, 0))  # Display NewPokemonDialogue background
                    caught_pokemon_dialogue = f"{text}: Sweet, caught a Gible and Lapras to join my team!"
                    display_dialogue(screen, font, caught_pokemon_dialogue, dialogue_box_rect, True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        training_choice_shown = True
                        show_training_choice = True  # Show training choice after dialogue

                if show_training_choice and not training_gible and not training_lapras:
                    training_choice_text = font.render("1: Train Gible, 2: Train Lapras", True, BLACK)
                    screen.blit(training_choice_text, (100, screen_height // 2 + 50))
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            training_gible = True
                            show_training_choice = False
                        elif event.key == pygame.K_2:
                            training_lapras = True
                            show_training_choice = False

                if training_gible and current_gible_part < len(gible_battle_images):
                    screen.blit(gible_battle_images[current_gible_part], (0, 0))
                    gible_dialogue = "Gible, use Tackle!" if current_gible_part % 2 == 0 else "We did it Gible!"
                    display_dialogue(screen, font, gible_dialogue, dialogue_box_rect, True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_gible_part += 1
                        if current_gible_part >= len(gible_battle_images):
                            training_gible = False  # Gible training completed
                            training_completed = True

                if training_lapras and current_lapras_part < len(lapras_battle_images):
                    screen.blit(lapras_battle_images[current_lapras_part], (0, 0))
                    lapras_dialogue = "Lapras, use Ice Beam!" if current_lapras_part % 2 == 0 else "Way to go Lapras!"
                    display_dialogue(screen, font, lapras_dialogue, dialogue_box_rect, True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_lapras_part += 1
                        if current_lapras_part >= len(lapras_battle_images):
                            training_lapras = False  # Lapras training completed
                            training_completed = True
                # Tournament sequence logic
                if training_completed:
                    if not in_tournament:
                        # Display initial tournament scene
                        screen.blit(tournament_image_riolu, (0, 0))
                        display_dialogue(screen, font, "This is how we prove ourselves, guys!", dialogue_box_rect, True)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                            in_tournament = True
                            tournament_state = 'lapras_round1'
                            last_keypress_time = pygame.time.get_ticks()

                    if in_tournament:
                        # Lapras Tournament Battles
                        if tournament_state == 'lapras_round1':
                            screen.blit(lapras_tournament_image, (0, 0))
                            display_dialogue(screen, font, "Use Water Gun, Lapras!", dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'lapras_round1_end'
                                last_keypress_time = pygame.time.get_ticks()

                        elif tournament_state == 'lapras_round1_end':
                            screen.blit(lapras_tournament_end_image, (0, 0))
                            display_dialogue(screen, font, "Let's go Lapras, our first win!", dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'gible_round1'
                                last_keypress_time = pygame.time.get_ticks()

                        # Gible Tournament Battles
                        if tournament_state == 'gible_round1':
                            screen.blit(gible_tournament1_image, (0, 0))
                            display_dialogue(screen, font, "Alright Gible, use Dragon Rage!", dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'gible_round1_end'
                                last_keypress_time = pygame.time.get_ticks()

                        elif tournament_state == 'gible_round1_end':
                            screen.blit(gible_tournament1_end_image, (0, 0))
                            display_dialogue(screen, font,
                                             "Yes, we did it Gible! We are moving on to the championship!",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'riolu_final'
                                last_keypress_time = pygame.time.get_ticks()

                        # Riolu Final Battle
                        if tournament_state == 'riolu_final':
                            screen.blit(riolu_tournament_final_image, (0, 0))
                            display_dialogue(screen, font, "OK Riolu, use Aura Sphere!", dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'riolu_final_end'
                                last_keypress_time = pygame.time.get_ticks()

                        elif tournament_state == 'riolu_final_end':
                            screen.blit(riolu_tournament_final_faint_end_image, (0, 0))
                            display_dialogue(screen, font, "Announcer: OH, Riolu has fainted after one hit!",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'gible_final'
                                last_keypress_time = pygame.time.get_ticks()

                        # Gible Final Battle
                        if tournament_state == 'gible_final':
                            screen.blit(gible_tournament_final_image, (0, 0))
                            display_dialogue(screen, font,
                                             "Announcer: After a long battle, each are left with one Pokemon.",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'gible_final_end'
                                last_keypress_time = pygame.time.get_ticks()

                        elif tournament_state == 'gible_final_end':
                            display_dialogue(screen, font, f"{text}: Okay Gible, one final Dragon Rage!",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'congrats'
                                last_keypress_time = pygame.time.get_ticks()

                        # Check if the tournament has just been won
                        if tournament_state == 'congrats' and not tournament_won:
                            screen.fill(BLACK)
                            winner_text = font.render("CONGRATS, YOU WON THE TOURNAMENT!", True, WHITE)
                            screen.blit(winner_text, (screen_width // 2 - winner_text.get_width() // 2,
                                                      screen_height // 2 - winner_text.get_height() // 2))
                            pygame.display.flip()  # Ensure the screen updates to show the winner text
                            pygame.time.delay(2000)  # Wait for 2 seconds
                            tournament_won = True

                        # Check if it's time to show the post-tournament dialogue
                        if tournament_won and not post_tournament_dialogue_shown:
                            post_tournament_dialogue_shown = True
                            current_dialogue_part = 0  # Reset the dialogue part counter

                        # Handle the post-tournament dialogue at the police station
                        if post_tournament_dialogue_shown and not outside_police_station_shown:
                            screen.blit(police_station_image, (0, 0))
                            police_station_dialogue = [
                                "Uncle: Well done, you won the tournament",
                                f"{text}: Thanks have you been able to find out anymore of my sister's kidnapping?",
                                "Uncle: Yes, Team Vultron is holding her as ransom in exchange for your Riolu.",
                                f"{text}: What!? That is absurd!",
                                "Uncle: I figured you would say that, we know they are hiding out in an abandoned building in town.",
                                "Uncle: Don't get any ideas now."
                            ]

                            if current_dialogue_part < len(police_station_dialogue):
                                display_dialogue(screen, font, police_station_dialogue[current_dialogue_part],
                                                 dialogue_box_rect, True)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                    current_dialogue_part += 1  # Progress to the next part of the dialogue
                            else:
                                post_tournament_dialogue_shown = False
                                outside_police_station_shown = True  # Ready to move on to the outside scene

                        # Display choice at the outside of the police station
                        if outside_police_station_shown and outside_police_station_choice is None:
                                screen.blit(outside_police_station_image, (0, 0))
                                choice_text = font.render("1: Exchange Riolu for Sis, 2: Rescue Sis", True, BLACK)
                                screen.blit(choice_text, (100, screen_height // 2 + 50))
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_1:
                                        outside_police_station_choice = "exchange_riolu"
                                        # Logic for exchanging Riolu
                                    elif event.key == pygame.K_2:
                                        outside_police_station_choice = "rescue_sis"
                                        # Logic for rescuing Sis

                        # Logic based on the choice made at the outside of the police station
                        if outside_police_station_choice == "exchange_riolu":
                            riolu_exchange_game_over = True

                        # Display game-over screen for Riolu exchange scenario
                        if riolu_exchange_game_over:
                            screen.fill(BLACK)
                            game_over_text = font.render(f"{text} GAVE UP RIOLU. GAME OVER", True, WHITE)
                            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2,
                                                         screen_height // 2 - game_over_text.get_height() // 2))
                        if outside_police_station_choice == "rescue_sis" and not final_battle_started:
                            # Display the Villain image with the initial dialogue
                            screen.blit(villain_image1, (0, 0))
                            villain_initial_dialogue = [
                                "Villain: So you have decided to turn in your pokemon.",
                                f"{text}: No, I have come to take my sister back from you!"
                            ]
                            if current_dialogue_part < len(villain_initial_dialogue):
                                display_dialogue(screen, font, villain_initial_dialogue[current_dialogue_part],
                                                 dialogue_box_rect, True)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                    current_dialogue_part += 1
                            else:
                                final_battle_started = True
                                current_dialogue_part = 0  # Reset for next use
                        if final_battle_started and not final_battle_dialogue_shown:
                            # Display the final battle image with Riolu
                            screen.blit(final_battle_image, (0, 0))
                            display_dialogue(screen, font, "Riolu, let's finish this with Aura Sphere!",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                final_battle_dialogue_shown = True
                        if final_battle_dialogue_shown and not villain_defeated:
                            # Display the Villain image with the defeat dialogue
                            screen.blit(villain_image1, (0, 0))
                            display_dialogue(screen, font, "Villain: To think a kid like you could be this good.",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                villain_defeated = True
                        if villain_defeated:
                            # Display the game over screen
                            screen.fill(BLACK)
                            game_over_text = font.render("GAME OVER", True, WHITE)
                            screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2,
                                                         screen_height // 2 - game_over_text.get_height() // 2))
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                running = False  # Exit the game loop
        if new_choice_selected == "call_for_help":
            if not on_route1:
                screen.blit(red_livingroom_image, (0, 0))  # Display Red Living Room background
                display_dialogue(screen, font, dialogue_after_choice, dialogue_box_rect, True)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    on_route1 = True

            elif on_route1 and not at_police_station:
                screen.blit(Route1_image, (0, 0))  # Display Route1 background
                route1_dialogue = f"{text}: Sweet, let's hurry up and get to my Uncle's police station."
                display_dialogue(screen, font, route1_dialogue, dialogue_box_rect, True)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    at_police_station = True

            if at_police_station and not police_station_dialogue_shown:
                screen.blit(police_station_image, (0, 0))  # Display Police Station background
                # Check if there are more dialogue parts to display
                if current_dialogue_part < len(police_station_dialogue_parts):
                    display_dialogue(screen, font, police_station_dialogue_parts[current_dialogue_part],
                                     dialogue_box_rect, True)

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_dialogue_part += 1  # Move to the next part of the dialogue
                if current_dialogue_part >= len(police_station_dialogue_parts):
                            police_station_dialogue_shown = True
                            show_chapter2_screen = True
                            chapter2_start_time = pygame.time.get_ticks()
            if show_chapter2_screen and not chapter2_text_displayed:
                screen.fill(BLACK)
                chapter2_text = font.render("CHAPTER 2", True, WHITE)
                screen.blit(chapter2_text, (screen_width // 2 - chapter2_text.get_width() // 2,
                                            screen_height // 2 - chapter2_text.get_height() // 2))
                if pygame.time.get_ticks() - chapter2_start_time > 2000:  # Display "Chapter 2" for 2 seconds
                    show_chapter2_screen = False
                    chapter2_text_displayed = True
                    show_choice3 = True

            if show_choice3 and not choice3_selected:
                screen.blit(choice3_image, (0, 0))  # Display Choice3 background
                choice3_text = font.render("1: Train with Riolu, 2: Catch New Pokemon", True, BLACK)
                screen.blit(choice3_text, (100, screen_height // 2 +  50))
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        choice3_selected = "train_riolu"
                        # Add logic for training with Riolu
                    elif event.key == pygame.K_2:
                        choice3_selected = "catch_pokemon"
                        # Add logic for catching new Pokemon
                        # Inside your game loop
                        # Inside the game loop
            if choice3_selected == "train_riolu":
                            if not training_sequence_started:
                                training_sequence_started = True  # Start the training sequence

                            if training_sequence_started and not training_completed:
                                if current_training_part < len(riolu_training_images):
                                    screen.blit(riolu_training_images[current_training_part], (0, 0))
                                    display_dialogue(screen, font, training_dialogues[current_training_part],
                                                     dialogue_box_rect,
                                                     True)
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                    current_training_part += 1
                                    if current_training_part >= len(riolu_training_images):
                                        training_completed = True
                                        tournament_started = True
                                        current_training_part = 0  # Reset for the tournament sequence

                            if tournament_started and not showing_tournament_prompt:
                                screen.blit(tournament_image_riolu, (0, 0))
                                tournament_dialogue = "Time for the tournament. Let's do this, Riolu!"
                                display_dialogue(screen, font, tournament_dialogue, dialogue_box_rect, True)
                                showing_tournament_prompt = True

                            elif showing_tournament_prompt:
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                    showing_tournament_prompt = False
                                    tournament_battles_started = True  # Now ready to start the battles

                            if tournament_battles_started:
                                if current_tournament_part == 0:
                                    screen.blit(riolu_tournament1_image, (0, 0))
                                    display_dialogue(screen, font, "Riolu use Aura Sphere!", dialogue_box_rect, True)
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                        current_tournament_part = 1
                                elif current_tournament_part == 1:
                                    screen.blit(riolu_tournament1_end_image, (0, 0))
                                    display_dialogue(screen, font, "Let's go Riolu, we won our first match!",
                                                     dialogue_box_rect,
                                                     True)
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                        current_tournament_part = 2
                                elif current_tournament_part == 2:
                                    screen.blit(riolu_tournament_final_image, (0, 0))
                                    display_dialogue(screen, font,
                                                     "This is it Riolu, we have made it to the final! Let's use Aura Sphere!",
                                                     dialogue_box_rect, True)
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                        current_tournament_part = 3
                                elif current_tournament_part == 3:
                                    screen.blit(riolu_tournament_final_end_image, (0, 0))
                                    display_dialogue(screen, font, "Announcer: Riolu has lost! 1 hit KO!",
                                                     dialogue_box_rect, True)
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                        game_over = True

                            if game_over:
                                screen.fill(BLACK)
                                game_over_text = font.render("GAME OVER", True, WHITE)
                                screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2,
                                                             screen_height // 2 - game_over_text.get_height() // 2))
                            # Inside your game loop
            if choice3_selected == "catch_pokemon":
                if not catching_pokemon_sequence:
                    catching_pokemon_sequence = True
                    training_choice_shown = False  # To display the training choice once

                if catching_pokemon_sequence and not training_choice_shown:
                    screen.blit(new_pokemon_dialogue_image, (0, 0))  # Display NewPokemonDialogue background
                    caught_pokemon_dialogue = f"{text}: Sweet, caught a Gible and Lapras to join my team!"
                    display_dialogue(screen, font, caught_pokemon_dialogue, dialogue_box_rect, True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        training_choice_shown = True
                        show_training_choice = True  # Show training choice after dialogue

                if show_training_choice and not training_gible and not training_lapras:
                    training_choice_text = font.render("1: Train Gible, 2: Train Lapras", True, BLACK)
                    screen.blit(training_choice_text, (100, screen_height // 2 + 50))
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            training_gible = True
                            show_training_choice = False
                        elif event.key == pygame.K_2:
                            training_lapras = True
                            show_training_choice = False

                if training_gible and current_gible_part < len(gible_battle_images):
                    screen.blit(gible_battle_images[current_gible_part], (0, 0))
                    gible_dialogue = "Gible, use Tackle!" if current_gible_part % 2 == 0 else "We did it Gible!"
                    display_dialogue(screen, font, gible_dialogue, dialogue_box_rect, True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_gible_part += 1
                        if current_gible_part >= len(gible_battle_images):
                            training_gible = False  # Gible training completed
                            training_completed = True

                if training_lapras and current_lapras_part < len(lapras_battle_images):
                    screen.blit(lapras_battle_images[current_lapras_part], (0, 0))
                    lapras_dialogue = "Lapras, use Ice Beam!" if current_lapras_part % 2 == 0 else "Way to go Lapras!"
                    display_dialogue(screen, font, lapras_dialogue, dialogue_box_rect, True)
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_lapras_part += 1
                        if current_lapras_part >= len(lapras_battle_images):
                            training_lapras = False  # Lapras training completed
                            training_completed = True
                # Tournament sequence logic
                if training_completed:
                    if not in_tournament:
                        # Display initial tournament scene
                        screen.blit(tournament_image_riolu, (0, 0))
                        display_dialogue(screen, font, "This is how we prove ourselves, guys!", dialogue_box_rect, True)
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                            in_tournament = True
                            tournament_state = 'lapras_round1'
                            last_keypress_time = pygame.time.get_ticks()

                    if in_tournament:
                        # Lapras Tournament Battles
                        if tournament_state == 'lapras_round1':
                            screen.blit(lapras_tournament_image, (0, 0))
                            display_dialogue(screen, font, "Use Water Gun, Lapras!", dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'lapras_round1_end'
                                last_keypress_time = pygame.time.get_ticks()

                        elif tournament_state == 'lapras_round1_end':
                            screen.blit(lapras_tournament_end_image, (0, 0))
                            display_dialogue(screen, font, "Let's go Lapras, our first win!", dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'gible_round1'
                                last_keypress_time = pygame.time.get_ticks()

                        # Gible Tournament Battles
                        if tournament_state == 'gible_round1':
                            screen.blit(gible_tournament1_image, (0, 0))
                            display_dialogue(screen, font, "Alright Gible, use Dragon Rage!", dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'gible_round1_end'
                                last_keypress_time = pygame.time.get_ticks()

                        elif tournament_state == 'gible_round1_end':
                            screen.blit(gible_tournament1_end_image, (0, 0))
                            display_dialogue(screen, font,
                                             "Yes, we did it Gible! We are moving on to the championship!",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'riolu_final'
                                last_keypress_time = pygame.time.get_ticks()

                        # Riolu Final Battle
                        if tournament_state == 'riolu_final':
                            screen.blit(riolu_tournament_final_image, (0, 0))
                            display_dialogue(screen, font, "OK Riolu, use Aura Sphere!", dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'riolu_final_end'
                                last_keypress_time = pygame.time.get_ticks()

                        elif tournament_state == 'riolu_final_end':
                            screen.blit(riolu_tournament_final_faint_end_image, (0, 0))
                            display_dialogue(screen, font, "Announcer: OH, Riolu has fainted after one hit!",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'gible_final'
                                last_keypress_time = pygame.time.get_ticks()

                        # Gible Final Battle
                        if tournament_state == 'gible_final':
                            screen.blit(gible_tournament_final_image, (0, 0))
                            display_dialogue(screen, font,
                                             "Announcer: After a long battle, each are left with one Pokemon.",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'gible_final_end'
                                last_keypress_time = pygame.time.get_ticks()

                        elif tournament_state == 'gible_final_end':
                            display_dialogue(screen, font, f"{text}: Okay Gible, one final Dragon Rage!",
                                             dialogue_box_rect, True)
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and (
                                    pygame.time.get_ticks() - last_keypress_time > keypress_delay):
                                tournament_state = 'congrats'
                                last_keypress_time = pygame.time.get_ticks()

                                # Check if the tournament has just been won
                                if tournament_state == 'congrats' and not tournament_won:
                                    screen.fill(BLACK)
                                    winner_text = font.render("CONGRATS, YOU WON THE TOURNAMENT!", True, WHITE)
                                    screen.blit(winner_text, (screen_width // 2 - winner_text.get_width() // 2,
                                                              screen_height // 2 - winner_text.get_height() // 2))
                                    pygame.display.flip()  # Ensure the screen updates to show the winner text
                                    pygame.time.delay(2000)  # Wait for 2 seconds
                                    tournament_won = True

                                # Check if it's time to show the post-tournament dialogue
                                if tournament_won and not post_tournament_dialogue_shown:
                                    post_tournament_dialogue_shown = True
                                    current_dialogue_part = 0  # Reset the dialogue part counter

                                # Handle the post-tournament dialogue at the police station
                                if post_tournament_dialogue_shown and not outside_police_station_shown:
                                    screen.blit(police_station_image, (0, 0))
                                    police_station_dialogue = [
                                        "Uncle: Well done, you won the tournament",
                                        f"{text}: Thanks have you been able to find out anymore of my sister's kidnapping?",
                                        "Uncle: Yes, Team Vultron is holding her as ransom in exchange for your Riolu.",
                                        f"{text}: What!? That is absurd!",
                                        "Uncle: I figured you would say that, we know they are hiding out in an abandoned building in town.",
                                        "Uncle: Don't get any ideas now."
                                    ]

                                    if current_dialogue_part < len(police_station_dialogue):
                                        display_dialogue(screen, font, police_station_dialogue[current_dialogue_part],
                                                         dialogue_box_rect, True)
                                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                            current_dialogue_part += 1  # Progress to the next part of the dialogue
                                    else:
                                        post_tournament_dialogue_shown = False
                                        outside_police_station_shown = True  # Ready to move on to the outside scene

                                # Display choice at the outside of the police station
                                if outside_police_station_shown and outside_police_station_choice is None:
                                    screen.blit(outside_police_station_image, (0, 0))
                                    choice_text = font.render("1: Exchange Riolu for Sis, 2: Rescue Sis", True, BLACK)
                                    screen.blit(choice_text, (100, screen_height // 2 + 50))
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_1:
                                            outside_police_station_choice = "exchange_riolu"
                                            # Logic for exchanging Riolu
                                        elif event.key == pygame.K_2:
                                            outside_police_station_choice = "rescue_sis"
                                            # Logic for rescuing Sis
                                # Logic based on the choice made at the outside of the police station
                                if outside_police_station_choice == "exchange_riolu":
                                    riolu_exchange_game_over = True
                                # Display game-over screen for Riolu exchange scenario
                                if riolu_exchange_game_over:
                                    screen.fill(BLACK)
                                    game_over_text = font.render(f"{text} GAVE UP RIOLU. GAME OVER", True, WHITE)
                                    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2,
                                                                 screen_height // 2 - game_over_text.get_height() // 2))
                                if outside_police_station_choice == "rescue_sis" and not final_battle_started:
                                    # Display the Villain image with the initial dialogue
                                    screen.blit(villain_image1, (0, 0))
                                    villain_initial_dialogue = [
                                        "Villain: So you have decided to turn in your pokemon.",
                                        f"{text}: No, I have come to take my sister back from you!"
                                    ]
                                    if current_dialogue_part < len(villain_initial_dialogue):
                                        display_dialogue(screen, font, villain_initial_dialogue[current_dialogue_part],
                                                         dialogue_box_rect, True)
                                        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                            current_dialogue_part += 1
                                    else:
                                        final_battle_started = True
                                        current_dialogue_part = 0  # Reset for next use
                                if final_battle_started and not final_battle_dialogue_shown:
                                    # Display the final battle image with Riolu
                                    screen.blit(final_battle_image, (0, 0))
                                    display_dialogue(screen, font, "Riolu, let's finish this with Aura Sphere!",
                                                     dialogue_box_rect, True)
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                        final_battle_dialogue_shown = True
                                if final_battle_dialogue_shown and not villain_defeated:
                                    # Display the Villain image with the defeat dialogue
                                    screen.blit(villain_image1, (0, 0))
                                    display_dialogue(screen, font,
                                                     "Villain: To think a kid like you could be this good.",
                                                     dialogue_box_rect, True)
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                        villain_defeated = True
                                if villain_defeated:
                                    # Display the game over screen
                                    screen.fill(BLACK)
                                    game_over_text = font.render("GAME OVER", True, WHITE)
                                    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2,
                                                                 screen_height // 2 - game_over_text.get_height() // 2))
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                                        running = False  # Exit the game loop
    # Display the title page if the title screen flag is set
    if show_title_screen:
        screen.blit(title_page_image, (0, 0))
    # If the name has not been entered, show the name prompt screen
    elif not entered_name:
        screen.blit(name_prompt_image, (0, 0))
        prompt_text = font.render('Enter your name:', True, BLACK)
        screen.blit(prompt_text, (input_box.x, input_box.y - 40))  # Position above the input box
        pygame.draw.rect(screen, color, input_box, 2)
        txt_surface = font.render(text, True, BLACK)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        input_box.w = max(200, txt_surface.get_width() + 10)  # Adjust width if text is too long
    # If gender has not been selected, show the gender selection screen
    elif selected_gender is None:
        gender_prompt = font.render('Select Boy or Girl:', True, BLACK)
        screen.blit(gender_prompt, (100, 350))
        screen.blit(boy_image, (100, 400))
        screen.blit(girl_image, (300, 400))
    # If "CHAPTER 1" should be displayed, show it for 2 seconds
    elif show_chapter_screen and current_time - chapter_start_time < 2000:
        screen.fill(BLACK)
        chapter_text = font.render("CHAPTER 1", True, WHITE)
        screen.blit(chapter_text, (screen_width // 2 - chapter_text.get_width() // 2, screen_height // 2 - chapter_text.get_height() // 2))
    # Once "CHAPTER 1" has been displayed for 2 seconds, show the dialogue
    elif show_chapter_screen and current_time - chapter_start_time >= 2000:
        show_chapter_screen = False
        if not show_dialogue:
            show_dialogue = True
    if show_dialogue or (show_choice and not choice_selected):
        # Display the living room if the player is in the living room scene
        if in_living_room:
            screen.blit(red_livingroom_image, (0, 0))  # Living room image for the dialogue
        else:
            screen.blit(red_bedroom_image, (0, 0))  # Bedroom image for the dialogue
        if show_dialogue:
            # Render dialogue
            display_dialogue(screen, font, dialogue_text, dialogue_box_rect, True)
        if show_choice and not choice_selected:
            # Display the options for the player to choose
            choice_text = font.render("1: Investigate, 2: Stay in your bedroom", True, WHITE)  # Text color changed to WHITE for visibility
            screen.blit(choice_text, (100, screen_height // 2))  # Adjust position as needed
        if new_choice_displayed and not new_choice_selected:
            new_choice_text = font.render("1: Steal Dad's Pokemon, 2: Call Uncle", True, BLACK)
            screen.blit(new_choice_text, (100, screen_height // 3))
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()
sys.exit()
