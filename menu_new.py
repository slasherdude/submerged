from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub

hub = PrimeHub()

STORAGE_OFFSET = 0

def get_previous_route():
    """Reads the previous route from hub.system.storage."""
    try:
        # Read 1 byte from the specified offset
        data = hub.system.storage(STORAGE_OFFSET, read=1)
        if data:
            return int(data[0])  # Convert byte to integer
        else:
            return 1  # Default to 1 if no data is found
    except ValueError:
        return 1  # Default to 1 if reading fails

def set_previous_route(route):
    """Writes the new previous route to hub.system.storage."""
    try:
        # Write the integer as a single byte to the specified offset
        hub.system.storage(STORAGE_OFFSET, write=bytes([route]))
    except ValueError:
        print("Failed to save the previous route. Ensure route is within valid range.")

previous_route = get_previous_route()

if previous_route == 1:
    selected = hub_menu("2", "3", "4", "5", "6", "7", "1")
elif previous_route == 2:
    selected = hub_menu("3", "4", "5", "6", "7", "1", "2")
elif previous_route == 3:
    selected = hub_menu("4", "5", "6", "7", "1", "2", "3")
elif previous_route == 4:
    selected = hub_menu("5", "6", "7", "1", "2", "3", "4")
elif previous_route == 5:
    selected = hub_menu("6", "7", "1", "2", "3", "4", "5")
elif previous_route == 6:
    selected = hub_menu("7", "1", "2", "3", "4", "5", "6")
elif previous_route == 7:
    selected = hub_menu("1", "2", "3", "4", "5", "6", "7")
else:
    # Default menu if the previous route is invalid or out of bounds
    selected = hub_menu("1", "2", "3", "4", "5", "6", "7")

# Based on the selection, run a program.
if selected == "1":
    import mission1_new
elif selected == "2":
    import mission2_new
elif selected == "3":
    import mission3
elif selected == "4":
    import mission4
elif selected == "5":
    import mission5
elif selected == "6":
    import mission6
elif selected == "7":
    import mission7

# Determine the new route from the selection
new_route = int(selected)

# Save the new route
set_previous_route(new_route)