import time
import sys
from pip._vendor.msgpack.fallback import xrange
from random import choice

responses = ["Magic 8 Ball: Have you tried using a banana?",
             "Magic 8 Ball: Yes.",
             "Magic 8 Ball: No.",
             "Magic 8 Ball: Perhaps.",
             "Magic 8 Ball: Improper shaking, please try again.",
             "Magic 8 Ball: ...Sorry, I didn't catch that.",
             "Magic 8 Ball: Are you sure you want to ask that? :)",
             "Magic 8 Ball: IDK.",
             "Magic 8 Ball: Be yourself.",
             "Magic 8 Ball: Feed me please I haven't eaten in months."]
quit = False  # Setup for quit option
while not quit:
    quitresponse = False
    quitinput = ''
    questionmark = False
    while not questionmark:  # Checks to see if there is a question mark
        question = input("Please ask a question:\n")  # Allow the user to input their question.
        if "?" in question:
            questionmark = True
        else:
            print("This is not a question.")
    # Show an in progress message
    toolbar_width = 40
    print("Magic 8 Balling in progress, do not disturb.")
    sys.stdout.write("[%s]" % (" " * toolbar_width))  # setup toolbar
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in xrange(toolbar_width):
        time.sleep(0.2)  # Amount of pause between update
        # Updates the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n")  # This ends the progress bar
    print(choice(responses))  # Randomizes responses
    while not quitresponse:  # Allow the user to ask another question/advice or quit the game
        quitinput = input('Would you like to ask the Magic 8 Ball again?\n [Yes] \n [No] \n')
        if str(quitinput.lower()) in ('yes',
                                      'no'):
            if str(quitinput.lower()) in 'yes':
                quit = False
                quitresponse = True
            else:
                quit = True
                quitresponse = True
                print("Magic 8 Ball: Goodbye...")
        else:
            print('Invalid response')
