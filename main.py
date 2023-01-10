import os
import re

if __name__ == '__main__':
    # assign directory
    directory = os.getcwd()
    
    subfolders = [ f.path for f in os.scandir(os.getcwd()) if f.is_dir() ]

    for folder in subfolders:
        # iterate over files in
        # that directory

        # Extragem numele folderului
        plate_number = os.path.basename(folder)
        for filename in os.scandir(folder):
            if filename.is_file():
                print(filename.path)

                f = open(filename.path,'r')
                filedata = f.read()
                f.close()

                nr_vehicul = 'nrVehicul="' + plate_number + '"'
                newdata = re.sub('nrVehicul=".*?"', nr_vehicul, filedata)

                f = open(filename.path,'w')
                f.write(newdata)
                f.close()