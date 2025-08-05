# this is still drip simulation
# i'll be using this for PSEI: RCR and CREIT personally

import csv

def main():
    sel = menu()
    constant = branch(sel)
    user = user_input()
    result = compute(user, constant)
    invest = user | result                          # merges both user and result dictionaries
    summary(invest, constant)
    read(constant)


# start up menu
def menu():

    print("\nDRIP SIMULATION FOR RCR AND CREIT\n")
    print("Choose Stock: ")

    c = {
        1: "CITICORE ENERGY REIT CORP. (CREIT)",
        2: "RL COMMERCIAL REIT INC. (RCR)",
        3: "EXIT",

    }

    for i in c:
        print(f"[{i}] {c[i]}")

    while True:
        try:
            x = int(input("Selection: "))
            if x in c:
                return x
            else:
                print("Enter value between 1to 3!\n")
        except ValueError:
            print("Invalid Input!\n")

def branch(sel):

    if sel == 1:
        return creit()
    elif sel == 2:
        return rcr()
    else:
        exit()


def creit():
    print("""
          CITICORE ENERGY REIT CORP. (CREIT)

          Price per Share:          ₱3.68
          Yield % (Indicated):      5.49%
          Dividend Pay-out:         Quarterly
          Minimum Board Lot:        100 shares
    """)
    
    # CREIT constant
    name = "CITICORE ENERGY REIT CORP. (CREIT)"
    pps = 3.68
    div_yield = 5.49 / 100
    board_lot = 1000

    #return
    return {'name': name, 'pps': pps, 'div_yield': div_yield, 'board_lot': board_lot}

def rcr():
    print("""
          RL COMMERCIAL REIT INC. (RCR)

          Price per Share:          ₱7.90
          Yield % (Indicated):      5.22%
          Dividend Pay-out:         Quarterly
          Minimum Board Lot:        100 shares
    """)

    # RCR constant
    name = "RL COMMERCIAL REIT INC. (RCR)"
    pps = 7.90
    div_yield = 5.22 / 100
    board_lot = 100

    #return
    return {'name': name, 'pps': pps, 'div_yield': div_yield, 'board_lot': board_lot}


def user_input():
        
    def dep_input():    
        while True:
            try:
                dep = round(float(input("Monthly Deposit: ₱")), 2)
                if dep > 0:
                    return dep
                else:
                    print("Enter value greater than 0!\n")
            except ValueError:
                print("Invalid Input!\n")

    def time_input():
        while True:
            try:
                t = int(input("Investment Duration (Years): "))
                if 0 < t <= 60:
                    return t
                else:
                    print("Enter value between 0 to 60!\n")
            except ValueError:
                print("Invalid Input!\n")

    return {
        "dep": dep_input(),
        "time": time_input(),

    }


def compute(user, constant):

    # constants
    freq = 4
    board_lot_price = constant['board_lot'] * constant['pps']

    bp_total = 0
    t_shares = 0

    # dividend per share per quarter
    dps = (constant['div_yield'] * constant['pps']) / freq

    # csv file (example: rcr_div.csv)
    filename = constant['name'].split('(')[-1].strip(')').lower() + f"_div.csv"
    header = ['Year', 'Quarter', 'Dividends', 'Shares']

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()

        # DRIP
        for t in range(user['time']):
            for f in range(freq):
                for _ in range( 12 // freq):
                    bp_total += user['dep']                                             # add deposit to buying power
                    n_shares = (bp_total // board_lot_price) * constant['board_lot']    # no. of shares (100 board lot min)
                    t_shares += n_shares                                                # accumulate shares
                    bp_used = n_shares * constant['pps']                                # amount used on shares
                    bp_total -= bp_used                                                 # remaining amount
                    
                # add dividend to bp
                dividend = dps * t_shares
                bp_total += dividend

                # Log
                writer.writerow({'Year': t + 1, 
                                 'Quarter': f + 1, 
                                 'Dividends': f'{dividend:.2f}', 
                                 'Shares': int(t_shares)
                })

    return {
        'bp_total': bp_total,
        'shares': t_shares,

    }


def summary(invest, constant):
        
        gained = (invest['shares'] * constant['pps']) + invest['bp_total']
        total_deposit = invest['dep'] * 12 * invest['time']
        roi = (gained - total_deposit) / total_deposit

        print(f"""
--------------------------------------------------------              
SUMMARY:
{constant['name']}

Price per Share:            ₱{constant['pps']}
Yield % (Indicated):        {constant['div_yield']:.2%}
Monthly Investment:         {invest['dep']:,.2f}
Investment Duration:        {invest['time']} years
Total Investment:           ₱{total_deposit:,.2f}

Total No. of Shares:        {invest['shares']:,.0f}
Total Amount of Shares:     ₱{invest['shares'] * constant['pps']:,.2f}

Return on Investment:       {roi:.2%}
""")


def read(constant):
    print("--------------------------------------------------------")

    choice = input("Open Dividend Log (Y/N)? ").lower()

    if choice == 'y':
        print("\nDividend Log\n")
        filename = constant['name'].split('(')[-1].strip(')').lower() + f"_div.csv"
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

    elif choice == 'n':
        exit()
    else:
        print('Invalid Input! Exiting Program!')
        exit()



if __name__ == "__main__":
    main()