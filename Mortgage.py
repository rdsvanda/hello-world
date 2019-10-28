good_credit = False
bad_credit = False
price = 1000000
good_rate = int(price * .1)
bad_rate = int(price * .2)

if good_credit:
    print('Congratulations, you have good credit so your down payment will be $' + str(good_rate))

else:
    print('Well, you can get the house but the down payment will be $' + str(bad_rate))


