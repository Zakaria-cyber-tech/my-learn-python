multiple=int(input("Enter the nember for multiplication table: "))
print(f"the multiplication table of {multiple} is:\n")
for x in range(1, 11):
    multi=x * multiple
    print(f"{multiple} * {x} = {multi}" )