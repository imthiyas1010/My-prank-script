import time
import os

# Function to create a fake "hacking" effect
def fake_hack():
    os.system("clear")  # Clears the terminal
    print("Initializing...")
    time.sleep(1)
    print("Connecting to target device...")
    time.sleep(2)
    print("Accessing system files...")
    time.sleep(2)
    print("Injecting payload...")
    time.sleep(2)
    print("\n⚠️ SYSTEM ERROR! Unauthorized access detected! ⚠️")
    time.sleep(2)
    print("\nJust Kidding! 😂 It’s a prank!")

# Run the prank
fake_hack()
