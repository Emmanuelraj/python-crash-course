# raise equivalent in java is throw
# Handling in exception in java try catch finally in python try except finally


try:
    x = 7/0

except ZeroDivisionError as ex:
    print('zero',ex)    

except Exception as e:
    print(e) 

finally:
    print('finally') 
