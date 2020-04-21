'''
Created on Feb 5, 2020
@author: Joseph Naiburg, Vincenzo Susi, Timothy Leonard
'''

from prettytable import PrettyTable
import datetime
from dateutil import relativedelta

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

#part of US01
def getCurrentDate():
    ret = []
    now = datetime.datetime.today()
    ret.append(now.day)
    ret.append(now.month)
    ret.append(now.year)
    return ret
#part of US01
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

#checks date
def US01(d):
    today = getCurrentDate()
    if(d == 'N/A'):
        return True
    else:
        dateNums = strToIntArrDate(d)
        if(dateNums[2] > today[2]):
            return False
        elif(dateNums[2] == today[2]):
            if(dateNums[1] > today[1]):
                return False
            elif(dateNums[1] == today[1]):
                if(dateNums[0] > today[0]):
                    return False
    return True

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

#d1 marriage date, d2 divorce date
def US04(d1, d2):
    if(d1 == 'N/A' and d2 == 'N/A'):
        return True
    elif(d1 != 'N/A' and d2 == 'N/A'):
        return True
    elif(d1 == 'N/A' and d2 != 'N/A'):
        return False
    else:
        d1_int = strToIntArrDate(d1)
        d2_int = strToIntArrDate(d2)
        if(d2_int[2] < d1_int[2]):
            return False
        elif(d2_int[2] == d1_int[2]):
            if(d2_int[1] < d1_int[1]):
                return False
            elif(d2_int[1] == d1_int[1]):
                if(d2_int[0] < d1_int[0]):
                    return False
    return True


def US05(mdate, husbdate, wifedate):
    if husbdate == "N/A" and wifedate == 'N/A':
        return True

    mdatetemp = mdate.split()
    mday = datetime.date(int(mdatetemp[2]), month_dict[mdatetemp[1]], int(mdatetemp[0]))
    ddatetemphusb = husbdate.split()
    ddatetempwife = wifedate.split()
    if wifedate != 'N/A':
        wifeday = datetime.date(int(ddatetempwife[2]), month_dict[ddatetempwife[1]], int(ddatetempwife[0]))
        if mday > wifeday:
            return False
    if husbdate != 'N/A':
        husbday = datetime.date(int(ddatetemphusb[2]), month_dict[ddatetemphusb[1]], int(ddatetemphusb[0]))
        if mday > husbday:
            return False
    return True

def US06 (divorce, hdeath, wdeath):
    if (hdeath == 'N/A' and wdeath == 'N/A'):
        return True

    if (divorce == 'N/A'):
        return True

    divd = divorce.split()
    divday = datetime.date(int(divd[2]), month_dict[divd[1]], int(divd[0]))

    if (wdeath != 'N/A'):
        wdd = wdeath.split()
        wdday = datetime.date(int(wdd[2]), month_dict[wdd[1]], int(wdd[0]))
        if(wdday < divday):
            return False

    if (hdeath != 'N/A'):
        hdd = hdeath.split()
        hdday = datetime.date(int(hdd[2]), month_dict[hdd[1]], int(hdd[0]))
        if (hdday < divday):
            return False

    return True

# not older than 150
def US07(bdate):
    bdate_num = strToIntArrDate(bdate)
    today = getCurrentDate()
    year_diff = today[2] - bdate_num[2]
    if (year_diff > 150):
        return False
    elif(year_diff == 150):
        if(bdate_num[1] > today[1]):
            return False
        else:
            if(bdate_num[2] >= today[2]):
                return False
            else:
                return True
    else:
        return True

def US08(bdate, mdate, ddate):
    if mdate == 'N/A':
        return False

    mdatetemp = mdate.split()
    bdatetemp = bdate.split()

    mday = datetime.date(int(mdatetemp[2]), month_dict[mdatetemp[1]], int(mdatetemp[0]))
    bday = datetime.date(int(bdatetemp[2]), month_dict[bdatetemp[1]], int(bdatetemp[0]))

    if bday < mday:
        return False
    if ddate != 'N/A':
        ddatetemp = ddate.split()
        dday = datetime.date(int(ddatetemp[2]), month_dict[ddatetemp[1]], int(ddatetemp[0]))
        if (bday - dday).days > 280:
            return False
    return True

#Born before death of parents
def US09(mom, dad, birth):
    if birth == 'N/A':
        return True
    if mom == 'N/A' and dad == 'N/A':
        return True

    bd = birth.split()
    birthday = datetime.date(int(bd[2]), month_dict[bd[1]], int(bd[0]))

    if mom == 'N/A' or dad == 'N/A':
        if mom == 'N/A':
            dd = dad.split()
            dadDay = datetime.date(int(dd[2]), month_dict[dd[1]], int(dd[0]))
            dadDay = dadDay + relativedelta.relativedelta(months=9)
            if (birthday > dadDay):
                return False
        if dad == 'N/A':
            md = mom.split()
            momDay = datetime.date(int(md[2]), month_dict[md[1]], int(md[0]))
            if (birthday > momDay):
                return False
        return True

    md = mom.split()
    dd = dad.split()
    momDay = datetime.date(int(md[2]), month_dict[md[1]], int(md[0]))
    dadDay = datetime.date(int(dd[2]), month_dict[dd[1]], int(dd[0]))
    dadDay = dadDay + relativedelta.relativedelta(months=9)
    if (birthday > momDay) or (birthday > dadDay):
        return False

    return True

# not married before 14
def US10(mdate, bdate):
    if mdate == 'N/A':
        return True
    num_mdate = strToIntArrDate(mdate)
    num_bdate = strToIntArrDate(bdate)
    age = num_mdate[2] - num_bdate[2]
    if num_mdate[1] <= num_bdate[1] and num_mdate[2] <= num_bdate[2]:
        age = age + 1
    if(age < 14):
        return False
    else:
        return True

def US11(marriage2, divorce, spousedeath):
    mtemp = marriage2.split()
    mday = datetime.date(int(mtemp[2]), month_dict[mtemp[1]], int(mtemp[0]))

    if divorce != 'N/A':
        dtemp = divorce.split()
        dday = datetime.date(int(dtemp[2]), month_dict[dtemp[1]], int(dtemp[0]))
        if dday > mday:
            return False
        else:
            return True
    elif spousedeath != 'N/A':
        dtemp = spousedeath.split()
        dday = datetime.date(int(dtemp[2]), month_dict[dtemp[1]], int(dtemp[0]))
        if dday > mday:
            return False
        else:
            return True
    else:
        return False

#Parents not too old (mom < 60 years older than children, dad < 80)
def US12(momAge, dadAge, childAge):
    if ((momAge - childAge >= 60) or (dadAge - childAge >= 80)):
        return False
    return True

#each sibling is born at least 9 months after the previous
def US13(birth_dates):
  for i in range(len(birth_dates)):
    for j in range(len(birth_dates)):
      if i != j:
        d1 = strToIntArrDate(birth_dates[i])
        d2 = strToIntArrDate(birth_dates[j])
        d1m = 12*d1[2] + d1[1]
        d2m = 12*d2[2] + d2[1]
        if not abs(d1m - d2m) >= 9:
          return False
  return True


#no more than 5 kids in one family can have the same birthday
def US14(birth_dates):
    for x in birth_dates:
        if birth_dates.count(x) > 5:
            return False
    return True

#Fewer than 15 siblings (returns false if 15 or more)
def US15(children):
    if (children == 'N/A'):
        return True
    if (len(children) >= 15):
        return False
    return True

def US16(husband, wife):
  hl = husband.split(' ')[1]
  wl = wife.split(' ')[1]
  return hl == wl


#returns false if marriage to a descendant
def US17(husband, wife, children):
    if husband in children:
        return False
    if wife in children:
        return False
    return True


#Siblings should not marry (returns false if at least two are married)
def US18(children):
    if (children == 'N/A'):
        return True
    if (len(children) <= 1):
        return True
    for i in range(len(children)):
        if (people_dict[children[i]][7] == 'N/A'):
            continue
        for j in range(i + 1, len(children)):
            if (people_dict[children[i]][7] == people_dict[children[j]][7]):
                return False
    return True

def US21(husb, wife): # Correct gender for role
    if husb != 'M':
        return False
    if wife != 'F':
        return False
    return True

def US24(husb1, wife1, mdate1, husb2, wife2, mdate2): # Unique family by spouse
    if husb1 == husb2 and wife1 == wife2:
        if mdate1 == mdate2:
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
                # new person
                if temp[2] == 'INDI':
                    if indi != '':
                        # add the row of info for the previous guy to the itable
                        if(not US01(bdate) or not US01(ddate)):
                            raise SyntaxError('Dates must be today or earlier')

                        itable.add_row([indi, name, sex, bdate, age, alive, ddate, child, spouse])
                        people_dict[indi] = [name, sex, bdate, age, alive, ddate, child, spouse]
                        ddate = 'N/A'
                        alive = 'True'
                        child = 'N/A'
                        spouse = 'N/A'

                        # make sure birth date is before death date
                        if not US03(bdate, ddate):
                            print("Error: Family with id " + famid + " has a death date before a birth date")
                        if not US07(bdate):
                            print("Error: Family with id " + famid + " "+ bdate + "is older than 150")
                        # get the new id for the next guy
                    indi = temp[1]
                if temp[2] == 'FAM':
                    if isindi:
                        if(not US01(bdate) or not US01(ddate)):
                            raise SyntaxError('Dates must be today or earlier')

                        itable.add_row([indi, name, sex, bdate, age, alive, ddate, child, spouse])
                        people_dict[indi] = [name, sex, bdate, age, alive, ddate, child, spouse]
                        isindi = False
                    else:
                        if children == []:
                            children = 'N/A'

                        if(not US01(mdate) or not US01(divorced)):
                            raise SyntaxError('Dates must be today or earlier')

                        if(not US04(mdate, divorced)):
                            raise SyntaxError('Cannot have a divorce date earlier than marriage date')

                        bdatetemphusb = people_dict[husbid][2]
                        bdatetempwife = people_dict[wifeid][2]

                        ddatetemphusb = people_dict[husbid][5]
                        ddatetempwife = people_dict[wifeid][5]

                        for family in fam_dict:
                            if family[2] == husbid:
                                if not (US11(mdate, family[1], ddatetempwife) and US11(family[1], divorced, people_dict[family[3]][5])):
                                    print("Error: " + husbid + " cannot be married to two wives at the same time")
                            if family[3] == wifeid:
                                if not (US11(mdate, family[1], ddatetemphusb) and US11(family[1], divorced, people_dict[family[2]][5])):
                                    print("Error: " + wifeid + " cannot be married to two husbands at the same time")
                            if not(US24(husband, wife, mdate, people_dict[fam_dict[family][2]][0], people_dict[fam_dict[family][3]][0], family[0])):
                                print("Error: family with id " + famid + " does not have a unique family by spouses")

                        ftable.add_row([famid, mdate, divorced, husbid, husband, wifeid, wife, children])
                        fam_dict[famid] = [mdate, divorced, husbid, wifeid, children]

                        child_bdatelist = []

                        for child in children:
                            bdatechild = people_dict[child][2]
                            if not US08(bdatechild, mdate, divorced):
                                print("Error: family with id " + famid + "has a birth date for a child not within the marriage")
                            if not US09(people_dict[wifeid][5], people_dict[husbid][5], bdatechild):
                                print("Error: Child with id " + child + " has a birth date after the death of his parents")
                            if not US12(people_dict[wifeid][3], people_dict[husbid][3], people_dict[child][3]):
                                print("Error: Child with id " + child + " has parents that are too old")
                            child_bdatelist.append(bdatechild)
                        if not US13(child_bdatelist):
                            print("Error two children born withing 9 months of each other in family " + famid)
                        if not US14(child_bdatelist):
                            print("Error: More than 5 children in family " + famid + " are born on the same day")

                        # make sure marriage date is after birth date
                        if not US02(mdate, bdatetemphusb, bdatetempwife):
                            print("Error: Family with id " + famid + " has a marriage date before a birth date")
                        if not US05(mdate, ddatetemphusb, ddatetempwife):
                            print("Error: Family with id " + famid + " has a marriage date after a death date")
                        if not US06(divorced, people_dict[husbid][5], people_dict[wifeid][5]):
                            print("Error: Family with id " + famid + " has a death date before a divorce date")
                        # Checks for fewer than 15 children in a family
                        if not US15(children):
                            print("Error: Family with id " + famid + " has 15 or more siblings")
                        if not US16(husband, wife):
                            print("Error husband and wife do not share the husband's last name")
                        #check that marriage is not to children
                        if not US17(husbid, wifeid, children):
                            print("Error: Cannot marry children")
                        # Checks that siblings aren't married
                        if not US18(children):
                            print("Error: Family with id " + famid + " has siblings who are married to each other")
                        # Checks that spouses have correct genders
                        if not US21(people_dict[fam_dict[famid][2]][1], people_dict[fam_dict[famid][3]][1]):
                            print("Error: Family with id " + famid + " doesn't have correct genders for roles")


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

    if(not US01(mdate) or not US01(divorced)):
        raise SyntaxError('Dates must be today or earlier')

    if(not US04(mdate, divorced)):
        raise SyntaxError('Cannot have a divorce date earlier than marriage date')

    ftable.add_row([famid, mdate, divorced, husbid, husband, wifeid, wife, children])
    fam_dict[famid] = [mdate, divorced, husbid, wifeid, children]
    bdatetemphusb = people_dict[husbid][2]
    bdatetempwife = people_dict[wifeid][2]

    ddatetemphusb = people_dict[husbid][5]
    ddatetempwife = people_dict[wifeid][5]

    #make sure marriage date is after birth date
    if not US02(mdate, bdatetemphusb, bdatetempwife):
        print("Error: Family with id " + famid + " has a marriage date before a birth date")
    if not US05(mdate, ddatetemphusb, ddatetempwife):
        print("Error: Family with id " + famid + " has a marriage date after a death date")
    if not US06(divorced, people_dict[husbid][5], people_dict[wifeid][5]):
        print("Error: Family with id " + famid + " has a death date before a divorce date")
    if not US10(mdate, people_dict[fam_dict[famid][2]][2]):
        print("Error: Family with id " + famid + " has a marriage before 14")
    if not US10(mdate, people_dict[fam_dict[famid][3]][2]):
        print("Error: Family with id " + famid + " has a marriage before 14")
    if not US15(children):
        print("Error: Family with id " + famid + " has 15 or more siblings")
    if not US18(children):
        print("Error: Family with id " + famid + " has siblings who are married to each other")
    if not US21(people_dict[fam_dict[famid][2]][1], people_dict[fam_dict[famid][3]][1]):
        print("Error: Family with id " + famid + " doesn't have correct genders for roles")

    print("Individuals")
    print(itable)
    print("Families")
    print(ftable)

run()