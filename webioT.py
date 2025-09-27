from pywebio.input import input, FLOAT
from pywebio.output import put_text

def bmi():
    height = input("دخل الطول ديالك (cm):", type=FLOAT)
    weight = input("دخل الوزن ديالك (kg):", type=FLOAT)

    bmi = weight / ((height / 100) ** 2)
    put_text("BMI ديالك هو: %.1f" % bmi)

bmi()