# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

# daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# def isLeapYear(year):
#     ##
#     # Your code here. Return True or False
#     # Pseudo code for this algorithm is found at
#     # http://en.wikipedia.org/wiki/Leap_year#Algorithm
#     ##

# def daysBetweenDates(y1, m1, d1, y2, m2, d2):
#     ##
#     # Your code here.
#     ##
#     return days



    ###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

# def nextDay(year, month, day):
#     """
#     Returns the year, month, day of the next day.
#     Simple version: assume every month has 30 days.
#     """
#     # YOUR CODE HERE
#     if day < 30:
#         return year, month, day + 1
#     else:
#         if month < 12:
#             return year, month + 1, 1
#         else:
#             return year + 1, 1, 1


# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    # YOUR CODE HERE!
    days = 0
    while dateisbefore(year1, month1, day1, year2, month2, day2):
        year1,month1, day1 = nextDay(year1, month1, day1)
        days +=1
    return days

def dateisbefore(year1, month1, day1, year2, month2, day2):
   
    if year1 < year2:
        return True
    
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1<day2
    return False


def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

#test()

print daysBetweenDates(2013,1,24,2013,6,29)



