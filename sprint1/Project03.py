'''
Created on Feb 5, 2020
@author: Joseph Naiburg, Vincenzo Susi, Timothy Leonard
'''

from prettytable import PrettyTable
import datetime

month_dict = {
        'JAN' : 1,
        'FEB' : 2,
        'MAR' : 3,
        'APR' : 4,
        'MAY' : 5,
        'JUN' : 6,
        'JUL' : 7,
        'AUG' : 8,
        'SEP' : 9, 
        'OCT' : 10,
        'NOV' : 11,
        'DEC' : 12
}

people_dict = {}
fam_dict = {}

def US02(mdate, husbdate, wifedate):
    mdatetemp = mdate.split()
    mday = datetime.date(int(mdatetemp[2]), month_dict[mdatetemp[1]], int(mdatetemp[0]))
    bdatetemphusb = husbdate.split()
    bdatetempwife = wifedate.split()
    wifeday = datetime.date(int(bdatetempwife[2]), month_dict[bdatetempwife[1]], int(bdatetempwife[0]))
    husbday = datetime.date(int(bdatetemphusb[2]), month_dict[bdatetemphusb[1]], int(bdatetemphusb[0]))
    if mday < husbday or mday < wifeday:
        return False
    else:
        return True
    
    
    
def US03(birth, death):
    if(death == 'N/A' or birth == 'N/A'):
        return True
    bd = birth.split()
    dd = death.split()
    bday = datetime.date(int(bd[2]), month_dict[bd[1]], int(bd[0]))
    dday = datetime.date(int(dd[2]), month_dict[dd[1]], int(dd[0]))
    if dday < bday :
        return False
    else:
        return True
    
def US06 (divorce, hdeath, wdeath):
    if((hdeath == 'N/A' and wdeath == 'N/A') or divorce == 'N/A'):
        return True
    divd = divorce.split()
    hdd = hdeath.split()
    wdd = wdeath.split()
    divday = datetime.date(int(divd[2]), month_dict[divd[1]], int(divd[0]))
    hdday = datetime.date(int(hdd[2]), month_dict[hdd[1]], int(hdd[0]))
    wdday = datetime.date(int(wdd[2]), month_dict[wdd[1]], int(wdd[0]))
    if (hdday < divday) or (wdday < divday) :
        return False
    else:
        return True

def run():
    
    #initialize the individual table and family table
    itable = PrettyTable()
    ftable = PrettyTable()
    #open the ged file
    f = open("Project01.ged", "r")
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
                        
                        #make sure birth date is before death date
                        if not US03(bdate, ddate):
                            print("Error: Family with id " + famid + " has a death date before a birth date")
                        
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
                        ftable.add_row([famid, mdate, divorced, husbid, husband, wifeid, wife, children])
                        fam_dict[famid] = [mdate, divorced, husbid, wifeid, children]
                        
                        bdatetemphusb = people_dict[fam_dict[famid][2]][2]
                        bdatetempwife = people_dict[fam_dict[famid][3]][2]
                        
                        #make sure marriage date is after birth date
                        if not US02(mdate, bdatetemphusb, bdatetempwife):
                            print("Error: Family with id " + famid + " has a marriage date before a birth date")
                        if not US06(divorced, people_dict[husbid][5], people_dict[wifeid][5]):
                            print("Error: Family with id " + famid + " has a death date before a divorce date")
                        
                        
                        
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
    ftable.add_row([famid, mdate, divorced, husbid, husband, wifeid, wife, children])
    fam_dict[famid] = [mdate, divorced, husbid, wifeid, children]
    
    bdatetemphusb = people_dict[fam_dict[famid][2]][2]
    bdatetempwife = people_dict[fam_dict[famid][3]][2]
    
    #make sure marriage date is after birth date
    if not US02(mdate, bdatetemphusb, bdatetempwife):
        print("Error: Family with id " + famid + " has a marriage date before a birth date")
    print("Individuals")
    print(itable)
    print("Families")
    print(ftable)
            
        
run()
