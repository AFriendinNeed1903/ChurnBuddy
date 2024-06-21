Credit Card Profitability Calculator, originally created by Adam Altmejd, later used jointly for a class project by Adam Altmejd and Matthew Santos. 

Project Overview:

It's a credit card points calculator. It first asks the user what their monthly spending is on the following categories: dining, grocery, transportation, and misc. Then once it has that info, it uses object-oriented programming to create a bunch of credit card objects, by asking the user the name of a credit card and for its point rewards on each of those listed categories, as well as its monthly fee. Once the user is done making new objects, it uses an insertion sort to list the cards from most to least profitable given the user's specified objects. This is all done through a simple and unfancy command line plaintext interface.

Dataset:

We don't use any external datasets. The program relies on user-provided info regarding monthly spending in different categories.

Package, Class, Method, and Function Design

The program has of two main parts outside of its main function: the 'CreditCard' class and the 'insertion_sort()' function.

CreditCard Class:

Attributes:
- 'name': Represents the name of the card
- 'rewards_dining', 'rewards_grocery', 'rewards_transportation', 'rewards_misc': Represent the rewards rates for dining, groceries, transportation, and miscellaneous spending.
- 'monthly_fee': Represents the monthly fee associated with the card

Methods:
- 'calculate_profitability()': Calculates the monthly profit for the credit card based on the user's monthly spending in each of the categories

insertion_sort() Function:

Purpose: Implements the insertion sort algorithm to sort a list of credit card objects based on their monthly profitability.

Libraries

We don't use any libraries

Data Structures

For maximal compliance with the described requirements, we used 2 data structures from class: Lists and Objects. We also used the Insertion Sorting Algorithm to meet with the requirements described in the project pdf.

Test Cases
To ensure the correctness of the software, we ran through it a few times by hand and checked it against math we did manually. It all checks out!

Software Expectations

The software is should accurately calculate the monthly profitability of different credit cards based on user-provided spending patterns within narrow parameters. It should handle various input scenarios and offer a friendly interface for interacting with itself.

Expected Weaknesses

1. lack of calculation on Sign Up Bonus profitability. This is an unfortunate flaw in the program which I hope to address one day with personal development.

2. Limited customization: The program currently focuses on four spending categories, but it could be enhanced to accommodate user created spending categories so that the user may delineate as many or few spending categories as they'd like.

3. limited Error handling: the program does not handle errors well, and crashes like the titanic if given anything it doesn't expect.

4. it doesn't value points at anything other than 1cpp.
