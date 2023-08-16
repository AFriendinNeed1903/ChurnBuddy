#Credit Card Compare

print("Welcome to the credit card program!")

signUpBonus = float(input("\nWhat's the sign up bonus on your card?\nIf it's points, enter the raw number of points with no comma. If it's cash, just enter number of dollars with no comma.\nIf you can't hit the required spend to get the sign up bonus, you'd better enter 0.\n"))

pointValue = float(input("\nWhat's the cent value of each point from the card?\nIf you're getting raw cash, you'll put 100.\n"))

diningBonus = float(input("\nHow many points per dollar do you get on dining?\nthat includes catering for chapter dinner. it may or may not include a meal plan, or bar tabs.\n"))

diningSpend = float(input("\nHow much will we spend on dining? Either guesstimate, or use a previous semester's spend.\n"))

groceryBonus = float(input("\nHow many points per dollar do you get on grocery? that includes liquor stores.\n"))

grocerySpend = float(input("\nHow much will we spend on grocery? Either guesstimate, or use a previous semester's spend.\n"))

otherBonus = float(input("\nHow many points per dollar do you get on everything else?\nMake sure you won't be charged card fees for doing these other sources.\n"))

otherSpend = float(input("\nHow much will we spend on everything else? Either guesstimate, or use a previous semester's spend.\n"))

annualFee = 2 * float(input("\nWhat's the annual fee for this card?\nAfter you give it to me I'm going to multiply it by 2, because you need to keep a card for two years or else when you cancel it the bank will be mad at you.\n"))

yummyRebates = 2 * float(input("\nCheck the rebates for this card. What is the dollar value of the rebates that you'll actually use?\nPlease try to ignore rebates you can convince yourself are good, like CLEAR. Focus on spend you're already going to do anyway.\nAfter you give it to me I'm going to multiply it by 2, because you need to keep a card for two years or else when you cancel it the bank will be mad at you.\n"))

profit = ((signUpBonus * pointValue) - annualFee + yummyRebates +
          ((diningSpend * ((diningBonus * pointValue) / 100)) +
           (grocerySpend * ((groceryBonus * pointValue) / 100)) +
           ((otherSpend * pointValue)/100)))

print("Alright great! Crunching the numbers now.")
print("The profit for owning this card for two years and using it for the spend you've described is as follows: ", profit)