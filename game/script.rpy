init:
    $ config.screen_width = 800
    $ config.screen_height = 600
    $ config.window_title = "Samsara Staffing Services - Intake Survey"
    $ default player_name = "New Employee"
    $ default player_day = "Day"
    $ default player_time = "Time"

label start:
    $ save_name = "BOOT UP"
    "Welcome to Samsara Staffing Services."
    "You are about to begin a short survey so we can get a better understanding of who you are."
    "Answer each question as truthfully as possible."
    "The survey will begin momentarily."

label question_1:
    $ save_name = "QUESTION 1"
    "Question 1."
    "What is your preferred name?"
    $ player_name = renpy.input("Type your name here.")

label question_2:
    $ save_name = "QUESTION 2"
    "Question 2."
    "How did you hear about us?"
    menu:
        "referral":
            pass
        "previous employer":
            pass
        "academic supervisor":
            pass
        "written correspondence":
            pass
        "I was listed.":
            pass

label question_3:
    $ save_name = "QUESTION 3"
    "Question 3."
    "What are the best days to reach you?"
    $ player_day = renpy.input("Enter which days you are available.")

label question_4:
    $ save_name = "QUESTION 4"
    

