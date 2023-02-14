#=====importing libraries===========
content = "" #define the variable
user_file = open('user.txt','r+')
#====Login Section====
valid_usernames =[] #define the list

for line in user_file:
    content = content + line # build up the text lines
    content2 = content.replace(",", "") # removes the comma
    variables = line.split() # turns the text on each line into individual strings
    valid_usernames.append(variables[0]) # a list of valid usernames is created by adding each variable in position 0 on each line.

while True:
    input_username = input("Enter your username: ")
    input_username = str(input_username.lower()+",") # a comma is added for the input to be compared to the 'valid_usernames' list as each username is followed by a comma in the text file.
    if input_username in valid_usernames: # if the input matches the list of accepted usernames, the loop breaks.
        break
    else:
        print("Incorrect username.Please try again.") # if the input doesn't match the list of accepted usernames, it disaplays an error and asks again for a username input by repeating the loop.
        continue

while True:
    input_password = input("Enter your password: ")
    input_password = str(input_password.lower())
    check = input_username + input_password # to check if the password matches the username
    check2 = check.replace(",", " ")
    if check2 in content2: # if the username input and password input matches the data on of the content lines, then the loop breaks.
        break
    else:
        print("Incorrect password.Please try again.") # if not, it repeats the loop and asks again for a password input.
        continue
print("\n")

#====Functions Section====

# define the function to register a user
def reg_user(x):
    allowed = "admin,"
    # only the admin is allowed to register new users
    # if the string x where x = input_username matches the 'allowed' string, then the condition takes place
    if x == allowed:
        while True:
            new_username = input("Enter new username: ").lower()
            new_username_2 = str(new_username.lower()+",") # a comma is added for the input to be compared to the 'valid_usernames' list as each username is followed by a comma in the text file.
            if new_username_2 in valid_usernames:
            # if the input matches the list of existent usernames, an error message is displayed, and the loop occurs until a not already registered username is the input.
                print("This username is already registered. Please add an user with a different username.")
                continue
            else:
                break
        new_password = input("Enter new password: ").lower()
        confirmation = input("Confirm your password: ").lower()
        # if the two string inputs don't match, the user is asked to confirm the password again.
        if confirmation != new_password:
            print("It does not match your password. Please try again.")
            confirmation = input("Confirm your password: ").lower()
        new_content = new_username + "," + " " + new_password
        # the new content is saved in the format the user text file is following (username, password)
        user_file.write("\n" + new_content)
    # if the string x where x = input_username doesn't match the 'allowed' string, then an attention message is displayed to inform the user.
    elif x != allowed:
        print("\n" + "ATTENTION: Only the admin is allowed to register a new user." + "\n")


#define the function to add a new task
def add_task():
    tasks_file = open('tasks.txt', 'a')
    task_person = input("Enter the username of the person whom the task is assigned to: ").lower()
    task_title = input("Enter the task title: ")
    task_description = input("Enter the task description: ")
    task_deadline = input("Enter the task due date: ")
    task_status = "No"
    current_date = "30 Jan 2023"
    new_task = task_person + "," + " " + task_title + "," + " " + task_description + "," + " " + current_date + "," + " " + task_deadline + "," + " " + task_status
    tasks_file.write("\n" + new_task) 
    # the new task information is added to the tasks text file following the above structure.
    tasks_file.close()


# define the function to view all the tasks
def view_all():
    tasks_file = open('tasks.txt', 'r')
    data = tasks_file.readlines()
    for pos, line in enumerate(data, 1):
        # enumerate counts the lines and displays the number of that line. 
        # It increases every time a new line is read.
        split_data = line.split(", ")
        output = f"___________________[Task {pos}]______________________\n\n"
        output += f"Task:\t\t\t{split_data[1]}\n"
        output += f"Assigned to:\t\t{split_data[0]}\n"
        output += f"Date assigned:\t\t{split_data[4]}\n"
        output += f"Due date:\t\t{split_data[3]}\n"
        output += f"Task Complete?:\t\t{split_data[5]}\n"
        output += f"Task description:\n\t{split_data[2]}"
        output += "\n"
        output += f"_______________________________________________\n"
        print(output)
    tasks_file.close()


#define the function to view all the tasks that have been assigned to the logged in user
def view_mine():
    tasks_file = open('tasks.txt', 'r')
    data = tasks_file.readlines()
    for pos, line in enumerate(data, 1): 
    # enumerate counts the lines and displays the number of that line. 
    # It increases every time a new line is read.
        if input_username in line:
            split_data = line.split(", ")
            output = f"_____________________[Task {pos}]___________________________\n\n"
            output += f"Task:\t\t\t{split_data[1]}\n"
            output += f"Assigned to:\t\t{split_data[0]}\n"
            output += f"Date assigned:\t\t{split_data[4]}\n"
            output += f"Due date:\t\t{split_data[3]}\n"
            output += f"Task Complete?:\t\t{split_data[5]}\n"
            output += f"Task description:\n\t{split_data[2]}"
            output += "\n"
            output += f"_________________________________________________________\n"
            print(output)
    while True:
        output += f"_______________________________________________\n"
        output = f"Select one of the following options below:\n"
        output += f"1 - Select a Task number\n"
        output += f"-1 - Return to main menu\n"
        output += f"_______________________________________________\n"

        choice = int(input(output))
        if choice == -1:
        # if the user enters '-1' the while loop breaks and the user is displayed with the main menu.
            break
        elif choice == 1:
            task_choice = int(input("Type in Task Number: ")) - 1 # we need to substract 1 as we start counting the tasks from 1, not 0
            if task_choice < 0 or task_choice > len(data):
            # the task numbers start from 1 so anything less than that would be an error.
            # anything bigger than the total amount of tasks would be an error too.
                print("This is not a valid Task number. Please try again.")
                continue
            edit_data = data[task_choice] # the data in the choice index position
            #print(edit_data)
            # the data in the choice index position is printed.
            while True:
                output += f"_______________________________________________\n"
                output = f"Select one of the following options below:\n"
                output += "-1 - Return to task number\n"
                output += "1 - Mark the task as complete\n"
                output += "2 - Edit the task\n"
                output += f"_______________________________________________\n"

                choice = int(input(output))
                if choice < -1 or choice == 0 or choice >= 3:
                    print("You have selected an invalid option. Please try again.")
                    continue

                if choice == -1:
                    break

                elif choice == 1:
                    split_data = edit_data.split(", ")
                    split_data[-1] = "Yes\n" # changes the last element in the list from 'No' to 'Yes'
                    new_data = ", ".join(split_data)
                    data[task_choice] = new_data

                    tasks_write = open('tasks.txt', 'w')
                    for line in data:
                        tasks_write.write(line)
                    tasks_write.close()
                    break

                elif choice == 2:
                    split_data = edit_data.split(", ")
                    if split_data[-1] == "Yes\n":
                        print("This task has already been completed and therefore can't be edited anymore.\n")
                        break
                    while True:
                            output += f"_______________________________________________\n"
                            output = f"Select one of the following options below:\n"
                            output += "-1 - Return to edit options\n"
                            output += "1 - Edit the username of the person the task is assigned to\n"
                            output += "2 - Edit the task due date\n"
                            output += f"_______________________________________________\n"

                            choice = int(input(output))
                            if choice < -1 or choice == 0 or choice >= 3:
                                print("You have selected an invalid option. Please try again.")
                                continue

                            if choice == -1:
                                break

                            elif choice == 1:
                                split_data[0] = input("Enter new username: ")
                                new_data = ", ".join(split_data)
                                data[task_choice] = new_data

                                tasks_write = open('tasks.txt', 'w')
                                for line in data:
                                    tasks_write.write(line)
                                tasks_write.close()
                                break

                            elif choice == 2:
                                split_data[-2] = input("Enter new due date in the format '12 Jan 2023': ")
                                new_data = ", ".join(split_data)
                                data[task_choice] = new_data

                                tasks_write = open('tasks.txt', 'w')
                                for line in data:
                                    tasks_write.write(line)
                                tasks_write.close()
                                break
            tasks_file.close()

#define function to generate reports

def generate_reports():
        tasks_file = open('tasks.txt', 'r')
        data = tasks_file.readlines()
        num_tasks = 0
        output = ""
        user_output = ""
        completed = 0
        incompleted = 0
        overdue = 0
        completed_total = 0
        for line in enumerate(data):
            num_tasks += 1
        for line in data:
            split_data = line.split(", ")
            if split_data[-1] == "Yes\n":
                completed_total += 1
            if split_data[-1] == "No\n":
                incompleted += 1
            import datetime
            due_date = split_data[-2]
            # assign the date format to convert a string into a datetime
            due_date_format = "%d %b %Y"
            due_date_obj = datetime.datetime.strptime(due_date, due_date_format)
            # if the due date is before today's date aka less than today's date
            # and the task hasn't been completed, then the task is overdue
            if due_date_obj < datetime.datetime.today():
                overdue += 1
        # define the dictionary task_count
        # the values stored in the dictionary show how many tasks are assigned to each user
        task_count = {}
        for line in data:
            task_info = line.strip().split(",")
            username = task_info[0]
            # if the username is already in the dictionary, the count increases by 1
            if username in task_count:
                task_count[username] += 1
            # otherwise a new key username is added to the dictionary
            else:
                task_count[username] = 1

        # opens the user_overview text file and writes new information
        user_overview_write = open('user_overview.txt', 'w')
        user_output = f"The total number of users registered is: {len(valid_usernames)}.\n"
        user_output += f"The total number of tasks generated is: {num_tasks}.\n"
        user_overview_write.write(user_output)
        user_overview_write.close()

        # opens the user_overview text file and appends new information
        user_overview_write = open('user_overview.txt', 'a')
        user_output_2 = "\n"
        for user in task_count:
            user_output_2 += f"{user} has been assigned: {task_count[user]} tasks.\n"
        user_overview_write.write(user_output_2)
        user_overview_write.close()

        task_count_percentage = task_count
        # update all values in the task_count_percentage dictionary to display the percentage
        # of the total number of tasks that have been assigned to that user
        task_count_percentage.update((x, y / num_tasks * 100) for x, y in task_count.items())

        # define the completed_count dictionary
        # the values stored in the dictionary show how many tasks each user has completed
        completed_count = {}
        for line in data:
            task_info = line.strip().split(",")
            username = task_info[0]
            if username in completed_count:
                if task_info[-1] == " Yes":
                    completed_count[username] += 1
            else:
                if task_info[-1] == " Yes":
                    completed_count[username] = 1
                else:
                    completed_count[username] = 0

        # define a new function that calculates the percentage of
        # the total number of tasks that have been completed by the user

        def dict_percentage (d1, d2):
            d3 = dict()
            for k in d1:
                if k in d2:
                    d3[k] = d1[k] / d2[k] * 1000
            return d3

        # define a new function that calculates the percentage of
        # the total number of tasks that have not been completed by the user yet

        def incomplete_dict (d1):
            d2 = dict()
            for k in d1:
                d2[k] = 100 - d1[k]
            return d2

        completed_count_percentage = dict_percentage(completed_count, task_count)
        incompleted_tasks_percentage = incomplete_dict(completed_count_percentage)

        # define the incompleted_count dictionary
        # the values stored in the dictionary show how many tasks each user has not completed and are overdue
        incompleted_count = {}
        for line in data:
            task_info = line.strip().split(",")
            username = task_info[0]
            if username in incompleted_count:
                if task_info[-1] == " No":
                    import datetime
                    user_due_date = task_info[-2]
                    user_due_date_format = " %d %b %Y"
                    user_due_date_obj = datetime.datetime.strptime(user_due_date, user_due_date_format)
                    if user_due_date_obj < datetime.datetime.today():
                        incompleted_count[username] += 1
            else:
                if task_info[-1] == " No":
                    incompleted_count[username] = 1
                    import datetime
                    user_due_date = task_info[-2]
                    user_due_date_format = " %d %b %Y"
                    user_due_date_obj = datetime.datetime.strptime(user_due_date, user_due_date_format)
                    if user_due_date_obj > datetime.datetime.today():
                        incompleted_count[username] -= 1
                else:
                    incompleted_count[username] = 00

        # calculate the percentage of the total number of tasks that are incomplete and overdue
        overdue_tasks_percentage = dict_percentage(incompleted_count, task_count)

        import math
        # calculates the percentage of incompleted tasks
        incomplete_percentage = math.ceil(incompleted / num_tasks * 100)
        # calculates the percentage of overdue tasks
        overdue_percentage = math.ceil(overdue / num_tasks * 100)

        # opens the task_overview text file and writes new information
        task_overview_write = open('task_overview.txt', 'w')
        output += f"The total number of tasks generated is: {num_tasks}.\n"
        output += f"The total number of completed tasks is: {completed_total}.\n"
        output += f"The total number of incompleted tasks is: {incompleted}.\n"
        output += f"The total number of incompleted tasks that are overdue is: {overdue}.\n"
        output += f"The percentage of tasks that are incomplete is: {incomplete_percentage}%.\n"
        output += f"The percentage of tasks that are incomplete and overdue is: {incomplete_percentage}%.\n"
        task_overview_write.write(output)
        task_overview_write.close()


        # opens the user_overview text file and appends new information
        user_overview_write = open('user_overview.txt', 'a')
        user_output_3 = "\n"
        for user in task_count_percentage:
            user_output_3 += f"{user} has been assigned: {task_count_percentage[user]}% of the total tasks.\n"
        user_output_3 += "\n"
        for user in completed_count_percentage:
            user_output_3 += f"{user} has completed: {completed_count_percentage[user]}% of their tasks.\n"
        user_output_3 += "\n"
        for user in incompleted_tasks_percentage:
            user_output_3 += f"{user} still has to complete: {incompleted_tasks_percentage[user]}% of their tasks.\n"
        user_output_3 += "\n"
        for user in overdue_tasks_percentage:
            user_output_3 += f"{user} has: {overdue_tasks_percentage[user]}% of their tasks that are incomplete and overdue.\n"
        user_overview_write.write(user_output_3)
        user_overview_write.close()

        tasks_file.close()



# define a function to read the first few lines from a text file
def read_first_lines(filename, limit):
    result = []
    with open(filename, 'r') as input_file:
        for line_number, line in enumerate(input_file):
            if line_number > limit:
                break
            result.append(line)
    return result

# define a function that turns a list into a string
def list_to_string(s):
    string = ""
    for element in s:
        string += element
    return string

#====Menu Section====

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        reg_user(input_username)

    elif menu == 'a':
        pass
        add_task()

    elif menu == 'va': # display the information for each task.
        pass
        view_all()

    elif menu == 'vm': # display the task information for the user that is currently logged in.
        pass
        view_mine()

    elif menu == 'ds': # this menu option displays the total number of tasks and the total number of users
        allowed = "admin," # only the admin is allowed to display statistics
        if allowed == input_username: # if the string input_username matches the 'allowed' string, then the condition takes place
            # automatically generates reports in case the user hasn't done so yet.
            generate_reports()
            f = open('task_overview.txt', 'r')
            f2 = open('user_overview.txt', 'r')
            task_overview = f.read()
            print("_______________________________________________\n")
            print(task_overview)
            print("_______________________________________________\n")
            # display the first two lines of text from the user_overview text file
            # using the 'read_first_lines' function
            first_lines = read_first_lines('user_overview.txt', 1)
            # turn the list into a string so it can be displayed as text on the screen
            first_lines_2 = list_to_string(first_lines)
            print(first_lines_2)
            print("_______________________________________________\n")
            f3 = open('tasks.txt', 'r')
            # create a list with the users that have been assigned a task
            tasks_file = open('tasks.txt', 'r')
            data = tasks_file.readlines()
            task_count = {}
            for line in data:
                task_info = line.strip().split(",")
                username = task_info[0]
                # if the username is already in the dictionary, the count increases by 1
                if username in task_count:
                    task_count[username] += 1
                # otherwise a new key username is added to the dictionary
                else:
                    task_count[username] = 1
            # from the task_count dictionary
            # create a list with all the users that have been allocated a task
            users_with_tasks = list(task_count.keys())

            max_users = len(users_with_tasks)

            # define a function to read lines from a text file
            # that only contain the user in a given index position
            def read_data(i):
                user = users_with_tasks[i]
                f = open('user_overview.txt', 'r')
                s = f.readlines()
                result = ""
                for line in s:
                    if user in line:
                        result = result + line
                print(result)

            # as long as i is less than the total amount of users in the users_with_tasks list
            # the loop will take place
            # and the function read_data will be activated
            i = 0
            while i < max_users:
                read_data(i)
                print("_______________________________________________\n")
                i += 1

            f.close()
            f2.close()
            tasks_file.close()
        elif allowed != input_username: # if the string input_username doesn't match the 'allowed' string, then an attention message is displayed to inform the user.
            print("\n" + "ATTENTION: Only the admin is allowed to display statistics." + "\n")
    
    elif menu == 'gr':
        generate_reports()


    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
    user_file.close()