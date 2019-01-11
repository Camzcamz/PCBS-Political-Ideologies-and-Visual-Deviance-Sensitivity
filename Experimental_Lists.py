######## Generate Stimuli Data Files #######
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
        writer.writerow(filename)
