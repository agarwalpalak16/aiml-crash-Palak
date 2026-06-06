# This program calculates tip and total bill amount.

# return sends data back from a function
# print only displays output on the screen

def calculate_tip(bill, tip_percent):
    tip_amount = (bill * tip_percent) / 100
    total = bill + tip_amount

    return {
        "tip": tip_amount,
        "total": total
    }

bill1 = calculate_tip(1000, 10)
bill2 = calculate_tip(2500, 15)
bill3 = calculate_tip(500, 5)

print(bill1)
print(bill2)
print(bill3)