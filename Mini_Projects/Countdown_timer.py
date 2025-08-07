import time

t = int(input("enter time in seconds: "))

for i in range(t, 0, -1):  # Here in this for loop we taking the range from t to 0 which is from end to start
    seconds = i % 60
    minutes = int(i / 60) % 60      # here compulsory we have to use int() to convert float to int
    hours = int(i / 3600)           # here compulsory we have to use int() as before in minutes
    # print(f"{hours:02}:{minutes:02}:{seconds:02}")
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")   
    '''end = '\r' is a carriage return character, 
    it will overwrite the content on the same line from the beginning, rather than printing on a new line'''
    time.sleep(1)
    
print("Time's up!")