# Financial Information and Analytics
# Assignment 3
# By Rajat Sudagade (UTD ID: 2021449378)
# Stocks

# Question 1
# 1.	The Jackson-Timberlake Wardrobe Co. just paid a dividend of $1.32 per share on its stock. The dividends are expected to grow at a constant rate of 6 percent per year indefinitely.
# Required:
# (a)	If investors require a 10 percent return on The Jackson-Timberlake Wardrobe Co. stock, what is the current price?
# (b)	What will the price be in 10 years?
def stock1():
  dividend = 1.32 # Dividend paid by Jackson-Timberlake Wardrobe Co. per share on its stock.
  rate = 0.06 # The Constant Rate at which the dividends are expected to grow indefinetly.
  requiredReturn = 0.1 # Return required by the investors
  years = 10 # To calculate the price in ten years.
  P = dividend * ((1 + rate) / (requiredReturn - rate)) # P = D((1 + g)/ (R - g))
  P10 = dividend * (((1 + rate) ** (years + 1)) / (requiredReturn - rate)) # Price in 10 years
  print("""Answer 1:
  a. The current price of the stock if the investors require 10 percent return is: ${:0,.2f}
  b. The price in 10 years will be: ${:1,.2f} \n""".format(P, P10))

# Question 2
# 2.	The next dividend payment by Hot Wings, Inc., will be $4.55 per share, The dividends are anticipated to maintain a 3 percent growth rate forever.
# Required: If the stock sells for $40 per share, what is the required return?
def stock2():
  D1 = 4.55 # The next dividen payment by Hot Wings, Inc.
  g = 0.03 # Growth rate is 3 percent forever
  P = 40 # Selling price of the stock
  R = (D1 / P) + g # Required Return 
  print("""Answer 2:
  The required return of the stock is: {:,.2f}% \n""".format(R * 100))

# Question 3 
# Metroplex Corporation will pay a $4.90 per share dividend next year4 The company pledges to increase its dividend by 4.30 percent per year indefinitely.
# Required: If you require an 7.90 return on your investment, how much will you pay for the company’s stock today?
def stock3():
  D1 = 4.90 # Dividend
  g = 0.043 # Growth rate
  R = 0.079 # Required return
  P0 = D1 / (R - g) # Price of the stock
  print("""Answer 3:
  For the company's stock today, we will pay: ${:,.2f}\n""".format(P0))

# Question 4
# Suppose you know a company's stock currently sells for $90 per share and the required return on the stock is 10 percent. 
# You also know that the total return on the stock is evenly divided between a capital gains yield and a dividend yield.
# Required: If it’s the company’s policy to always maintain a constant growth rate in its dividends, what is the current dividend per share?
def stock4():
  requiredReturn = 0.1 # Required Return
  sellingPrice = 90 # Selling price
  capitalGain = requiredReturn / 2 # Capital Gain 
  dividendYield = requiredReturn / 2 # Dividend Yield
  currentDividend = ((sellingPrice * dividendYield) / (1 + capitalGain)) # Current Dividend
  print("""Answer 4:
  The current dividend per share is: ${:,.2f}\n""".format(currentDividend))

# Question 5:
# Apocalyptica Corp. pays a constant $25 dividend on its stock. 
# The cornpany will maintain this dividend for the next 7 years and will then cease paying dividends forever.
# Required: If the required return on this stock is 10 percent, what is the current share price?
def stock5():
  dividend = 25 # Dividend
  t = 7 # Number of years
  r = 0.1 # Required Return
  pvifa = (1 - ((1 + r) ** (-t))) / r # Present Value of Annuity Factory
  P = dividend * pvifa # Current Price
  print("""Answer 5:
  The current share is: ${:,.2f}\n""".format(P))

# Question 6:
# Red, Inc., Yellow Corp., and Blue Company each will pay a dividend of $1.40 next year. The growth rate in dividends for all three companies is 6 percent. The required return for each company's stock is 8.90 percent, 11.90 percent, and 15.30 percent, respectively.
# Required:
# (a)	What is the stock price for Red. Inc., Company?
# (b)	What is the stock price for Yellow Corp. Company?
# (c)	What is the stock price for Blue Company?
def stock6():
  dividend = 1.40 # Dividend
  growthRate = 0.06 # Growth Rate
  redRequired = 0.089 # Required Rate for Red
  yellowRequired = 0.119 # REquired rate for Yellow
  blueRequired = 0.153 # Required Rate for Blue
  redStock = dividend / (redRequired - growthRate) # Stock value of Red
  yellowStock = dividend / (yellowRequired - growthRate) # Stock value of Yellow
  blueStock = dividend / (blueRequired - growthRate) # STock value of Blue
  print("""Answer 6:
  a. The stock price for Red. Inc., Company is: ${0:,.2f}
  b. The stock price for Yellow Corp. Company is: ${1:,.2f}
  c. The stock price for Blue Company is: ${2:,.2f}\n""".format(redStock, yellowStock, blueStock))

# Question 7:
# Metallic Bearings, Inc., is a young start-up company.  No dividends will be paid on the stock over the next 15 years because the firm needs to plow back its earnings to fuel growth.  The company will pay a $11 per share dividend in 16 years and will increase the dividend by 4 percent per year thereafter.
# Required: If the required return on this stock is 12 percent, what is the current share price? (Do not round your intermediate calculations.)
def stock7():
  D = 11 # Dividend
  r = 0.12 # Required Return rate
  g = 0.04 # Growth rate
  years = 15 # Years
  P = D / (r - g) 
  P0 = P / ((1 + r) ** (years)) # Current Share price
  print("""Answer 7:
  The present share price is: ${:,.2f}\n""".format(P0))

# Question 8:
# Far Side Corporation is expected to pay the following dividends over the next four years: $13, $11, $9, and $5. 
# Afterward, the company pledges to maintain a constant 8 percent growth rate in dividends forever.
# Required: If the required return on the stock is 17 percent, what is the current share price? (Do not round your Intermediate calculations.)
def stock8():
  D1 = 13 #Dividend for year 1
  D2 = 11 #Dividend for year 2
  D3 = 9 #Dividend for year 3
  D4 = 5 #Dividend for year 4
  g = 0.08 #Growth rate
  R = 0.17 #Required Rate
  P4 = D4 * ((1 + g) / (R - g)) #Price after year 4
  P = (D1 / (1 + R)) + (D2 / ((1 + R) ** (2))) + (D3 / ((1 + R) ** (3))) + (D4 / ((1 + R) ** (4))) + (P4 / ((1 + R) ** (4))) #Current Share price
  print("""Answer 8:
  The current share price is: ${:,.2f}\n""".format(P))

# Question 9:
# Marcel Co. is growing quickly. 
# Dividends are expected to grow at a 18 percent rate for the next 3 years, with the growth rate falling off to a constant 4 percent thereafter.
# Required: If the required return is 7 percent and the company just paid a $1.60 dividend.  What is the current share price?  (Do not round your intermediate calculations.)
def stock9():
  dividend = 1.6 #Dividend 
  rate = 0.18 # Expected Return Rate
  growthRateAfter = 0.04 # Growth after 
  requiredReturn = 0.07 # Required Return
  period1 = dividend * (1 + rate) # First period
  period2 = period1 * (1 + rate) # Second Period
  period3 = period2 * (1 + rate) # Third Period
  afterPeriod3 = (period3 * ( 1 + growthRateAfter)) / (requiredReturn - growthRateAfter) # After Third Period
  csp =  (period1 / (1 + requiredReturn)) + (period2 / ((1 + requiredReturn) **(2))) + (period3 / ((1 + requiredReturn) ** (3))) + (afterPeriod3 / ((1 + requiredReturn) ** (3))) # Current Share Price
  print("""Answer 9:
  The current share price is: ${:,.2f}\n""".format(csp))

# Question 10:
# 10.	Antiques R Us is a mature manufacturing firm. 
# The company just paid a $18 dividend, but management expects to reduce the payout by 12 percent per year indefinitely.  
# Required: If you require an 19 percent return on this stock, what will you pay for a share today?
def stock10():
  D0 = 18 # Dividend just paid
  g = 0.12 # Dividend reduce by rate
  required = 0.19 # Required return rate
  D1 = D0 - (g * D0) # New Dividend
  P0 = D1 / (required + g) # Today's payment
  print("""Answer 10:
  For a 19 percent return today, we will pay today: ${:,.2f}\n""".format(P0))

# Print Functions
print("""Financial Information and Analytics\n
Assignment 3\n
Stocks\n
By Rajat Sudagade (UTD ID 2021449378)\n""")
def menu():
  print("Displaying all the answers... \n")
  stock1()
  stock2()
  stock3()
  stock4()
  stock5()
  stock6()
  stock7()
  stock8()
  stock9()
  stock10()
  a = str(input("Do you want to run this code again? Y/N: \n"))
  if (a == "Y"):
    menu()
menu()
