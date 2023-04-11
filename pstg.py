import time
import tkinter as tk

# Define the function to log the sanity of each player
# Define the function to log the sanity of each player and calculate the average sanity of the whole team
def log_sanity():
    # Get the sanity levels of each player from the input fields
    player1_sanity = int(player1_input.get().strip())
    player2_sanity = int(player2_input.get().strip())
    player3_sanity = int(player3_input.get().strip())
    player4_sanity = int(player4_input.get().strip())

    # Calculate the average sanity of the whole team
    avg_sanity = (player1_sanity + player2_sanity + player3_sanity + player4_sanity) / 4

    # Get the current time in hours and minutes
    current_time = time.strftime("%H:%M")

    # Construct the log message with the average sanity
    log_message = f"{current_time} - Sanity levels: {player1_sanity}, {player2_sanity}, {player3_sanity}, {player4_sanity}. Average sanity: {avg_sanity:.2f}"

    # Set the text of the log label to the log message
    log_label.config(text=log_message)

    # Open the log file in append mode and write the log message
    with open("sanity_log.txt", "a") as f:
        f.write(log_message + "\n")

    # Get the sanity levels of each player from the input fields
    player1_sanity = int(player1_input.get().strip())
    player2_sanity = int(player2_input.get().strip())
    player3_sanity = int(player3_input.get().strip())
    player4_sanity = int(player4_input.get().strip())

    # Get the current time in hours and minutes
    current_time = time.strftime("%H:%M")

    # Construct the log message
    log_message = f"{current_time} - Sanity levels: {player1_sanity}, {player2_sanity}, {player3_sanity}, {player4_sanity}"

    # Set the text of the log label to the log message
    log_label.config(text=log_message)

    # Open the log file in append mode and write the log message
    with open("sanity_log.txt", "a") as f:
        f.write(log_message + "\n")

# Create the Tkinter GUI window
window = tk.Tk()
window.title("Phasmophobia Sanity Tracker")

# Create the input fields and labels for the player sanity levels
player1_label = tk.Label(window, text="Player 1 Sanity:")
player1_label.grid(row=0, column=0)
player1_input = tk.Entry(window)
player1_input.grid(row=0, column=1)

player2_label = tk.Label(window, text="Player 2 Sanity:")
player2_label.grid(row=1, column=0)
player2_input = tk.Entry(window)
player2_input.grid(row=1, column=1)

player3_label = tk.Label(window, text="Player 3 Sanity:")
player3_label.grid(row=2, column=0)
player3_input = tk.Entry(window)
player3_input.grid(row=2, column=1)

player4_label = tk.Label(window, text="Player 4 Sanity:")
player4_label.grid(row=3, column=0)
player4_input = tk.Entry(window)
player4_input.grid(row=3, column=1)

# Create the log label
log_label = tk.Label(window, text="")
log_label.grid(row=4, column=0, columnspan=2)

# Create the submit button and bind it to the log_sanity function
submit_button = tk.Button(window, text="Submit", command=log_sanity)
submit_button.grid(row=5, column=0, columnspan=2)

# Start the Tkinter event loop
window.mainloop()
