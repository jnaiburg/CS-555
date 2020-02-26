'''
Created on Feb 19, 2020
@author: Joseph Naiburg, Tim Leonard
'''

#Dates (birth, marriage, divorce, death) should not be after the current date
from datetime import datetime
from prettytable import PrettyTable

people_dict = {}
fam_dict = {}

def strToIntArrDate(date):
    ret = []
    ddmmyyyy = date.split(' ')
    ret.append(int(ddmmyyyy[0]))
    if(ddmmyyyy[1] == 'JAN'):
      ret.append(1)
    elif(ddmmyyyy[1] == 'FEB'):
      ret.append(2)
    elif(ddmmyyyy[1] == 'MAR'):
      ret.append(3)
    elif(ddmmyyyy[1] == 'APR'):
      ret.append(4)
    elif(ddmmyyyy[1] == 'MAY'):
      ret.append(5)
    elif(ddmmyyyy[1] == 'JUN'):
      ret.append(6)
    elif(ddmmyyyy[1] == 'JUL'):
      ret.append(7)
    elif(ddmmyyyy[1] == 'AUG'):
      ret.append(8)
    elif(ddmmyyyy[1] == 'SEP'):
      ret.append(9)
    elif(ddmmyyyy[1] == 'OCT'):
      ret.append(10)
    elif(ddmmyyyy[1] == 'NOV'):
      ret.append(11)
    elif(ddmmyyyy[1] == 'DEC'):
      ret.append(12)
    else:
      ret.append(13) #will never be < self.month
    ret.append(int(ddmmyyyy[2]))
    return ret
#d1 marriage date, d2 divorce date
def compareDates(d1, d2):

  if(d1 == 'N/A' and d2 == 'N/A'):
    return True
  elif(d1 != 'N/A' and d2 == 'N/A'):
    return True
  elif(d1 == 'N/A' and d2 != 'N/A'):
    return False
  else:
    d1_int = strToIntArrDate(d1)
    d2_int = strToIntArrDate(d2)
    if(d2_int[2] > d1_int[2]):
          return False
    elif(d2_int[2] == d1_int[2]):
      if(d2_int[1] > d1_int[1]):
        return False
      elif(d2_int[1] == d1_int[1]):
        if(d2_int[0] > d1_int[0]):
          return False
  return True


def run():
    #initialize the individual table and family table
    itable = PrettyTable()
    ftable = PrettyTable()
    #open the ged file
    f = open("../gedcom.ged", "r")
    #make the columns for the itable
    itable.field_names = ['ID', 'Name', 'Gender', 'Birth Date', 'Age', 'Alive', 'Death Date', 'Child', 'Spouse']
    ftable.field_names = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
    #initialize a bunch of variables
    indi = ''
    name = ''
    sex = ''
    bdate = ''
    ddate = 'N/A'
    age = ''
    alive = 'True'
    child = 'N/A'
    spouse = 'N/A'
    isindi = True
    
    famid = ''
    mdate='N/A'
    divorced='N/A'
    husbid=''
    wifeid=''
    husband = ''
    wife = ''
    children = []
    
    
    
    byear = 0
    
    #iterate through each line
    for x in f:
        #split by space
        temp = x.split()
        #id 0
        if temp[0] == '0':
            
            if(len(temp) > 2):
                #new person
                if temp[2] == 'INDI':
                    if indi != '':
                        #add the row of info for the previous guy to the itable
                        itable.add_row([indi, name, sex, bdate, age, alive, ddate, child, spouse])
                        people_dict[indi] = [name, sex, bdate, age, alive, ddate, child, spouse]
                        ddate = 'N/A'
                        alive = 'True'
                        child = 'N/A'
                        spouse = 'N/A'
                        #get the new id for the next guy
                    indi = temp[1]
                if temp[2] == 'FAM':
                    if isindi:
                        itable.add_row([indi, name, sex, bdate, age, alive, ddate, child, spouse])
                        people_dict[indi] = [name, sex, bdate, age, alive, ddate, child, spouse]
                        isindi = False
                    else:
                        if children == []:
                            children = 'N/A'
                        if(not compareDates(mdate, divorced)):
                          raise SyntaxError('Cannot have a divorce date earlier than marriage date')
                        ftable.add_row([famid, mdate, divorced, husbid, husband, wifeid, wife, children])
                        fam_dict[famid] = [mdate, divorced, husbid, wifeid, children]
                        children = []
                    famid = temp[1] 
                        
        #id 0
        if temp[0] == '1':
            #the persons name
            if temp[1] == 'NAME':
                name = temp[2] + ' ' + temp[3]
            #their gender
            if temp[1] == 'SEX':
                sex = temp[2]
            #make a variable to know that the next line is the birthday
            if temp[1] == 'BIRT':
                dtype = 'birth' 
            #same but with death date
            if temp[1] == 'DEAT':
                dtype = 'death'
            
            if temp[1] == 'HUSB':
                husband = people_dict[temp[2]][0]
            
            if temp[1] == 'WIFE':
                wife = people_dict[temp[2]][0]    
            
            if temp[1] == 'MARR':
                dtype = 'marr'
            if temp[1] == 'DIV':
                dtype = 'divorce'
            
            if temp[1] == 'FAMC':
                child = temp[2]
            if temp[1] == 'FAMS':
                spouse = temp[2]
            
            if temp[1] == 'HUSB':
                husbid = temp[2]
                        
            if temp[1] == 'WIFE':
                wifeid = temp[2]
            if temp[1] == 'CHIL':
                children.append(temp[2])
        
        #id 2 
        if temp[0] == '2':
            #figuring out death vs birth date and storing it to a variable
            if temp[1] == 'DATE':
                dtemp = temp[2] + ' ' + temp[3] + ' ' + temp[4]
                if dtype == 'birth':
                    bdate = dtemp
                    byear = int(temp[4])
                    #age in 2020
                    age = 2020 - byear
                if dtype == 'death':
                    alive = 'False'
                    ddate = dtemp
                    #age at time of death
                    age = int(temp[4]) - byear
                if dtype == 'marr':
                    mdate = dtemp
                if dtype == 'divorce':
                    divorced = dtemp
    #add the last row and print stuff
    if(not compareDates(mdate, divorced)):
      raise SyntaxError('Cannot have a divorce date earlier than marriage date')
    ftable.add_row([famid, mdate, divorced, husbid, husband, wifeid, wife, children])
    # print("Individuals")
    # print(itable)
    # print("Families")
    # print(ftable)
    return [itable, ftable]
            
if __name__ == '__main__':
    run()
