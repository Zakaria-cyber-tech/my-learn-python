from textblob import TextBlob
def choose(text):
    blob=TextBlob(text)
    sentiment=blob.sentiment
    if sentiment.polarity > 0:
        return "Happy"
    elif sentiment.polarity <0:
        return "Sad"
    else:
        return "Normal"
text=input("Enter A Text:  ")
mood=choose(text)
print(f"Your status IS:{mood}")