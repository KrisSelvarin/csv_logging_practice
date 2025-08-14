# class implementation
import csv

class Name:
    def __init__(self, company, ticker):
        self.company = company.upper()
        self.ticker = ticker.upper()

class Stock:
    def __init__(self, name, pps, div_yield, payout, board_lot):
        self.name = name
        self.pps = pps
        self.div_yield = div_yield
        self.payout = payout
        self.board_lot = board_lot

    def get_info(self):
        freq_map = {12: 'Monthly', 4: 'Quarterly', 2: 'Bi-Annually', 1: 'Annually'}
        freq = freq_map.get(self.payout)

        print(
            f'\n{self.name.company}   ({self.name.ticker})\n\n'
            f'Price per Share:        ₱{self.pps:.2f}\n'
            f'Yield % (Indicated):    {self.div_yield}%\n'
            f'Dividend Pay-out:       {freq}\n'
            f'Minimum Board Lot:      {self.board_lot:,} shares'
        )
        
class Market:
    def __init__(self):
        self.stock_market = []
    
    def add_stock(self, stock):
        self.stock_market.append(stock)

    def display_stocks(self):
        if not self.stock_market:
            print('No stocks were added!')
        else:
            for stock in self.stock_market:
                stock.get_info()
                print()

class User:
    def __init__(self, dep, time):
        self.dep = dep
        self.time = time

    def user_info(self):
        print(
            f'Monthly Investment:   ₱{self.dep:.2f}\n'
            f'Investment Duration:  {self.time} Years\n'
        )

    @classmethod
    def user_input(cls):
        print()
        dep = float(input('Monthly Investment: ₱'))
        time = int(input('Investment Duration (Years): '))
        return cls(dep, time)
    
class Calculation:
    result = []
    t_shares = 0
    bp_total = 0

    @classmethod
    def calculate(cls, selection, user):
        cls.result = []         # reset before new calculations
        cls.t_shares = 0        # reset before new calculations
        cls.bp_total = 0        # reset before new calculations
        # what stock to use
        if selection == 1:
            stock = stock_1
        else:
            stock = stock_2

        # constants
        board_lot_price = stock.board_lot * stock.pps
        dps = ((stock.div_yield / 100) * stock.pps) / stock.payout

        # calculations
        for t in range(user.time):
            for f in range(stock.payout):
                for _ in range(12 // stock.payout):
                    cls.bp_total += user.dep
                    n_shares = (cls.bp_total // board_lot_price) * stock.board_lot
                    cls.t_shares += n_shares
                    bp_used = n_shares * stock.pps
                    cls.bp_total -= bp_used

                dividend = dps * cls.t_shares
                cls.bp_total += dividend

                cls.result.append({
                    'Year': t + 1,
                    'Quarter': f + 1,
                    'Dividends': f'{dividend:.2f}',
                    'Shares': int(cls.t_shares)
                })

    @classmethod
    def logging(cls, selection):
        # what stock to use
        if selection == 1:
            stock = stock_1
        else:
            stock = stock_2

        filename = stock.name.ticker.lower() + '_div.csv'
        header = ['Year', 'Quarter', 'Dividends', 'Shares']

        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()

            for row in cls.result:
                writer.writerow(row)

# reassign
market = Market()

# add creit
name_creit = Name('CITICORE ENERGY REIT CORP.', 'CREIT')
stock_1 = Stock(name_creit, 3.68, 5.49, 4, 1000)
market.add_stock(stock_1)

# add rcr
name_rcr = Name('RL COMMERCIAL REIT INC.', 'RCR')
stock_2 = Stock(name_rcr, 7.90, 5.22, 4, 100)
market.add_stock(stock_2)


def menu():

    while True:
    
        print("\nDRIP SIMULATION FOR RCR AND CREIT\n")
        print("Choose Stock: ")

        c = {
            1: f"{stock_1.name.company} ({stock_1.name.ticker})",
            2: f"{stock_2.name.company} ({stock_2.name.ticker})",
            3: "Display Stocks' Info",
            4: "Exit",

        }

        for i in c:
            print(f'[{i}] {c[i]}')

        def selection():
            while True:
                try:
                    x = int(input('Selection: '))
                    if x in c:
                        return x
                    else:
                        print('Enter value between 1 to 4!\n')
                except ValueError:
                    print('Invalid Selection!\n')

        def branch(x):
            if x == 1:
                return x
            elif x == 2:
                return x
            elif x == 3:
                market.display_stocks()
                back = input('Back to Menu (Y|N): ').strip().lower()
                if back != 'y':
                    exit()
            else:
                exit()

        x = selection()
        choice = branch(x)
        if choice == 1 or choice == 2: 
            return branch(x)

def summary(selection, user):
    print("--------------------------------------------------------")
    if selection == 1:
        stock = stock_1
    else:
        stock = stock_2

    total_invest = user.dep * 12 * user.time
    total_share_cost = stock.pps * Calculation.t_shares
    roi = ((total_share_cost + Calculation.bp_total) - total_invest) / total_invest

    print('\nSummary: ')
    stock.get_info()
    print(f"Monthly Investment:     ₱{user.dep:,.2f}")
    print(f"Investment Duration:    {user.time} years")
    print(f'Total Investment:       ₱{total_invest:,.2f}')
    print(f'Total Shares Bought:    ₱{Calculation.t_shares:,.0f}')
    print(f'Total Shares Cost:      ₱{total_share_cost:,.2f}')
    print(f'Return on Investment:   {roi:.2%}\n')


def read(selection):
    print("--------------------------------------------------------")
    choice = input("Open Dividend Log (Y|N)? ").strip().lower()
    if selection == 1:
        stock = stock_1
    else:
        stock = stock_2

    if choice != 'y':
        print('Exiting Program!')
    else:
        print(f'\nDividend Log:\n')
        filename = stock.name.ticker.lower() + '_div.csv'
        with open(filename, 'r') as file:
            read = csv.DictReader(file)
            prev_year = None

            for i in read:
                year = int(i['Year'])
                quarter = int(i['Quarter'])
                dividends = float(i['Dividends'])
                shares = int(i['Shares'])

                if year != prev_year and prev_year != None:
                    print()

                print(f"Dividend in Year {year}, Quarter {quarter}: ₱{dividends:>10,.2f} | Shares: {shares:>7,.0f}")
                prev_year = year

def main():
    selection = menu()
    user = User.user_input()
    Calculation.calculate(selection, user)
    Calculation.logging(selection)
    summary(selection, user)
    read(selection)

    
if __name__ == '__main__':
    main()
