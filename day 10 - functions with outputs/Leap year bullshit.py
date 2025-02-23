def is_leap(year):
  global Leap
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        Leap = True


      else:
        Leap = False


    else:
      Leap = True


  else:
    Leap = False


  
# TODO: Add more code here 👇
def days_in_month(the_year, month_days):
  month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leap_month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  the_leap = ""
  is_leap(year)

  if Leap == True:
    month_days[2] += 1
    return month_days[month]
  elif Leap == False:
    return month_days[month]

  print(month_days[month])




  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)



