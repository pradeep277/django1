def today1():
    
    import datetime as dt
    today = dt.datetime.now()
    Y1 = today.year
    M1 = today.month
    D1=today.day

    s1 = str(Y1)+ " " + str(M1) + " " + str(D1)
    print(s1)

print(today1())
