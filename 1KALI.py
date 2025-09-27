import os
import json

dec = {"name": "", "age": "", "country": ""}

dec["name"] = input("Enter your name: ")

# التأكد أن age عدد صحيح
try:
    dec["age"] = int(input("Enter your age: "))
except ValueError:
    print("The age is incorrect")
    exit()

dec["country"] = input("Enter your country: ")

# كتابة dict في الملف بصيغة JSON مع سطر جديد
try:
    with open("test.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(dec, ensure_ascii=False) + os.linesep)
except Exception as e:
    print(f"Error: {e}")

print("Data save successfully")
# قراءة الملف وعرض المحتوى
try:
    with open("test.txt", "r") as f:
        print("Hello")
except:
    pass