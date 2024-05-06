def today1():
    
    import datetime as dt
    today = dt.datetime.now()
    hour=today.hour
    return hour

print(today1())
