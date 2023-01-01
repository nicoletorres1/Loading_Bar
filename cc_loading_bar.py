

# can possibly use print(amountloaded, end ="")
for amount_loaded in range(0, 101, 5):
    if amount_loaded == 25:
        print("25 - 1/4 of the way there.")
    elif amount_loaded == 50:
        print("50 - 1/2 way there.")
    elif amount_loaded == 75:
        print("75 - 3/4 of the way there.")
    elif amount_loaded == 100:
        print("100 - Loading complete.")
    else:
        # moving this print to the else causes to print in the format I wanted.
        print(amount_loaded)
        continue
