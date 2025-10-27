'''
This Capstone Project is Passion Project Idea Generator. This program
helps students come up with creative and personalized passion project
ideas based on their interests and time availability. It uses user
input, conditionals, loops, and functions to produce a unique result
for any user with any kind of passion.
'''

def welcome_message(): # CS Part 1, Unit 3 -- functions
    # displaying welcome message to user
    print("Welcome to the Passion Project Idea Generator!")
    print("This tool will help you find a creative passion project idea based on your interests and time availability.")
    print("Let's get started!")
    print()

def get_user_input(): # CS Part 1, Unit 4 -- user input
    # collecting user information
    # CS Part 1, Unit 3 -- variables
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    print()
    print("Select your area of interest from the list below:")

    # CS Part 2, Unit 2 -- list
    # list for user to choose from
    subjects = ["Math", "Science", "English", "World Language", "History", 
                "Sports", "Music", "Computer Science", "Technology"]

    # CS Part 1, Unit 2 -- for loop
    # printing list
    for subject in subjects:
        print("- " + subject)

    # displaying user interest to console
    subject_interest = input("Your interest: ").strip().title()
    
    # CS Part 1, Unit 4 -- conditionals (while loop)
    while subject_interest not in subjects: # CS Part 1, Unit 6 - comparison operators
        subject_interest = input("Please choose a valid subject from the list: ").strip().title()

    # asking user how much time they have for the project
    duration = input("Would you prefer a short or long project? (short/long): ").strip().lower()
    while duration != "short" and duration != "long":
        duration = input("Please enter 'short' or 'long': ").strip().lower()

    # returning multiple values based on user input
    return name, age, subject_interest, duration

# CS Part 2, Unit 1 -- returning values within function
# function returns a project idea based on the subject and duration
def generate_project_idea(subject, duration): # CS Part 1, Unit 4 -- function parameters
    
    # CS Part 1, Unit 4 -- conditionals
    # project is found (generated) based on user's responses
    if subject == "Math":
        if duration == "short":
            return ["Math Puzzle Video", "1-2 weeks", "Create a video explaining and solving a unique math puzzle."]
        else:
            return ["Math in Real Life Blog", "4-6 weeks", "Start a blog that shows how math is used in daily life."]
    elif subject == "Science":
        if duration == "short":
            return ["DIY Science Experiment", "1-2 weeks", "Conduct and document a simple experiment using household items."]
        else:
            return ["Sustainability Research Project", "4-6 weeks", "Research and propose a sustainability solution."]
    elif subject == "English":
        if duration == "short":
            return ["Poetry Zine", "1-2 weeks", "Write a collection of poems and design a small zine."]
        else:
            return ["Short Story Series", "4-6 weeks", "Write and self-publish a short story series."]
    elif subject == "World Language":
        if duration == "short":
            return ["Language Learning Tips Reel", "1-2 weeks", "Create a video with tips for learning a language."]
        else:
            return ["Culture Exchange Blog", "4-6 weeks", "Interview native speakers and write about their culture."]
    elif subject == "History":
        if duration == "short":
            return ["Historical Figure Profile", "1-2 weeks", "Create an infographic or video about a historical figure."]
        else:
            return ["Local History Podcast", "4-6 weeks", "Produce a podcast episode on local history."]
    elif subject == "Sports":
        if duration == "short":
            return ["Fitness Challenge Plan", "1-2 weeks", "Design a 7-day fitness challenge and share with friends."]
        else:
            return ["Student Athlete Interviews", "4-6 weeks", "Create a docuseries interviewing student athletes."]
    elif subject == "Music":
        if duration == "short":
            return ["Cover Song Recording", "1-2 weeks", "Record and post a creative cover of a favorite song."]
        else:
            return ["Original Music Album", "4-6 weeks", "Write and record a short original EP (2–3 songs)."]
    elif subject == "Computer Science":
        if duration == "short":
            return ["Mini Game in Python", "1-2 weeks", "Create a text-based or simple graphical mini-game."]
        else:
            return ["Build a Website or App", "4-6 weeks", "Create a website or app to solve a real-world problem."]
    elif subject == "Technology":
        if duration == "short":
            return ["Tech Review Video", "1-2 weeks", "Record and edit a review of a favorite piece of tech."]
        else:
            return ["Tech for Good Research Project", "4-6 weeks", "Propose a tech solution to a social issue."]

# displaying user and project info to conosole
def display_project(name, project_info):

    # CS Part 2, Unit 2 -- indexing
    title = project_info[0]
    time_estimate = project_info[1]
    description = project_info[2]

    print()
    # using concatenation
    print("Thanks, " + name + "! Based on your interests, here's a passion project idea for you:")
    print()
    
    # summary of project
    print("Project Title: " + title)
    print("Estimated Time: " + time_estimate)
    print("Description: " + description)

# encouraging closing function that motivates the user
def closing_message(): # CS Part 1, Unit 3 -- function
    print()
    print("Good luck on your passion project journey!")
    print("Remember, your passion can lead to purpose. You've got this!")

# main function that runs program in a structured method
def main():
    welcome_message()
    name, age, subject, duration = get_user_input()  # Unit 2 (Part 2): UNPACKING
    project_info = generate_project_idea(subject, duration)
    display_project(name, project_info)
    closing_message()

# calling main function
main()
