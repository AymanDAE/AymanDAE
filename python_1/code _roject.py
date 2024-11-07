import random

# Step 1: Start the Program
def start_program():
    """
    This function starts the game by asking the user to either create a new profile
    or log in to an existing profile. It calls either create_profile() or login() accordingly.
    """
    print("Welcome to the Game!")
    choice = input("Enter '1' to Create New Profile or '2' to Login: ")
    
    if choice == '1':
        create_profile()
    elif choice == '2':
        login()
    else:
        print("Invalid choice.")
        start_program()

# Step 2: Ask player to enter username, email, password to create new profile
def create_profile():
    """
    This function prompts the user to create a new profile by entering a username, email, and password.
    It checks if the username and email are unique and stores the profile data in dictionaries.
    """
    username = input("Enter a username: ")
    email = input("Enter your email: ")
    password = input("Create a password: ")
    
    # Check if username and email are unique
    if username in user_database or email in email_database:
        print("Username or email already used, please choose a different one.")
        create_profile()
    else:
        user_database[username] = {'email': email, 'password': password, 'score': 0}
        email_database[email] = username
        print("Profile created! Logging you in...")
        game_title_screen(username)

# Step 3: Login with existing username and password
def login():
    """
    This function allows the user to log in by entering their username and password.
    If the credentials are correct, it starts the game.
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username in user_database and user_database[username]['password'] == password:
        print("Login successful!")
        game_title_screen(username)
    else:
        print("Invalid username or password.")
        login()

# Step 4: Display Game Title Screen
def game_title_screen(username):
    """
    This function displays the game's title screen with options for the user to choose from.
    It allows the user to start the game, change avatar shape, change color, or close the program.
    """
    print(f"Welcome, {username}!")
    print("Title of the Game")
    print("Instructions: Press 'SPACE' to jump over obstacles.")
    print("Settings | Close Program | Start Game | Change Shape | Change Color")
    
    choice = input("Enter choice: ")

    if choice == 'Start Game':
        start_game()
    elif choice == 'Change Shape':
        change_avatar_shape(username)
    elif choice == 'Change Color':
        change_avatar_color(username)
    elif choice == 'Close Program':
        exit_program()
    else:
        print("Invalid choice.")
        game_title_screen(username)

# Step 5: Initialize Game Start Screen
def start_game():
    """
    This function initiates the start of the game by displaying a "READY?" message
    and waiting for the player to press 'SPACE' to begin the game.
    """
    print("READY?")
    input("Press 'SPACE' to start the game!")
    game_loop()

# Step 6: Game Loop
def game_loop():
    """
    This function represents the main game loop. It repeatedly checks for user input, 
    updates the game state, and checks for collisions with obstacles. It keeps track of the score
    and increases obstacle speed as the score increases.
    """
    score = 0
    obstacle_speed = 1  # Speed increases with score
    obstacles = []  # List to store obstacles

    # Add initial obstacles to the list
    for _ in range(3):  # Adding 3 obstacles initially
        obstacles.append(generate_obstacle())

    while True:
        action = input("Press 'SPACE' to jump: ")
        
        if action == "SPACE":
            if input("Press again for Super Jump!") == "SPACE":
                jump("super")
            else:
                jump("regular")
        
        # Check collision with obstacles
        if collision_with_obstacle(obstacles):
            print("Game Over!")
            if input("Play again? (yes/no): ").lower() == "yes":
                start_game()
            else:
                exit_program()
        else:
            score += 1
            obstacle_speed += 0.1  # Increase obstacle speed with score
            print(f"Score: {score}")
        
        # Update obstacles positions (simulate moving obstacles)
        for obstacle in obstacles:
            obstacle['x'] -= obstacle_speed
            if obstacle['x'] < 0:
                obstacle['x'] = random.randint(800, 1200)  # Reset obstacle position to the right

# Step 7: Helper functions
def jump(type):
    """
    This function handles the player's jump based on the type of jump.
    A regular jump or a super jump, depending on user input.
    """
    if type == "regular":
        print("Regular Jump!")
    elif type == "super":
        print("Super Jump!")

def collision_with_obstacle(obstacles): 
    """
    This function simulates collision detection. It checks if any obstacle
    has collided with the player. Returns True if a collision occurs, otherwise False.
    """
    for obstacle in obstacles:
        if obstacle['x'] < 100:  # Assume player is at x = 100 for simplicity
            return True
    return False

def generate_obstacle():
    """
    This function generates an obstacle at a random position to be added to the game.
    """
    return {'x': random.randint(800, 1200), 'y': 550}  # Random x position, fixed y position

def change_avatar_shape(username):
    """
    This function allows the player to change their avatar's shape.
    Currently, it is a placeholder.
    """
    print(f"{username}'s avatar shape changed!")

def change_avatar_color(username):
    """
    This function allows the player to change their avatar's color.
    Currently, it is a placeholder.
    """
    print(f"{username}'s avatar color changed!")

def exit_program():
    """
    This function exits the game, printing a message to the player.
    """
    print("Thanks for playing! Goodbye.")
    exit()

# Databases
user_database = {}  # Dictionary to store user profiles
email_database = {}  # Dictionary to map emails to usernames

# Start the program
start_program()
