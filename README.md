# DRIP Simulator OOP

A Python program that simulates a **Dividend Reinvestment Plan (DRIP)** for two sample stocks — **CITICORE ENERGY REIT CORP. (CREIT)** and **RL COMMERCIAL REIT INC. (RCR)** — using an **Object-Oriented Programming (OOP)** approach.

> ⚠️ **Note:** This is a **noob-level project** created purely for learning and mastery of Python and OOP concepts.  
> It is **not** intended for real-world financial decision-making.

---

## ✨ Features
- Two preloaded stocks:
  - CREIT
  - RCR
- Uses OOP structure with:
  - `Name` class for company/ticker info
  - `Stock` class for stock data and info display
  - `Market` class for stock management
  - `User` class for investment input
  - `Calculation` class for DRIP math and CSV logging
- Dividend pay-out frequency:
  - Monthly
  - Quarterly
  - Bi-Annually
  - Annually
- Supports fractional dividend reinvestment
- Saves dividend logs to a CSV file
- Displays a clear investment summary

---

## 📌 How It Works
1. **Menu** — Choose a stock (CREIT or RCR) or view their details.
2. **User Input** — Enter monthly investment amount and investment duration.
3. **Simulation** — Program calculates shares bought, dividends received, and reinvestments.
4. **CSV Export** — Dividend log saved automatically.
5. **Summary** — Displays ROI, total shares, and final portfolio value.

---

## 🖥️ Example Run
```
DRIP SIMULATION FOR RCR AND CREIT

Choose Stock:
[1] CITICORE ENERGY REIT CORP. (CREIT)
[2] RL COMMERCIAL REIT INC. (RCR)
[3] Display Stocks' Info
[4] Exit
Selection: 1

Monthly Investment: ₱5000
Investment Duration (Years): 3

Summary:
CITICORE ENERGY REIT CORP.   (CREIT)

Price per Share:        ₱3.68
Yield % (Indicated):    5.49%
Dividend Pay-out:       Quarterly
Minimum Board Lot:      1,000 shares
Monthly Investment:     ₱5,000.00
Investment Duration:    3 years
Total Investment:       ₱180,000.00
Total Shares Bought:    49,000
Total Shares Cost:      ₱180,320.00
Return on Investment:   0.18%

Open Dividend Log (Y|N)?
```

---

## 📂 Files Created
- `creit_div.csv` — Dividend log for CREIT
- `rcr_div.csv` — Dividend log for RCR

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/drip-simulator-oop.git
   ```
2. Navigate into the directory:
   ```bash
   cd drip-simulator-oop
   ```
3. Run the program:
   ```bash
   python main.py
   ```

---

## 🧠 Learning Goals
- Practice Python **classes** and **methods**
- Understand how to structure a program using **OOP principles**
- Learn how to save and read data from **CSV files**
- Improve DRIP calculation logic from a procedural approach to an object-oriented one

---

## 📅 Status
- Built while learning Python  
- No real-time data fetching  
- Fixed values for preloaded stocks  
- **Purely educational**
