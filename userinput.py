from datetime import date

import datetime

Current_Date = datetime.datetime.today()
print ('Current Date: ' + str(Current_Date))

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)
print ('Previous Date: ' + str(Previous_Date))

NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
print ('Next Date: ' + str(NextDay_Date))

name = input('name :')

age = int(input ('age :'))

reps = 10;

reps+=1;

currentReps = reps

print('Hello', name , 'age is', age, Current_Date,' prev reps', reps)

reps-=1;

print('Hello', name , 'age is', age, Previous_Date,' today reps', reps)

nextReps = currentReps+1;

print('Hello', name , 'age is', age, NextDay_Date,'next  reps', nextReps)

print(nextReps*nextReps);

print('exponent', nextReps**nextReps)




