######## Generate Stimuli Data Files #######
import csv, os, glob

def create_stim_list (filename, stim_path):
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Stimulus", "Type","Filenumber"])
        for filename in glob.glob(stim_path): #Glob does not take regular expressions but takes * which corresponds to 'anything' afterwards
            filename = os.path.basename(filename) # remove folder
            basename, ext = os.path.splitext(filename) # remove extension
            stimuli, type, filenumber = basename.split() # split into 3 columns
            filename = stimuli, type, filenumber
            writer.writerow(filename)

create_stim_list ('Task_Stimuli_Colors.csv', 'Stimuli_Colors/*.jpg')
create_stim_list ('Task_Stimuli_Shapes.csv', 'Stimuli_Shapes/*.jpg')
