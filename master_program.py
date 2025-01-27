from pybricks.hubs import PrimeHub
from pybricks.parameters import Button
from pybricks.tools import wait

# Import missions
import mission4
import mission5
# import mission2
# import mission3
# import mission4
# import mission5
# import mission6
# import mission7
# import mission8

# Initialize the Spike Prime Hub
hub = PrimeHub()

# List of missions
missions = [
    mission4.Run,
    mission5.Run
    # mission2.Run,
    # mission3.Run,
    # mission4.Run,
    # mission5.Run,
    # mission6.Run,
    # mission7.Run,
    # mission8.Run,
]

# Variables to track the current mission
current_mission = 0

while True:
    # Display the current mission number (1-based index)
    hub.display.text(str(current_mission + 1))

    # Wait for button press
    while True:
        buttons = hub.buttons.pressed()

        # If the right button is pressed, move to the next mission
        if Button.RIGHT in buttons:
            current_mission = (current_mission + 1) % len(missions)
            break

        # If the left button is pressed, move to the previous mission
        if Button.LEFT in buttons:
            current_mission = (current_mission - 1) % len(missions)
            break

        # If the center button is pressed, run the current mission
        if Button.CENTER in buttons:
            missions[current_mission](hub)
            wait(2000)
            break

        wait(100)