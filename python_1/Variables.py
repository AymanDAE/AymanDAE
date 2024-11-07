# Step 1: Start the Program
def start_program():
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
    print(f"Welcome, {username}!")
    print("Title of the Game")
    print("Instructions: Press 'SPACE' to jump over obstacles.")
    print("Settings | Close Program | Start Game | Change Shape | Change Color")
    choice = input("Enter choice: ")

    if choice == 'Start Game':
        start_game()
    elif choice == 'Change Shape':
        "change_avatar_shape"(username)
    elif choice == 'Change Color':
          "change_avatar_color"(username)
    elif choice == 'Close Program':
        exit_program()
    else:
        print("Invalid choice.")
        game_title_screen(username)

# Step 5: Initialize Game Start Screen
def start_game():
    print("READY?")
    input("Press 'SPACE' to start the game!")
    game_loop()

# Step 6: Game Loop
def game_loop():
    score = 0
    obstacle_speed = 1  # Speed increases with score
    
    while True:
        action = input("Press 'SPACE' to jump: ")
        if action == "SPACE":
            if input("Press again for Super Jump!") == "SPACE":
                jump("super")
            else:
                jump("regular")
        
        # Check collision with obstacle
        if collision_with_obstacle():
            print("Game Over!")
            if input("Play again? (yes/no): ").lower() == "yes":
                start_game()
            else:
                exit_program()
        else:
            score += 1
            obstacle_speed += 0.1  # Increase obstacle speed with score
            print(f"Score: {score}")

# Step 7: Helper functions
def jump(type):
    if type == "regular":
        print("Regular Jump!")
    elif type == "super":
        print("Super Jump!")

def collision_with_obstacle(): 
    # Simulate collision detection
    return False  # Change to True to simulate a collision

def exit_program():
    print("Thanks for playing! Goodbye.")
    exit()

# Databases
user_database = {}
email_database = {}

# Start the program
start_program()
