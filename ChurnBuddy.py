class CreditCard:
    def __init__(self, name, rewards_dining, rewards_grocery, rewards_transportation, rewards_misc, monthly_fee):
        self.name = name
        self.rewards_dining = rewards_dining
        self.rewards_grocery = rewards_grocery
        self.rewards_transportation = rewards_transportation
        self.rewards_misc = rewards_misc
        self.monthly_fee = monthly_fee

    def calculate_profitability(self, monthly_spending_dining, monthly_spending_grocery, monthly_spending_transportation, monthly_spending_misc):
        total_rewards = self.rewards_dining * monthly_spending_dining / 100 + self.rewards_grocery * monthly_spending_grocery / 100 + self.rewards_transportation * monthly_spending_transportation / 100 + self.rewards_misc * monthly_spending_misc / 100
        
        monthly_profit = total_rewards - self.monthly_fee
        return monthly_profit

def insertion_sort(cards, monthly_spending_dining, monthly_spending_grocery, monthly_spending_transportation, monthly_spending_misc):
    for i in range(1, len(cards)):
        current_card = cards[i]
        current_profit = current_card.calculate_profitability(monthly_spending_dining, monthly_spending_grocery, monthly_spending_transportation, monthly_spending_misc)

        j = i - 1
        while j >= 0 and cards[j].calculate_profitability(monthly_spending_dining, monthly_spending_grocery, monthly_spending_transportation, monthly_spending_misc) < current_profit:
            cards[j + 1] = cards[j]
            j -= 1

        cards[j + 1] = current_card

def main():
    # ask user's monthly spending
    monthly_spending_dining = float(input("Enter your monthly dining spending: "))
    monthly_spending_grocery = float(input("Enter your monthly grocery spending: "))
    monthly_spending_transportation = float(input("Enter your monthly transportation spending: "))
    monthly_spending_misc = float(input("Enter your monthly miscellaneous spending: "))

    # make a list of credit card objects
    cards = []

    # make credit cards until user is done
    while True:
        card_name = input("Enter the name of the credit card (or 'done' to finish): ")
        if card_name == "done":
            break

        rewards_dining = float(input("Enter the rewards rate for dining (percentage or X): "))
        rewards_grocery = float(input("Enter the rewards rate for groceries (percentage or X): "))
        rewards_transportation = float(input("Enter the rewards rate for transportation (percentage or X): "))
        rewards_misc = float(input("Enter the rewards rate for misc/other (percentage or X): "))
        monthly_fee = float(input("Enter the monthly fee (if only annual fee availible, divide by 12): "))

        card = CreditCard(card_name, rewards_dining, rewards_grocery, rewards_transportation, rewards_misc, monthly_fee)
        cards.append(card)

    # sort credit cards based on profitability
    insertion_sort(cards, monthly_spending_dining, monthly_spending_grocery, monthly_spending_transportation, monthly_spending_misc)

    # print the final sorted list of credit cards
    print("\nSorted credit cards based on profitability:")
    for card in cards:
        profit = card.calculate_profitability(monthly_spending_dining, monthly_spending_grocery, monthly_spending_transportation, monthly_spending_misc)
        print(f"{card.name}: ${profit:.2f}")

if __name__ == "__main__":
    main()
