####################
# General settings #
####################

# The instruction text to display in the beginning
INSTRUCTION_TEXT = """PLEASE READ THESE INSTRUCTIONS CAREFULLY

In this experiment, you will see different shapes on screen. Touching
some shapes will make a happy face appear, touching other shapes will
make a sad face appear. Your task is to get as many happy faces as
possible and as few sad faces.

THE TWO PARTICIPANTS WITH THE HIGHER SCORE (HAPPY FACES MINUS SAD
FACES) WILL RECEIVE A $25 STARBUCKS GIFT CARD.

Make sure to leave your SONA ID to enter the contest.

You may interrupt the experiment at any time without penalty. If you
interrupt, you will still receive course credit, but you will not
enter the gift card contest.

Please press the space bar to start.
"""

FINISH_TEXT = """Thank you for participating in this experiment!

You will now receive an information sheet.
"""

# The font and font size of the INSTRUCTION_TEXT and FINISH_TEXT
TEXTS_FONT = ("Helvetica", 15)

# Initial visibility of mouse pointer (False/True). Can be toggled with <F10>.
HIDE_MOUSE_POINTER = False

# The start (and pause) screen color
START_SCREEN_COLOR_RGB = (255, 192, 203)  # Pink

# The time (in milliseconds) for the black screen after incorrect answer
BLACKOUT_TIME = 3000

# The delay (in milliseconds) after correct answer, before the next stimulus is displayed
DELAY_AFTER_REWARD = 1000


#################################
# Sequence discrimination probe #
#################################

SDP = {
    # The time to display the single stimuli
    "SINGLE_STIMULUS_TIME": 1500,

    # Every n:th trial is a probe trial where n = PROBE_TRIAL_INTERVAL
    "PROBE_TRIAL_INTERVAL": 10,

    # The time to display A when AB is displayed
    "LONG_A_TIME": 4000,

    # The time to display A when aB is displayed
    "SHORT_A_TIME": 1000,

    # The time to display B when aB or AB is displayed
    "B_TIME": 2000,

    # The inter-stimulus time for probes
    "INTER_STIMULUS_TIME": 300,

    # The time (in ms) of delay between the last stimulus disappears until the response buttons appear
    "DELAY": 500
}
