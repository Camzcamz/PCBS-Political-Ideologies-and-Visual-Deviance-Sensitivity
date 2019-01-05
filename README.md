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
    - [Stimuli Preparation](#Stimuli-Preparation)
        - [Shapes Stimuli] (#Shapes-Stimuli)
        - [Shapes Experimental List](#Shapes-Experimental-List)
        - [Color Stimuli and Experimental List] (#Colors-Stimuli-and-Experimental-List)
        - [Rescale Stimuli](#Color-Stimuli)
    - [Experiment](#Experiment)
    - [Conclusion](#conclusion)
    - [Reference](#reference)

<!-- markdown-toc end -->

## Stimuli Preparation ##

### Shapes Stimuli 
The first step was obtaining by email and renaming the shape stimuli obtainedby Okimoto and colleagues (2015), which was then stored in the Stimuli folder. 
### Shapes Experimental List 
From the Stimuli data file the shapes experimental list was created using ` ` and stored as'Task_Stimuli_Shape.csv'.

### Color Stimuli 
The second step was creating the color stimuli with colors chosen from //www.htmlcsscolor.com/hex/00FF6D based on the experimenter's observation of color ambiguity for red, blue, and green. Saturation and lightness was maintained to focus on sensitivity to hues. The following script `Colors.py` was used to generate the coor stimuli and the second part to create the color experimental list 'Task_Stimuli_Color.csv':

### Rescale Stimuli 
To have the text above the image the stimuli had to be resized. All images were similarly resized with the script `Rescale.py`:

## Experiment
The experiment was run using the following script (`Final_Expyriment.py`), which stored the demographic data for all participants in " demographic.csv " file in Data folder and the image task data for each participant in Data folder.

## Conclusion
In light of my lack knowledge of python prior to this class and its intriduction to me during my first semester of M1, I spent a lot of time this semester working on my project. There are additional things that should be done to improve this experiment and that would have been interesting to code. 

For instance, it would have been interesting to use auditoty typical and deviant stimuli to see if differences in political opinion also influence auditory deviance sensitivity. Moreover, while the perfect red, green and blue were chosen acording to the typical rbg code standards, ambiguous red, green, blue rbg codes were chosen by a single experimenter who personally judged these stimuli as ambiguous. This is not ideal and a scrpit that selects colors based on their distance between well established colors should be used (e.g. selecting color midway between orange and red). This should be done for lightness and saturation too.  

## Reference
Okimoto, T., & M Gromet, D. (2015). Differences in Sensitivity to Deviance Partly Explain Ideological Divides in Social Policy Support. Journal of personality and social psychology. https://doi.org/10.1037/pspp0000080
