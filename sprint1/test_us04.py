import unittest 
from US04 import run

class TestUS04(unittest.TestCase):
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

  #d1 marriage date, d2 divorce date
  def compareDates(self, d1, d2):

    if(d1 == 'N/A' and d2 == 'N/A'):
      return True
    elif(d1 != 'N/A' and d2 == 'N/A'):
      return True
    elif(d1 == 'N/A' and d2 != 'N/A'):
      return False
    else:
      d1_int = self.strToIntArrDate(d1)
      d2_int = self.strToIntArrDate(d2)
      if(d1_int[2] > d2_int[2]):
            return False
      elif(d1_int[2] == d2_int[2]):
        if(d1_int[1] > d2_int[1]):
          return False
        elif(d1_int[1] == d2_int[1]):
          if(d1_int[0] > d2_int[0]):
            return False
    return True

  def test_all_divorce_dates(self):
    ret = True
    ftable = run()[1]
    for row in ftable:
      row.border = False
      row.header = False
      marriage_date = row.get_string(fields=['Married']).strip()
      divorce_date = row.get_string(fields=['Divorced']).strip()
      ret = self.compareDates(marriage_date, divorce_date)
    self.assertTrue(ret)

  def test_good(self):
    ret = True
    ftable=run()[1]
    ftable.add_row(['', '6 May 2015', '7 May 2015', '', '', '', '', ''])
    for row in ftable:
      row.border = False
      row.header = False
      marriage_date = row.get_string(fields=['Married']).strip()
      divorce_date = row.get_string(fields=['Divorced']).strip()
      if not self.compareDates(marriage_date, divorce_date):
        ret = False
    self.assertTrue(ret)

  def test_bad(self):
    ret = True
    ftable=run()[1]
    ftable.add_row(['', '6 May 2015', '4 May 2015', '', '', '', '', ''])
    for row in ftable:
      row.border = False
      row.header = False
      marriage_date = row.get_string(fields=['Married']).strip()
      divorce_date = row.get_string(fields=['Divorced']).strip()
      if not self.compareDates(marriage_date, divorce_date):
        ret = False
    self.assertFalse(ret)

  def test_good_bad_good(self):
    ret = True
    ftable=run()[1]
    ftable.add_row(['', '1 July 2000', '2 July 2000', '', '', '', '', ''])
    ftable.add_row(['', '6 May 2015', '4 May 2014', '', '', '', '', ''])
    ftable.add_row(['', '6 May 2015', '7 May 2015', '', '', '', '', ''])
    for row in ftable:
      row.border = False
      row.header = False
      marriage_date = row.get_string(fields=['Married']).strip()
      divorce_date = row.get_string(fields=['Divorced']).strip()
      if not self.compareDates(marriage_date, divorce_date):
        ret = False
    self.assertFalse(ret)

  def test_bad_good_bad(self):
    ret = True
    ftable=run()[1]
    ftable.add_row(['', '1 July 2000', '30 May 2000', '', '', '', '', ''])
    ftable.add_row(['', '6 May 2015', '9 May 2014', '', '', '', '', ''])
    ftable.add_row(['', '6 May 2015', '7 May 2011', '', '', '', '', ''])
    for row in ftable:
      row.border = False
      row.header = False
      marriage_date = row.get_string(fields=['Married']).strip()
      divorce_date = row.get_string(fields=['Divorced']).strip()
      if not self.compareDates(marriage_date, divorce_date):
        ret = False
    self.assertFalse(ret)


 
if __name__ == '__main__':
    unittest.main()

