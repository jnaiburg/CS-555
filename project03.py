'''
Created on Feb 5, 2020

@author: Joseph Naiburg
'''

from prettytable import PrettyTable



valid = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS",
         "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE",
         "HEAD", "TRLR", "NOTE"]


def isValid(s):
    if s in valid:
        return True
    else:
        return False

def run():
    itable = PrettyTable()
    ftable = PrettyTable()
    f = open("Project01.ged", "r")
    itable.field_names = ['ID', 'Name', 'Gender', 'Birth Date', 'Death Date', 'Age']
    indi = ''
    name = ''
    sex = ''
    bdate = ''
    ddate = 'N/A'
    age = ''
    
    byear = 0
    
    for x in f:
        temp = x.split()
        if temp[0] == '0':
            
            if(len(temp) > 2):
                if temp[2] == 'INDI':
                    if indi != '':
                        itable.add_row([indi, name, sex, bdate, ddate, age])
                        ddate = 'N/A'
                    indi = temp[1]
         
        if temp[0] == '1':
            if temp[1] == 'NAME':
                name = temp[2] + ' ' + temp[3]
            if temp[1] == 'SEX':
                sex = temp[2]
            if temp[1] == 'BIRT':
                dtype = 'birth' 
            if temp[1] == 'DEAT':
                dtype = 'death'
                
        if temp[0] == '2':
            if temp[1] == 'DATE':
                dtemp = temp[2] + ' ' + temp[3] + ' ' + temp[4]
                if dtype == 'birth':
                    bdate = dtemp
                    byear = int(temp[4])
                    age = 2020 - byear
                if dtype == 'death':
                    ddate = dtemp
                    age = int(temp[4]) - byear
                
    print(itable)
            
        
run()
        
 
