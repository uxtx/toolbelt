interest = float(raw_input('Provide interest rate (no percent sign needed):  '))
price = float(raw_input('Provide price (no dollar sign needed): '))
years = int(raw_input('years to calculate?: '))


def calc_interest(interest_rate, price, years):
    new_price = price
    for year in xrange(years):
        new_price = new_price * (1+(interest_rate * 0.01))
        print 'value increase in Year %d is $%s' % (year, "%.2f" % new_price)

calc_interest(interest, price, years)
