# This script calculates loan basics

# Part 2
  # Basic loan function to calculate length, total and average loan
def loan_basics (loans):
  length = len(loans)
  total = sum(loans)
  average_loan = total / length

  print(f"The number of loans is {length}.")
  print(f"The sum of loans is ${total}.")
  print(f"The average loan is ${average_loan}.")
  return

# Input loan data and function call
loan_costs = [500, 600, 200, 1000, 450]
loan_basics(loan_costs)

# Part 3
