import random

'''========================='''

suits = ('Hearts' ,'Diamonds','Spades','clubs')

ranks = ('Tow','Three','Four','Five','Six','Seven',
	'Eight','Nine','Ten','Jack','Queen','King','Ace')

values = {'Tow':2 , 'Three':3 , 'Four': 4 , 'Five':5 ,'Six':6 ,
			'Seven':7,'Eight':8,'Nine':9, 'Ten':10,
			'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class Card():
	'''====================='''
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

		def __str__(self):
			return self.rank + " of " + self.suit

class Deck():
	"""docstring for Deck"""
	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_comp = ''
		for card in self.deck:
			deck_comp += "\n" + card.__str__()
		return "The deck has : " + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		single_card = self.deck.pop()
		return single_card

class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]

	def adjusst_for_ace(self):

		while self.value > 21 and self.aces > 0 :
			self.value -= 10
			self.aces -= 1

class Chips():
	'''===================='''

	def __init__(self,total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How Many Chips You Like to bet ? "))
		except ValueError:
			print("Sorry, a bet must be an integer!")
		else:
			if chips.bet > chips.total:
				print("Sorry, you dont have enough chips! You Have : {}".format(chips.total))
			else:
				break

def hit(deck,hand):

	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjusst_for_ace()

def hit_or_stand(deck,hand): 

	global playing 

	while True:
		x = input("Hit or Stand? Enter 'h' or 's' ")

		if x[0].lower() == 'h':
			hit(deck,hand)

		elif x[0].lower() == 's':
			print("Player Stands Dealer's Turn")
			playing = False

		else:
			print("sorry, I did not undrestand that, Please enter 's' or 'h' only!")
			continue

		break

def player_busts(player,dealer,chips):
	 print("BUST PLAYER!")
	 chips.lose_bet()

def dealer_busts(player,dealer,chips):
	print("BUST DEALER!")
	chips.win_bet()

def player_wins(player,dealer,chips):
	print("PLAYER WINS!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("DEALER WINS!")
	chips.lose_bet()

def push(player,dealer):
	print("Dealer and Player tie! PUSH")

def show_some(player,dealer):

	print("DEALERS HAND: ")
	print("one card hidden!")
	print(dealer.cards[1].rank + dealer.cards[1].suit)
	print('\n')
	print("PLAYERS HAND: ")
	for card in player.cards:
		print(card.rank + " " + card.suit)

def show_all(player,dealer):

	print("DEALERS HAND:")
	for card in dealer.cards:
		print(card.rank + card.suit)
	print('\n')
	print("PLAYERS HAND: ")
	for card in player.cards:
		print(card.rank + " " + card.suit)


while True:
	# print an opening statement
	print("* * * * * WELL COME TO BLACKJACK * * * * *")

	# create and shuffle the deck, deal two cards to each player
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())


	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# Set up the player's chips
	player_chips = Chips()

	# prompt the player for their bet
	take_bet(player_chips)

	show_some(player_hand,dealer_hand)

	while playing:

		hit_or_stand(deck,player_hand)

		show_some(player_hand,dealer_hand)

		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)

			break
	if player_hand.value <= 21:

		while dealer_hand.value < player_hand.value:
			hit(deck,dealer_hand)


		show_all(player_hand,dealer_hand)

		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

		print('\n Player total chips are at : {}'.format(player_chips.total))

		new_game = input("Would you like to play anouther hand? (y/n)")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thank you for playing!")
		break