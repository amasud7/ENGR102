########################
#### STUDY ANALYZER ####
########################

# Read in session data
# present summary of program
print("This program calculates the amount of \ time you studied for various exams")

# Loop until done entering study sessions
more_to_enter = True
names = []
lengths = []
while more_to_enter: 
    # Get test name
    test_name = input("Enter which test you studied for. \ Enter NONE to stop: ")
    if test_name == "NONE":
        more_to_enter = False
    # get session length
    if more_to_enter:
        study_length = int(input("Enter how many minutes you \ studied in this session: "))

        names.append(test_name)
        lengths.append(study_length)


# Process user queries
# Loop until done entering test names
more_to_enter = True
while more_to_enter:
    # get test name
    test_name = input("Whihc test do you want \ data for? Enter NONE to stop: ")
    if test_name == "NONE":
        more_to_enter = False
        break

    # process data
    # make list of times that match test name
    studylengths = []
    for i in range(len(names)):
        if (test_name == names[i]):
            studylengths.append(lengths[i])
    # get statistics
    num_sessions = len(studylengths)
    total_time = 0
    for i in studylengths:
        total_time += i

    # Present results
    print("You studied for", test_name, "in", num_sessions, "sessions, for", total_time, "minutes")
