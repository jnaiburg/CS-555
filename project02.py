'''
Created on Feb 5, 2020

@author: Joseph Naiburg
'''
valid = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS",
         "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE",
         "HEAD", "TRLR", "NOTE"]

def isValid(s):
    if s in valid:
        return True
    else:
        return False

def run():
    f = open("Project01.ged", "r")
    for x in f:
        temp = x.split()
        print("-->" + ' '.join(temp))
        
        level = temp[0]
        
        if(len(temp) < 3):
            tag = temp[1]
            arguments = ''
        elif(temp[2] == "INDI" or temp[2] == "FAM"):
            tag = temp[2]
            arguments = temp[1]
        else:       
            tag = temp[1]
            arguments = ' '.join(temp[2:])
            
        if isValid(tag):
            valid = "Y"
        else:
            valid = "N"
            
        if((level == '1' and tag == 'DATE') or (level == '2' and tag == 'NAME')):
            valid = "N"
        
        print("<--" + level + "|" + tag + "|" + valid + "|" + arguments)
        
run()
        
 
