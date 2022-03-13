from calendar import day_abbr
import datetime
from Speak import Say

# Non-Input Function

def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date=datetime.date.today()
    Say(date)

def Day():
    day=datetime.datetime.now().strftime("A")
    Say(day)

def NonInputExecution(query):
    query=str(query)
    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

# Input Function

def InputExecution(tag,query):
    
    if "wikipedia" in tag:
        name=str(query).replace("Who is","").replace("about","").replace("What is","").replace("wikipedia","")
        import wikipedia
        result=wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query=str(query).replace("google","")
        query=query.replace("search","")
        import pywhatkit
        pywhatkit.search(query)
