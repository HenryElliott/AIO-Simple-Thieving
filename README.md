# AIO-Simple-Thieving

This is a Python script that automates the process of thieving in a specific game using mouse automation and a graphical user interface (GUI). The script clicks on specified coordinates on the screen in intervals and logs its actions in a GUI window. You can control the script using a hotkey (`Ctrl+Shift+C`) to start and stop the automation.

## Features

- **Start/Stop Automation**: Use the `Ctrl+Shift+C` hotkey to start and stop the script.
- **Status Tracking**: View the current status (Running/Stopped) and the elapsed time of the script in real-time.
- **Action Logging**: The script logs its actions in a text area within the GUI, providing information on each click made by the automation.
- **Graphical User Interface (GUI)**: A modern Discord-like theme with custom fonts and a clean layout.
- **Randomized Clicks**: The script adds small randomization to mouse movements to avoid detection or repetitive patterns.
  
## Requirements

To run this script, you will need the following libraries installed:

- `pyautogui`: For automating mouse movements and clicks.
- `keyboard`: To capture hotkeys for controlling the script.
- `tkinter`: For creating the GUI.
- `threading`: For running the script in a separate thread to avoid blocking the main program.

You can install the required libraries using `pip`:

tkinter is usually included in standard Python installations, but if you don't have it, you can install it using the following command (for Ubuntu-based systems):
sudo apt-get install python3-tk

How It Works
The script uses pyautogui to simulate mouse movements and clicks at specific coordinates on the screen. The coordinates are defined as coords_1 and coords_2.
The script runs in a loop, clicking at coords_1 for 28 iterations and then at coords_2 after that. There is a 1.5-second pause between each click.
The script starts and stops using a hotkey combination (Ctrl+Shift+C). When running, the script shows the elapsed runtime in the GUI and logs every action it performs.
The script uses a simple GUI created with tkinter, which includes:
A status label (showing "Running" or "Stopped")
A runtime label (showing elapsed time)
A log area for displaying actions taken
A start/stop button that also works via the hotkey.

Usage
Running the Script:

After running the script, a GUI window will appear.
The script starts automatically when the hotkey Ctrl+Shift+C is pressed.
Stopping the Script:

Press Ctrl+Shift+C again to stop the script.
The status will update, and the script will stop clicking.
Exit the Program:

Press Esc on your keyboard to exit the program.
Example Output
When the script is running, you will see the following outputs:

In the GUI:

The status will show "Running" and the elapsed time will count up.
The log will display the coordinates where the script clicked.
In the console:

You will see messages like Mouse clicked at: (625, 248) showing the coordinates where the script is clicking.
Customization
You can change the coordinates coords_1 and coords_2 in the script to match the areas you want to automate.
The sleep time between clicks can also be adjusted by modifying the random_sleep function parameters.
