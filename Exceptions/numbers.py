try:
    x = int(input("What is x? "))
except Exception:
    print("please input an integer")
else:
    print(f"x = {x}")