# 📈 DRIP Simulation

A Python tool to simulate **Dividend Reinvestment Plans (DRIP)** for two Philippine REIT stocks:

- CITICORE ENERGY REIT CORP. (CREIT)
- RL COMMERCIAL REIT INC. (RCR)

It calculates accumulated shares and reinvested dividends based on:
- Monthly deposits
- Investment duration (in years)
- Quarterly dividend payouts
- Board lot constraints

All simulation results are saved to CSV files for review and analysis.

---

## 🛠️ Features

- Terminal-based menu for stock selection
- User input for monthly deposit & duration
- Simulates share accumulation with DRIP
- Outputs dividend/share log to a `.csv` file
- Prints a detailed investment summary

---

## 🧠 How It Works

1. Select between **CREIT** or **RCR**
2. Input your:
   - Monthly deposit amount
   - Investment duration in years
3. The program:
   - Simulates quarterly dividend payouts
   - Buys shares only in board lot multiples
   - Reinvests dividends into new shares
   - Logs the data to a CSV file
4. Optionally displays the dividend log

---

## 📄 Output CSV Files

Depending on the stock selected, one of these files is generated:

- `creit_div.csv` – for CREIT
- `rcr_div.csv` – for RCR

### 📂 Sample Format

Year,Quarter,Dividends,Shares
1,1,54.50,1200
1,2,58.25,1400
...

Each row shows the total dividends received and the accumulated shares at the end of each quarter.

---

## 🚀 How to Run

Make sure Python is installed. Then in your terminal:

```bash
python your_script_name.py
Replace your_script_name.py with the actual file name (e.g., drip_simulator.py).

✅ Requirements
Python 3.x

No external libraries (only uses Python’s built-in csv module)

📌 Notes
Prices and dividend yields are hardcoded based on current public data.

Outputs overwrite existing .csv files for each run.

Designed for personal simulation and learning purposes.

## Version History

### v1.1 – Class-based Refactor (2025-08-13)
- Rewrote simulation using OOP (classes for Stock, Market, User, Calculation).
- Added cleaner stock info display.
- Logging now uses `csv.DictWriter`.
- More readable and maintainable code.

### v1.0 – Initial Release
- Procedural code for DRIP simulation of RCR and CREIT.
- CSV logging of dividends and shares.

