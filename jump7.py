for value in range(1,101):
    if(value % 7 == 0 or value %10==7 or value//10==7):
        continue
    else:
         print(value)
