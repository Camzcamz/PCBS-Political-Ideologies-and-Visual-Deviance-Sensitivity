### IMPORT PACKAGES ###
import expyriment
from expyriment import design, stimuli, control, io, misc
from expyriment.misc import constants
import pandas as pd
import os.path

### OPEN DATA FILE ###
Stim_Shape = pd.read_csv("Task_Stimuli_Shape.csv")
Stim_Color = pd.read_csv("Task_Stimuli_Colors.csv")

### CREATE NEW DATA FILE FOR DEMOGRAPHIC INFORMATION IN DATA FOLDER ###
DEMO = 'Data/demographics.csv'

### EXPERIMENTAL DESIGN ####
exp = design.Experiment("Task") #create new experiment object by calling expyriment class in submodule design and naming it
control.initialize(exp) #starts countdown, sets up experimental clock, creates the screen (exp.screen), creates and event file (exp.events)and presents the preparing expyriment screen_size
screen_size = exp.screen.surface.get_size() #get_screen size of the screen surface

### INSTRUCTIONS ###
General_Instructions = "This study has two parts. You will have to answer questions using the keyboard for both parts!"
Continue_Instructions = 'Press any key to continue...'
Demographic_Task_Instructions = "In PART 1, you will be asked to answer some general questions about yourself."
Image_Task_Instructions = "In PART 2, you will be asked to judge shapes and colors. Press any key to continue."
Instructions_Shape_Task = "You will be shown several shapes and you will be asked to evaluate each shape. Press any key to start."
Instructions_Color_Task = "You will be shown several colors and you will be asked to evaluate each color. Press any key to start."
Image_Task_Answers = "Please select between 1 and 5, with 1 = definitely yes, 2 = mostly yes, 3  = neither yes nor no,  4 = mostly no, 5 = definitely no."

Question_1 = "Press f if you are a female, m for male, o for other."
Question_2 = "How old are you?"
Answer_Q2 = io.TextInput("") #participant inputs answer using all keyboard keys and presses enter to validate response
Question_3 = "What is you ethinicity?"
Answer_Q_3 = "Press 1 = white, 2 = Asian, 3 = Hispanic, 4 = Black, 5 = Other."
Question_4 = "Politically you consider yourself..."
Question_5 = "Concerning SOCIAL issues, you consider yourself..."
Question_6 = "Concerning ECONOMIC issues, you consider yourself..."
Answer_Q_456 = "Press 1 = extremely liberal, 2 = liberal, 3 = slightly liberal, 4 = moderate, 5 = slightly conservative, 6 = conservative, 7 = extremely conservative."
Question_7 = "What is your employement status?"
Answer_Q_7 = "1= employed, 2 = part-time, 3 = not employed, 4 = retiered, 5 = student."
Question_8 = "What is your highest degree of formal education?"
Answer_Q_8 = "1= Elementary/Primary School, 2 = High School, 3 = University/Undergraduate Degree, 4 = Graduate Degree (Masters, PhD, LLD, MD)."

############# FUNCTIONS ###################
def create_trial(Stimulus, Type, Filenumber):
    trial = design.Trial()
    trial.set_factor("Stimulus", Stimulus)
    trial.set_factor("Type",Type)
    trial.set_factor('Filenumber', int(Filenumber))
    # must write "int" because Filenumber = numpy.float64 due to pandas when 'pandas.read_csv' -
    # wouldn't happen with csv but then would have to deal with generating a header
    # + pandas allows us to use the name rather than the number of columns which is useful to easily extract information and add columns
    Image_Stimulus = 'Stimuli_Resize/{} {} {}.jpg'.format(Stimulus, Type, Filenumber) # each {} is filed by a factor in the presented format () order
    trial.add_stimulus(stimuli.Picture(Image_Stimulus))
    return trial

def stimuli_presentation (screen_size):
    canvas = stimuli.Canvas(size=screen_size) #create canvas that is the the size of the screen/screen surface. Must create new canvas every time or canvases will overwrite themselves (text will become blurry)
    trial.stimuli[0].plot(canvas)
    stimuli.TextScreen(heading = 'Is it a {}?'.format(trial.get_factor('Stimulus')), text = Image_Task_Answers).plot(canvas) # {} replaces by desired factor
    canvas.present() #canvas with trial and text stimuli above will be presented
    key, rt = exp.keyboard.wait(constants.K_ALL_DIGITS)
    exp.data.add([block_name, trial.get_factor('Stimulus'), trial.get_factor('Type'), trial.get_factor('Filenumber'), [chr(key)], key, rt]) #[chr(key)] dont get key number on keyboard but actual number pressed by participant (useful for participants with different keyboards e.g. french/chinese)

############## BLOCKS ##############

### CREATE BLOCKS ###
Shape = expyriment.design.Block(name = "Shape")
Color = expyriment.design.Block(name = "Color")

### INPUT BLOCKS ###
for i in Stim_Shape.index:
    Shape.add_trial(create_trial(Stim_Shape.get_value(i, 'Stimulus'),
                                 Stim_Shape.get_value(i, 'Type'),
                                 Stim_Shape.get_value(i, 'Filenumber')))
                                 # Creates a trial using create_trial function with the value of each factors at passed column and index using the get_value)
                                 # Add these created trials to the Shape Block
Shape.shuffle_trials() #shuffle trials so they appear in a randomized order for each participant
exp.add_block(Shape)

for i in Stim_Color.index:
    Color.add_trial(create_trial(Stim_Color.get_value(i, 'Stimulus'),
                                 Stim_Color.get_value(i, 'Type'),
                                 Stim_Color.get_value(i, 'Filenumber')))
Color.shuffle_trials()
exp.add_block(Color)

####################### START EXPERIMENT ##########f##
expyriment.control.start(skip_ready_screen = True) # asks for subject number available as exp.subject and creates data file available as exp.data
exp.data_variable_names = ["Block", "Stimulus", "Type", "Filenumber", "Key Number", "Key Value", "RT"] #create column variable names for the variables that will be stored in exp.data data file using exp.add

############# PART 1: Demographic Information #############
stimuli.TextScreen(heading = General_Instructions, text = Continue_Instructions).present()
exp.keyboard.wait() #press on any key
stimuli.TextScreen(heading = Demographic_Task_Instructions, text = Continue_Instructions).present()
exp.keyboard.wait()
stimuli.TextScreen(heading = Question_1, text = '').present()
Answer1 = exp.keyboard.wait(constants.K_ALL_LETTERS) #press on any letter key
stimuli.TextScreen(heading = Question_2, text = 'Press spacebar to enter your age (example: 26) and then press enter to move to the next question.').present()
exp.keyboard.wait()
Answer2 = Answer_Q2.get() #get input from io.TextInput("") (example here: numeric age of participant)
stimuli.TextScreen(heading = Question_3, text = Answer_Q_3).present()
Answer3 = exp.keyboard.wait(constants.K_ALL_DIGITS) #press on any digit key
stimuli.TextScreen(heading = Question_7, text = Answer_Q_7).present()
Answer7 = exp.keyboard.wait(constants.K_ALL_DIGITS)
stimuli.TextScreen(heading = Question_8, text = Answer_Q_8).present()
Answer8 = exp.keyboard.wait(constants.K_ALL_DIGITS)

####################### PART 2: IMAGE TASKS ##############################
if exp.subject%2 == 1:
    block_num = "0" # Even participant number
else:
    block_num = "1" # Odd participant number

if block_num == "0":
    stimuli.TextScreen(heading = Question_4, text = Answer_Q_456).present()
    Answer4 = exp.keyboard.wait(constants.K_ALL_DIGITS)
    stimuli.TextScreen(heading = Question_5, text = Answer_Q_456).present()
    Answer5 = exp.keyboard.wait(constants.K_ALL_DIGITS)
    stimuli.TextScreen(heading = Question_6, text = Answer_Q_456).present()
    Answer6 = exp.keyboard.wait(constants.K_ALL_DIGITS)
    stimuli.TextScreen(heading = " Image Task ", text = Image_Task_Instructions).present()
    exp.keyboard.wait()

    if exp.subject%2%2 == 1: # Even participant number/2
        block_name = "Politics Shape Color"
    else: # Odd participant number/2
        block_name = "Politics Color Shape"

    if block_name == "Politics Shape Color":
        stimuli.TextScreen(heading = " Shape Task ", text = Instructions_Shape_Task).present()
        exp.keyboard.wait()
        for trial in Shape.trials:
            stimuli_presentation(screen_size)
        stimuli.TextScreen(heading = " Color Task ", text = Instructions_Color_Task).present()
        exp.keyboard.wait()
        for trial in Color.trials:
            stimuli_presentation(screen_size)

    if block_name == "Politics Color Shape":
        stimuli.TextScreen(heading = " Shape Task ", text = Instructions_Shape_Task).present()
        exp.keyboard.wait()
        for trial in Shape.trials:
            stimuli_presentation(screen_size)
        stimuli.TextScreen(heading = " Color Task ", text = Instructions_Color_Task).present()
        exp.keyboard.wait()
        for trial in Color.trials:
            stimuli_presentation(screen_size)

if block_num == "1":
    stimuli.TextScreen(heading = " Image Task ", text = Image_Task_Instructions).present()
    exp.keyboard.wait()

    if exp.subject%2%2 == 1:
        block_name = "Shape Color Politics"
    else:
        block_name = "Color Shape Politics"

    if block_name == "Shape Color Politics":
        stimuli.TextScreen(heading = " Shape Task ", text = Instructions_Shape_Task).present()
        exp.keyboard.wait()
        for trial in Shape.trials:
            stimuli_presentation(screen_size)
        stimuli.TextScreen(heading = " Color Task ", text = Instructions_Color_Task).present()
        exp.keyboard.wait()
        for trial in Color.trials:
            stimuli_presentation(screen_size)

    if block_name == "Color Shape Politics":
        stimuli.TextScreen(heading = " Color Task ", text = Instructions_Color_Task).present()
        exp.keyboard.wait()
        for trial in Color.trials:
            stimuli_presentation(screen_size)
        stimuli.TextScreen(heading = " Shape Task ", text = Instructions_Shape_Task).present()
        exp.keyboard.wait()
        for trial in Shape.trials:
            stimuli_presentation(screen_size)

    stimuli.TextScreen(heading = Question_4, text = Answer_Q_456).present()
    Answer4 = exp.keyboard.wait(constants.K_ALL_DIGITS)
    stimuli.TextScreen(heading = Question_5, text = Answer_Q_456).present()
    Answer5 = exp.keyboard.wait(constants.K_ALL_DIGITS)
    stimuli.TextScreen(heading = Question_6, text = Answer_Q_456).present()
    Answer6 = exp.keyboard.wait(constants.K_ALL_DIGITS)

######## DEMOGRAPHIC DATA OUTPUT #######
if os.path.isfile(DEMO): # check if it is a file otherwise create it
    demo = pd.read_csv(DEMO)
else:
    demo = pd.DataFrame(columns = ["Subject_ID", "Answer1","Answer2", "Answer3", "Answer4","Answer5","Answer6","Answer7","Answer8"])
    #create file with demographic answers of all participants using key value and not key number

current_subj = pd.DataFrame({"Subject_ID": [exp.subject],
                             "Answer1": [chr(Answer1[0])], # add [chr(    [0])] to get key value not number
                             "Answer2": [chr(Answer3[0])],
                             "Answer3": [chr(Answer3[0])],
                             "Answer4": [chr(Answer4[0])],
                             "Answer5": [chr(Answer5[0])],
                             "Answer6": [chr(Answer6[0])],
                             "Answer7": [chr(Answer7[0])],
                             "Answer8": [chr(Answer8[0])]})
demo = pd.concat([demo, current_subj]) #Link (concatenate) current_subj data frame with demo data frame
demo.to_csv(DEMO, index = False) # False index so index doesn't appear in demographic.csv file stored in the data folder

expyriment.control.end(goodbye_text = "Thank you for participating!", confirmation = False, goodbye_delay = 1000)
