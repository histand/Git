# Miles Histand


import sys
import re
import os
import csv

def main():
    arg = 3       # column to extract

    w = open('/Users/histand/Desktop/outfile.csv','w')

    for csvFiles in os.listdir("/Users/histand/Desktop/Data"):
        
        
        if csvFiles.startswith("."):
            continue
        
        reader = csv.reader(open('/Users/histand/Desktop/Data/'+csvFiles,'r'))
            
        for row in reader:
            column=0
            for x in range (0,5):
                y = row[column]                        # desired column to store
                print y                                # print column as a check
                y = y.translate(None,' ')              # remove spaces
                if re.search('j',y) != None:           # operate on any js
                    y = y.translate(None,'j')          # remove j
                    y = list(y)                        # convert argument to a list
                    y.append('j')                      # add j to the list at end
                    y = "".join(y)                     # join into one string
                y = y.strip()                          # remove any \n or stuff
                w.write(y)                             # write out to file
                if column != 4:
                    w.write(',')                       # add comma for next cell
                column=column+1                        # go to next column
            w.write('\n')                           # go to new line after last column

    w.close()                                         # close written file

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
