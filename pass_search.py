# Miles Histand

# This program will search for the username of a specific site entered by user


import sys
import re

def user_search(site):
    x = open('/Volumes/Disk Image/list.txt','r')
    y = x.readlines()
    Argument = 0
    for line in y:
        z = re.split(',',line)
        website = z[0]
        user = z[1]
        password = z[2]
        password = password.strip()
        if site == website:
            print 'user:',user
            print 'password:',password
            Argument = 1
            
    if not Argument:
         print 'No such site (do not include .com in string)'
        
def main():
    user_search(sys.argv[1])
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
