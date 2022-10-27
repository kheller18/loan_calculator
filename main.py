# This script calculates loan basics and automates certain functions to output if taking a specified loan is smart
import csv
from pathlib import Path

# Part 1
  # Basic loan function to calculate length, total and average loan
def loan_basics (loans):
  length = len(loans)
  total = sum(loans)
  average_loan = total / length

  print(f"\n**** PART 1 ****")
  print(f"The number of loans is {length}.")
  print(f"The sum of loans is ${total}.")
  print(f"The average loan is ${average_loan}.")
  return average_loan

# Input loan data and function call
loan_costs = [500, 600, 200, 1000, 450]
loan_basics(loan_costs)

# Parts 2,3
  #Function that takes in a loan and prints future value and remaining months. Then calculates present value and returns to the user if the loan is worth it or not.
def present_value (loan):
  future_value = loan.get("future_value")
  remaining_months = loan.get("remaining_months")
  present_value = future_value / (1 + .2/12) ** remaining_months
  print(f"\n**** PART 2 ****")
  print(f"The future value of the loan is {future_value}.")
  print(f"The number of months remaining is {remaining_months}.")
  print(f"\n**** PART 3 ****")
  if (present_value >= future_value):
    print(f"The loan is worth at least the cost to buy it")

  else:
    print(f"The loan is too expensive and not worth the price")
  return present_value

new_loan = {
  "loan_price": 500,
  "remaining_months": 9,
  "repayment_interval": "bullet",
  "future_value": 1000
}

#function call for calculating present value
present_value(new_loan)

#Part 4
  #Function to calculate which loans are inexpensive and then print them out.
def inexpensive_loans (loans):
  inexpensive_loans = []
  for loan in loans:
    if loan["loan_price"] <= 500:
      inexpensive_loans.append(loan)

  print(f"\n**** PART 4 ****")
  print(f"The list of inexpensive loans is {inexpensive_loans}")
  return inexpensive_loans

# Seed data for loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#Function call for parsing through which loans are inexpensive
inexp_loans_output = inexpensive_loans(loans)

#Part 5
  #Function to take in inexpensive loan data, print headers and write inexpensive loan data to CSV file.
def csvWrite(loans):
  header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
  output_path = Path("inexpensive_loans.csv")

  with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for loan in loans:
      csvwriter.writerow(loan.values())
  return

csvWrite(inexp_loans_output)
