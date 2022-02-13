from replit import clear
#HINT: You can call clear() to clear the output in the console.
print("Secret Auction Program")

from art import logo

print(logo)

isAuctionOn = True

highestBidders = {}
while isAuctionOn:
  
  name = input("What is your name? ")
  bidAmount = int(input("What's your bid?: $"))
  highestBidders[name] = bidAmount
  toContinue = input("Are there any more bidders, 'yes'/'no': ")

  if toContinue == 'no':
    isAuctionOn = False
  else:
    clear()
    continue
  

highestBid = 0
nameOfbidder = ""
for item in highestBidders.keys():
  if highestBid < highestBidders[item]:
    highestBid = highestBidders[item]
    nameOfbidder = item

print(f"Today's winner is {nameOfbidder} with a bid of {highestBid}.")
    
