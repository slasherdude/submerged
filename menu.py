from pybricks.tools import hub_menu


# Make a menu to choose a letter. You can also use numbers.
selected = hub_menu("1", "2", "3", "4", "5", "6", "7", "8")

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
elif selected == "8":
    import mission8