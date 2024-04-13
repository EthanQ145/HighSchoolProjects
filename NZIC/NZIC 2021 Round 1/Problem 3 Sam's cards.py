card_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['spades', 'clubs', 'diamonds', 'hearts']
inputted_card_number = input()
inputted_suit = input()
larger_suits = SUITS.index('hearts') - SUITS.index(inputted_suit)
larger_numbers = len(card_numbers) - card_numbers.index(inputted_card_number) - 1
num_of_larger_cards = larger_suits * len(card_numbers) + larger_numbers
print(num_of_larger_cards)

