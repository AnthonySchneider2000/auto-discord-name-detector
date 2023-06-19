import pyautogui
import time
import keyboard
import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Define the target pixel color for termination
target_color = (45, 199, 112)  # Green color (adjust to match the desired color)

# Read the dictionary from a file
with open("dictionary.txt", "r") as file:
    dictionary = [word.strip() for word in file.readlines()]

# Function to start the program
def start_program():
    for word in dictionary:
        # Delete the previous word (if any)
        pyautogui.hotkey("ctrl", "a")  # Select the entire word
        pyautogui.press("delete")  # Delete the selected word

        # Logging the current word
        logging.debug(f"Testing username: {word}")

        # Typing the word
        # time.sleep(2)
        pyautogui.typewrite(word)
        logging.debug("Typed the word.")

        

        # Wait for a short delay to allow the page to load
        time.sleep(2)  # Adjust this delay based on your system and page loading time

        # Get the pixel color at the target location
        target_x, target_y = pyautogui.position()
        pixel_color = pyautogui.pixel(target_x, target_y)
        # Get the pixel color at the target location
        target_x, target_y = pyautogui.position()
        pixel_color = pyautogui.pixel(target_x, target_y)

        if pixel_color == target_color:
            logging.debug(f"Username '{word}' is available. Exiting...")
            break
        else:
            logging.debug(f"Username '{word}' is not available.")

        # Continue with the next word

# Define the hotkey combination
hotkey = "ctrl+shift+F12"  # Adjust the hotkey combination to your preference

# Countdown function
def countdown():
    for i in range(3, 0, -1):
        logging.debug(f"Starting in {i} seconds...")
        time.sleep(1)
    start_program()

# Register the hotkey event
keyboard.add_hotkey(hotkey, countdown)

logging.debug("Press the hotkey to start the program.")

# Start listening for keyboard events
keyboard.wait()
