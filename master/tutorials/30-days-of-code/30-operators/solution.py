mealPrice = float(input())
tipPercent = int(input())
taxPercent = int(input())

totalCost = mealPrice * (1 + (tipPercent + taxPercent)/100.0)

print("The total meal cost is {:.0f} dollars.".format(totalCost))