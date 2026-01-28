while True:
    try:
        x = int(input("What is x? "))
    except Exception:
        print("please input an integer")
    else:
        break

print(f"x is {x}")
