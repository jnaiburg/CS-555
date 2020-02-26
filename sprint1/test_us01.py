import unittest 
from datetime import datetime
from US01 import run

class TestUS01(unittest.TestCase):

  def getTodayIntArrDate(self):
    ret = []
    now = datetime.now()
    ret.append(now.day)
    ret.append(now.month)
    ret.append(now.year)
    return ret
  #returns array of ddmmyyy integers
  def strToIntArrDate(self, date):
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
    
  #check if any marriage date is less than or equal to today's date
  def test_marriage(self):
    ret = True
    today = self.getTodayIntArrDate()
    ftable = run()[1]
    for row in ftable:
      row.border = False
      row.header = False
      dateNums = self.strToIntArrDate(row.get_string(fields=['Married']).strip())
      if(dateNums[2] > today[2]):
        ret = False
        break
      elif(dateNums[2] == today[2]):
        if(dateNums[1] > today[1]):
            ret = False
            break
        elif(dateNums[1] == today[1]):
           if(dateNums[0] > today[0]):
            ret = False
            break
    self.assertTrue(ret)

    #check if any marriage date is less than or equal to today's date
  def test_divorce(self):
    ret = True
    today = self.getTodayIntArrDate()
    ftable = run()[1]
    for row in ftable:
      row.border = False
      row.header = False
      col = row.get_string(fields=['Divorced']).strip()
      if(col != 'N/A'):
        dateNums = self.strToIntArrDate(col)
        if(dateNums[2] > today[2]):
          ret = False
          break
        elif(dateNums[2] == today[2]):
          if(dateNums[1] > today[1]):
              ret = False
              break
          elif(dateNums[1] == today[1]):
            if(dateNums[0] > today[0]):
              ret = False
              break
    self.assertTrue(ret)


  def test_birthday(self):
    ret = True
    today = self.getTodayIntArrDate()
    itable = run()[0]
    for row in itable:
      row.border = False
      row.header = False
      dateNums = self.strToIntArrDate(row.get_string(fields=['Birth Date']).strip())
      if(dateNums[2] > today[2]):
        ret = False
        break
      elif(dateNums[2] == today[2]):
        if(dateNums[1] > today[1]):
            ret = False
            break
        elif(dateNums[1] == today[1]):
           if(dateNums[0] > today[0]):
            ret = False
            break
    self.assertTrue(ret)

  def test_death(self):
    ret = True
    today = self.getTodayIntArrDate()
    itable = run()[0]
    for row in itable:
      row.border = False
      row.header = False
      col = row.get_string(fields=['Death Date']).strip()
      if(col != 'N/A'):
        dateNums = self.strToIntArrDate(col)
        if(dateNums[2] > today[2]):
          ret = False
          break
        elif(dateNums[2] == today[2]):
          if(dateNums[1] > today[1]):
              ret = False
              break
          elif(dateNums[1] == today[1]):
            if(dateNums[0] > today[0]):
              ret = False
              break
    self.assertTrue(ret)



  def test_bad_birthday(self):
    ret = True
    today = self.getTodayIntArrDate()
    itable = run()[0]
    itable.add_row(['@I1@', 'Tim Leonard', 'M', '6 MAY 2020', '20', 'True', 'N/A', 'N/A', 'N/A'])
    for row in itable:
      row.border = False
      row.header = False
      dateNums = self.strToIntArrDate(row.get_string(fields=['Birth Date']).strip())
      if(dateNums[2] > today[2]):
        ret = False
        break
      elif(dateNums[2] == today[2]):
        if(dateNums[1] > today[1]):
            ret = False
            break
        elif(dateNums[1] == today[1]):
           if(dateNums[0] > today[0]):
            ret = False
            break
    self.assertFalse(ret)
  


  
if __name__ == '__main__':
    unittest.main()

