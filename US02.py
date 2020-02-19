'''
Created on Feb 5, 2020
@author: Joseph Naiburg
'''

from prettytable import PrettyTable


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

def US02(Hy, Wy, My, Hm, Wm, Mm, Hd, Wd, Md):
    if(My < Wy or My <Hy):
        return False
    elif(My == Hy):
        if(Mm < Hm):
            return False
        elif(Mm == Hm):
            if(Md < Hd):
                return False
    elif(My == Wy):
        if(Mm < Wm):
            return False
        elif(Mm == Wm):
            if(Md < Wd):
                return False
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
                        
                        #getting the marriage date for the family
                        mdatetemp = mdate.split()
                        myear = mdatetemp[2]
                        mmonth = month_dict[mdatetemp[1]]
                        mday = mdatetemp[0]
                        
                        #getting the husbands and wifes bdate
                        bdatetemphusb = people_dict[fam_dict[famid][2]][2].split()
                        bdatetempwife = people_dict[fam_dict[famid][3]][2].split()
                        husbyear = bdatetemphusb[2]
                        husbmonth = month_dict[bdatetemphusb[1]]
                        husbday = bdatetemphusb[0]
                        wifeyear = bdatetempwife[2]
                        wifemonth = month_dict[bdatetempwife[1]]
                        wifeday = bdatetempwife[0]
                        
                        #make sure marriage date is after birth date
                        if not US02(husbyear, wifeyear, myear, husbmonth, wifemonth, mmonth, husbday, wifeday, mday):
                            print("Error: Family with id " + famid + " has a marriage date before a birth date")
                        
                        
                        
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
    mdatetemp = mdate.split()
    myear = mdatetemp[2]
    mmonth = month_dict[mdatetemp[1]]
    mday = mdatetemp[0]
    
    #getting the husbands and wifes bdate
    bdatetemphusb = people_dict[fam_dict[famid][2]][2].split()
    bdatetempwife = people_dict[fam_dict[famid][3]][2].split()
    husbyear = bdatetemphusb[2]
    husbmonth = month_dict[bdatetemphusb[1]]
    husbday = bdatetemphusb[0]
    wifeyear = bdatetempwife[2]
    wifemonth = month_dict[bdatetempwife[1]]
    wifeday = bdatetempwife[0]
    
    #make sure marriage date is after birth date
    if not US02(husbyear, wifeyear, myear, husbmonth, wifemonth, mmonth, husbday, wifeday, mday):
        print("Error: Family with id " + famid + " has a marriage date before a birth date")
    print("Individuals")
    print(itable)
    print("Families")
    print(ftable)
            
        
run()