# Business Stock Calculator

This is a simple Python program that calculates the total value of items in a small business.

---

## What it does

- It keeps a list of items the business sells.  
- It stores how many of each item are in stock.  
- It stores the price of each item.  
- It calculates the total value of all the stock.  
- It prints the total value in South African Rand (R).

---

## How it works

1. The items are stored in a list:

```python
menu = ["donut", "latte", "breakfast bun", "juice"]
The stock quantity is stored in a dictionary:

stock = {"donut": 2000,
         "latte": 3000,
         "breakfast bun": 5000,
         "juice": 10000}
The price of each item is stored in another dictionary:

price = {"donut": 50.5,
         "latte": 75.5,
         "breakfast bun": 125.5,
         "juice": 65.5}
The program goes through all items, calculates the value of each one (stock * price), and adds them together.

It prints the total stock value.

Example Output
Total stock worth: R1610000.0
How to run
Make sure Python is installed.

Save the code in a file called cafe.py.

Open Command Prompt (or Terminal) and go to the folder with cafe.py.

Run:

python cafe.py
Author
Porché Sense
