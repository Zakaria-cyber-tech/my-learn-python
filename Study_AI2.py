from textblob import TextBlob

while True:
    text=input("Enter Any text for Revion:  ")
    corr=TextBlob(text)
    if corr.correct()==text:
        print("input is correct.")
    else:
        print(corr.correct())
        break