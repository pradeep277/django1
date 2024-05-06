def today1():
    
    import datetime as dt
    today = dt.datetime.now()
    Y1 = today.year
    M1 = today.month
    D1=today.day
    h1 = today.hour
    m1 = today.minute
    s1 = today.second

    str1 = str(Y1)+ " " + str(M1) + " " + str(D1)
    str2 = str(h1)+ " " + str(m1) + " " + str(s1)
    print(str1)
    print(str2)

print(today1())
