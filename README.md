# SoftwareCarpentryFinalProject
Pokemon RPG Style Game
# Main Sections of my Game:
# Initialization: Setting up Pygame, loading images and sounds, initializing variables, and preparing game states.
# Game Loop: The heart of the game where input is processed, game states are updated, and graphics are rendered continuously.
# Event Handling: Responding to player inputs and system events.
# Rendering: Drawing elements on the screen, including backgrounds, characters, and text.
# pygame.init(): Initializes all the Pygame modules.
# Image Loading and Scaling: Loads images (pygame.image.load()) and scales them to fit the screen (pygame.transform.scale()). This includes characters, backgrounds, and other assets.
# Event Loop: Checks for events like key presses (pygame.KEYDOWN) or mouse clicks (pygame.MOUSEBUTTONDOWN) and handles them appropriately to progress the game or make choices.
# display_dialogue(screen, font, text, box_rect, active): A custom function to display dialogue text. It splits the text into lines that fit within a dialogue box and renders it on the screen. This function is vital for storytelling and player interaction.
# Game State Management: Variables like show_title_screen, entered_name, and tournament_state manage where the player is in the game and what should be displayed or executed.
# Rendering: The screen.blit() function is used to draw images and text on the screen. It's used extensively to create the visual elements of your game.
# Modular Approach: The game is structured into distinct sections and states, making it easier to manage and expand. Each section of the game, like the title screen, character selection, battle sequences, and dialogues, is handled in different parts of the code.
# State Management: The game flow is controlled by state variables. These variables determine what part of the game the player is currently in and what should be displayed or executed next.
# Event-Driven Programming: The game responds to user inputs (like keyboard and mouse events) and system events in the event loop. This makes the game interactive and responsive to player actions.
# Rendering and Graphics: The game uses a combination of static images and rendered text to create the visual experience. Pygame's rendering functions are used to draw these elements on the screen each frame.

# HOW TO PLAY
# Use keyboard inputs to navigate through the game.
# Engage in dialogues and make choices that affect the game's narrative and outcome.
# Train Pokémon and use them in battles to advance through the story.

# FEATURES
# Interactive Storyline: Players make decisions that influence the game's outcome, leading to different paths and endings.
# Battle Sequences: Engage in thrilling battles using Pokémon, each with unique abilities.
# Diverse Environments: Explore various backgrounds like police stations, battle arenas, and outdoor sceneries.
# Character Customization: Choose your character's gender and name for a personalized gaming experience.
