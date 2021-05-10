### Instructions
# - Import the below library before you start with the questions
# - Use the dataset (flights) in nycflights13 library to ans below questions
# - Only the executable code should be placed in the ans section
# - Marking will be done based on correct output and also ways of writing code
# - Prefer using dplyr and pipe funtions to ans the questions
# - Any plagiarism or direct online copy past of code will be panelized 

# **Imp: this same .R file with Ans and executable code should be mailed to us at hr@stepupanalytics.com
# Last date of subission: 19th Nov End of the day.

#library(tidyverse)
#library(lubridate)
#library(nycflights13)                       
from nycflights13 import flights
from datetime import date,datetime


"""date_time_str = '180919'

date_time_obj = datetime.strptime(date_time_str, '%d%m%y')


print("The type of the date is now",  type(date_time_obj))
print("The date is", date_time_obj)"""

# Q1. Write a function that given your birthday (as a date), returns how old you are in years.
# Ans1
def f(d):
    age=date.today()
  
    return age.year-d.year-((age.month,age.day)<(d.month,d.day))



### Ans1 Ends ####

# Q2. What happens if you parse a string that contains invalid dates? Ex: ymd(c("2010-10-10", "bananas"))
# Ans2 
"""datetime.strptime("banana","%m%d%y")
In python it will give value error saying 'banana doesnot match format %m%d%y'"""


### Ans2 Ends ####

# Q3. How do you import default dataset presend in R to work session
# Ans3
""" In the packages panel we will find the list of packages , among them there will be a package with name datasets . we will have to check in its checkbox .Now just use the datasets by using dataset name
"""



# Ans3 Ends

###########################################################
#### Using the flights data, Find all the flights that ####
#### Instruction: Paste just the query which gives the correct output ##

# Q4. Had an delay in arrival of 3 or less hours
# Ans4

print(flights[(flights["arr_delay"]<=180) & (flights["arr_delay"]>0)]["flight"])


# Ans4 Ends

# Q5. Flew to Houston (IAH or HOU)
# Ans5
print(flights[(flights["dest"]=="IAH" )| (flights["flight"]=="HOU")]["flight"])


# Ans5 Ends

#Q6. Were operated by United, American, or Delta
# Ans6
print(flights[(flights["carrier"]=="UA" )| (flights["carrier"]=="AA")|(flights["carrier"]=="DL")]["flight"])




# Ans6 Ends

# Q7. Departed in summer (July, August, and September)
# Ans 7
print(flights[(flights["month"]>=7) & (flights["month"]<=9) ]["flight"])




# Ans7 Ends

# Q8. Arrived more than two hours late, but didn???t leave late
# Ans8
print(flights[(flights["arr_delay"]>120)& (flights["dep_delay"]<=0)]["flight"])




# Ans8 Ends

# Q9. Were delayed by at least an hour, but made up over 30 minutes in flight
# Ans9
print(flights[(flights["dep_delay"]>=60 )&(flights["dep_delay"]-flights["arr_delay"]>30)]["flight"])




# Ans9 Ends

#Q10. Departed between midnight and 6am (inclusive)
#Ans10
print(flights[(flights["dep_time"]<=600) |(flights["dep_time"]==2400)]["flight"])


#Ans 10 Ends
