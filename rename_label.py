import sys
import os
import fileinput

label_path = os.path.join('data', 'annotations', 'labels')
files = os.listdir(label_path)
print(files)

for file in files:
    if file == '.DS_Store':
        continue
    print(os.path.join('.',label_path, file))
    #for i, line in enumerate(fileinput.input(os.path.join('.',label_path, file), inplace=1)):
    for i, line in enumerate(fileinput.input(os.path.join('.',label_path, file), inplace=1)):
                #print(i, line)
                print(line.replace('SFI', 'SVE').replace('SFF', 'SVE').replace('SFL', 'SVE').replace('SNI', 'SVE').replace('SNF', 'SVE').replace('SNL', 'SVE').replace('HNL', 'GSL').replace('HFL', 'GSL').replace('HNR', 'GSR').replace('HFR', 'GSR'), end='')
    # replace all occurrences of 'sit' with 'SIT' and insert a line after the 5th
    #for i, line in enumerate(fileinput.input(os.path.join(label_path, file), inplace=1)):
    #    print(i, line)
     #   sys.stdout.write(line.replace('SFI', 'SVE').replace('SFF', 'SVE').replace('SFL', 'SVE').replace('SNI', 'SVE').replace('SNF', 'SVE').replace('SNL', 'SVE').replace('HNL', 'GSL').replace('HFL', 'GSL').replace('HNR', 'GSR').replace('HFR', 'GSR'))  # replace 'sit' and write


