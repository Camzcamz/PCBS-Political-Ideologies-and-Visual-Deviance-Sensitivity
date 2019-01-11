AE Project: Political Ideologies and Visual Deviance Sensitivity
============================================================================================
## Introduction 

Okimoto and Gromet's (2015) findings suggests that conservatives show greater sensitivity to deviance than liberals. Specifically, they reported that conservatives were less likely to characterize an ambiguous triangle (or circle, oval, rectangle, square) as being a triangle (or circle, oval, rectangle, square). After inquiring on the participant’s demographic information and political views they presented a picture stimulus (e.g. ‘ambiguous square’ or a ‘perfect square’) with a Likert scale question (e.g. Is it a square? Scale 1 to 5). 

I replicated the experiment to see if the difference in sensitivity to deviance between conservatives and liberals is also true using other stimuli and if the order of inquiring on political opinion influences sensitivity to deviance. In addition to replicating their finding that shape discrimination differs between groups, I will test if color discrimination differs between groups and if the order of political inquiry influences how people categorize colors or shape. 

I have contacted the experimenters and obtained their materials (demographic, political questions, and shape stimuli) as well as created new stimuli (color pictures) using pygame.  All images were resized prior to the experiment to be of similar shape. A paper consent form will be given to the participant before the subject begins the experiment. 

## Research Question: Does political opinion influence our sensitivity to deviance? ##
1.	Does political opinion influence how we distinguish deviance in shape? 
*Hypothesis: Yes, it does when political ideologies are asked before the image task, based on Okimoto and Gromet's (2015) findings.*
2.	Does political opinion influence how we distinguish deviance in colors?
*Hypothesis: If political opinion influences deviance sensitivity, we expect it to generalize to other stimuli than shapes.*
3.	Does political opinion influence how we distinguish deviance in shape or colors only when we are prompt to manifest our political opinions prior to the image deviance judgment task?
*Hypothesis: It may be that political opinion influences deviance sensitivity only when it is consciously brought to mind prior to deviance judgment rather than at all times. This will be the case if there is no difference between groups when they are asked about their political opinion following the stimuli (color or shape) judgment task.*

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Political Ideologies and Visual Deviance Sensitivity](#Political-Ideologies-and-Visual-Deviance-Sensitivity)
    - [Stimuli Preparation](#stimuli-preparation)
        - [Shape Stimuli](#shape-stimuli)
        - [Color Stimuli](#color-stimuli)
        - [Experimental Lists](#experimental-lists)
        - [Rescale Stimuli](#rescale-stimuli)
    - [Experiment](#experiment)
    - [Conclusion](#conclusion)
    - [Reference](#reference)

<!-- markdown-toc end -->

## Stimuli Preparation 

### Shape Stimuli 
The first step was obtaining by email and renaming the shape stimuli obtainedby Okimoto and colleagues (2015), which was then stored in the Stimuli_Shapes folder. 

### Color Stimuli
The second step was creating the color stimuli with colors chosen from //www.htmlcsscolor.com/hex/00FF6D based on the experimenter's observation of color ambiguity for red, blue, and green. Saturation and lightness was maintained to focus on sensitivity to hues. The following script `Colors.py` was used to generate the coor stimuli and the second part to create the color experimental list 'Task_Stimuli_Color.csv':

```
import pygame

## Define color parameters ##
Colors = {'Green Perfect 0':(0, 255, 0), 'Green Ambiguous 0': (0, 255, 176), 'Green Ambiguous 1': (195, 255, 0), 'Green Ambiguous 2': (218, 255, 0), 'Green Ambiguous 3': (0, 255, 109), 'Red Perfect 0':(255,0, 0), 'Red Ambiguous 0':(255,79, 0), 'Red Ambiguous 1':(255,70, 0), 'Red Ambiguous 2':(255,0, 68), 'Red Ambiguous 3':(255,0, 79), 'Blue Perfect 0':(0, 0, 255), 'Blue Ambiguous 0':(0, 255, 244), 'Blue Ambiguous 1':(0, 255, 199), 'Blue Ambiguous 2':(49, 0, 255), 'Blue Ambiguous 3':(82, 0, 255)}

## Define Screen parameters##
W, H = 600, 600

## Define Square parameters ##
width, height = 600, 600
left, top = (W-width)/2, (H-height)/2
SQUARE = pygame.Rect(left, top, width, height) #takes four parameters even if you want a square

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF) # no need her to define BG color or screen.fill( )
for c,v in Colors.items():
    print (c,v)
    pygame.draw.rect(screen, v, SQUARE)# v = color value of specific key
    pygame.image.save(screen, "Stimuli_Colors/%s.jpg" %c) # adds c instead of %s, a dictionary key for a specific v, value
pygame.display.flip() # allows for update of contents of the entire display
```
### Experimental Lists
The third step was generating the experimental lists for each image task: color (Task_Stimuli_Color.csv) and shape (Task_Stimuli_Shape.csv) based on the names of the stimuli using the following script `Exprimental_Lists.py`:

```
import csv, os, glob

with open('Task_Stimuli_Colors.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Stimulus", "Type","Filenumber"])
    for filename in glob.glob('Stimuli_Colors/*.jpg'): #Glob does not take regular expressions but takes * which corresponds to 'anything' afterwards
        filename = os.path.basename(filename) # remove folder
        basename, ext = os.path.splitext(filename) # remove extension
        stimuli, type, filenumber = basename.split() # split into 3 columns
        filename = stimuli, type, filenumber
        writer.writerow(filename)

with open('Task_Stimuli_Shapes.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Stimulus", "Type","Filenumber"])
    for filename in glob.glob('Stimuli_Shapes/*.jpg'): #Glob does not take regular expressions but takes * which corresponds to 'anything' afterwards
        filename = os.path.basename(filename) # remove folder
        basename, ext = os.path.splitext(filename) # remove extension
        stimuli, type, filenumber = basename.split() # split into 3 columns
        filename = stimuli, type, filenumber
```

### Rescale Stimuli 
To have the text above the image the stimuli had to be resized. All images were similarly resized with the script `Rescale.py` and storde in the Stimuli_Resize folder:
```
import glob
import os.path
from PIL import Image
from resizeimage import resizeimage

for image in glob.glob('Stimuli_Colors/*.jpg'): #Glob does not take regular expressions but takes * which corresponds to 'anything' afterwards
    img = Image.open(image)
    img = resizeimage.resize_contain(img, [355, 355]) #resize contain does not crop your image but rescales it while keeping initial proportions to desired scale indicated by [ , ]
    img_output = 'Stimuli_Resize/'+ os.path.basename(image) # store new files in different folder but maintain name by adding basename of initial image path (e.g. initial imag path = 'Stimuli/Red.jpg', basename = 'Red.jpg')
    img.save(img_output, img.format) #save new image with new path and in same format as img (e.g. jpg)


for image in glob.glob('Stimuli_Shapes/*.jpg'): #Glob does not take regular expressions but takes * which corresponds to 'anything' afterwards
    img = Image.open(image)
    img = resizeimage.resize_contain(img, [355, 355]) #resize contain does not crop your image but rescales it while keeping initial proportions to desired scale indicated by [ , ]
    img_output = 'Stimuli_Resize/'+ os.path.basename(image) # store new files in different folder but maintain name by adding basename of initial image path (e.g. initial imag path = 'Stimuli/Red.jpg', basename = 'Red.jpg')
    img.save(img_output, img.format) #save new image with new path and in same format as img (e.g. jpg)
```

## Experiment
The experiment was run using the following script `Experiment.py`, which stored the demographic data for all participants in " demographic.csv " file in Data folder and the image task data for each participant in Data folder.

The experiment had four conditions that differed in order of presentation of the image task and the political ideology questions. Each participant does one of the following conditions, based on their participant number:
(i) political opinion, then shape image task, then color image task 
(ii) political opinion, then color image task, then shape image task 
(iii) shape image task, then color image task, then political opinion
(iv) color image task, then shape image task, then political opinion

```
import expyriment
from expyriment import design, stimuli, control, io, misc
from expyriment.misc import constants
import pandas as pd
import os.path

### OPEN DATA FILE ###
Stim_Shape = pd.read_csv("Task_Stimuli_Shapes.csv")
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
Image_Task_Answer = "Please select between 1 and 5, with 1 = definitely yes, 2 = mostly yes, 3  = neither yes nor no,  4 = mostly no, 5 = definitely no."

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

#### FUNCTION ####
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

def stimulus_question_presentation (Answer):
    canvas = stimuli.Canvas(size=screen_size) #create canvas that is the the size of the screen/screen surface. Must create new canvas every time or canvases will overwrite themselves (text will become blurry)
    trial.stimuli[0].plot(canvas)
    stimuli.TextScreen(heading = 'Is it a {}?'.format(trial.get_factor('Stimulus')), text = Answer).plot(canvas) # {} replaces by desired factor
    canvas.present() #canvas with trial and text stimuli above will be presented
    key, rt = exp.keyboard.wait(constants.K_ALL_DIGITS)
    exp.data.add([block_name, trial.get_factor('Stimulus'), trial.get_factor('Type'), trial.get_factor('Filenumber'), [chr(key)], key, rt]) #[chr(key)] dont get key number on keyboard but actual number pressed by participant (useful for participants with different keyboards e.g. french/chinese)

def political_ideology_questions (Question_A, Question_B, Question_C, Answer_Question):
    stimuli.TextScreen(heading = Question_A, text = Answer_Question).present()
    Answer4 = exp.keyboard.wait(constants.K_ALL_DIGITS)
    stimuli.TextScreen(heading = Question_B, text = Answer_Question).present()
    Answer5 = exp.keyboard.wait(constants.K_ALL_DIGITS)
    stimuli.TextScreen(heading = Question_C, text = Answer_Question).present()
    Answer6 = exp.keyboard.wait(constants.K_ALL_DIGITS)
    return Answer4, Answer5, Answer6

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
    Answer4, Answer5, Answer6 = political_ideology_questions (Question_4, Question_5, Question_6, Answer_Q_456)
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
            stimulus_question_presentation (Image_Task_Answer)
        stimuli.TextScreen(heading = " Color Task ", text = Instructions_Color_Task).present()
        exp.keyboard.wait()
        for trial in Color.trials:
            stimulus_question_presentation (Image_Task_Answer)
    if block_name == "Politics Color Shape":
        stimuli.TextScreen(heading = " Shape Task ", text = Instructions_Shape_Task).present()
        exp.keyboard.wait()
        for trial in Shape.trials:
            stimulus_question_presentation (Image_Task_Answer)
        stimuli.TextScreen(heading = " Color Task ", text = Instructions_Color_Task).present()
        exp.keyboard.wait()
        for trial in Color.trials:
            stimulus_question_presentation (Image_Task_Answer)

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
            stimulus_question_presentation (Image_Task_Answer)
        stimuli.TextScreen(heading = " Color Task ", text = Instructions_Color_Task).present()
        exp.keyboard.wait()
        for trial in Color.trials:
            stimulus_question_presentation (Image_Task_Answer)
    if block_name == "Color Shape Politics":
        stimuli.TextScreen(heading = " Color Task ", text = Instructions_Color_Task).present()
        exp.keyboard.wait()
        for trial in Color.trials:
            stimulus_question_presentation (Image_Task_Answer)
        stimuli.TextScreen(heading = " Shape Task ", text = Instructions_Shape_Task).present()
        exp.keyboard.wait()
        for trial in Shape.trials:
            stimulus_question_presentation (Image_Task_Answer)
    Answer4, Answer5, Answer6 = political_ideology_questions (Question_4, Question_5, Question_6, Answer_Q_456)

######## DEMOGRAPHIC DATA OUTPUT #######
if os.path.isfile(DEMO): # check if it is a file otherwise create it
    demo = pd.read_csv(DEMO)
else:
    demo = pd.DataFrame(columns = ["Subject_ID", "Answer1","Answer2", "Answer3", "Answer4","Answer5","Answer6","Answer7","Answer8"])
    #create file with demographic answers of all participants using key value and not key number

current_subj = pd.DataFrame({"Subject_ID": [exp.subject],
                             "Answer1": [chr(Answer1[0])], # add [chr([0])] to get key value not number
                             "Answer2": (Answer2),
                             "Answer3": [chr(Answer3[0])],
                             "Answer4": [chr(Answer4[0])],
                             "Answer5": [chr(Answer5[0])],
                             "Answer6": [chr(Answer6[0])],
                             "Answer7": [chr(Answer7[0])],
                             "Answer8": [chr(Answer8[0])]})
demo = pd.concat([demo, current_subj]) #Link (concatenate) current_subj data frame with demo data frame
demo.to_csv(DEMO, index = False) # False index so index doesn't appear in demographic.csv file stored in the data folder

expyriment.control.end(goodbye_text = "Thank you for participating!", confirmation = False, goodbye_delay = 1000)
```
## Conclusion
In light of my lack knowledge of python prior to this class and its introduction during my first semester of M1, I spent a lot of time this semester working on my project. There are additional things that should be done to improve this experiment and that would have been interesting to code. 

For instance, it would have been interesting to use auditory perfect and deviant stimuli to see if differences in political opinion also influence auditory deviance sensitivity. Moreover, while the perfect red, green and blue were chosen acording to the typical rbg code standards, ambiguous red, green, blue rbg codes were chosen by a single experimenter who personally judged these stimuli as ambiguous. This is not ideal and a script that selects colors based on their distance between well established colors should be used (e.g. selecting color midway between orange and red). This should be done for lightness and saturation too. Finally, statistical analyses were not coded but could have been done on python.

## Reference
Okimoto, T., & M Gromet, D. (2015). Differences in Sensitivity to Deviance Partly Explain Ideological Divides in Social Policy Support. Journal of personality and social psychology. https://doi.org/10.1037/pspp0000080
