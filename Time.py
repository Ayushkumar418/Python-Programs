def Time():
    import time
    timestamp = int(time.strftime('%H'))
    if 4<=timestamp<=10:
        print("\nGood Morning Sir🥱.")
    elif 10<timestamp<=15:
        print("\nGood Afternoon Sir🤨.")
    elif 15<timestamp<=20:
        print("\nGood Evening Sir🫡.")
    else:
        print("\nGood Night Sir😴.")
