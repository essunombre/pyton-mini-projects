bid = {}
def add_offer(name, price):
    bid[name] = price

def best_bider(bid):
    highest_bid = 0
    winner = ""
    for bidder in bid:
        bid_amount = bid[bidder] 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"El ganador es {winner} con una cantidad de ${bid_amount}!")


another_bid = False
while not another_bid:
    name = input("Saludos, como es tu nombre? ")
    price = float(input("Cuanto quieres pagar? "))
    add_offer(name, price)
    should_continue = input('Hay otro participante? (responder "si" o "no")\n')
    if should_continue == "no":
        another_bid = True        
        best_bider(bid)

#revisar repl