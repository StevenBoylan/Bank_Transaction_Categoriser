# Working

import csv
import pandas as pd
import Arrays


# create lists to hold the tuples taken from the CSV ()
transactions = [] # list of transactions with category defined
full_transactions = [] # full list of all transactions

def categoriser(csv_filename):
  # Open input CSV with raw data as csvfile
  with open(csv_filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for transaction in csvreader:            # Loop through each transaction to get values for Date, Name and Transaction Ammount
      date = transaction[0]
      name = transaction[2]
      ammount = transaction[7]
      temp_transaction = (date, name, ammount)     # save these values as a list

    # The CSV figures come out in a mixed format, using a "." as a 1000s seperator and another as a decimal point.
    # This loop checks the "ammount" value and if there are two decimal points, gets rid of the first one
    # numbers are output in the format "1000.00" instead of "1.000.00"

      for value in ammount:
        count = ammount.count('.')
        if count == 2:
          first_point = ammount.index('.')
          new_ammount = ammount[:first_point] + ammount[first_point + 1:]
          ammount = new_ammount
          temp_transaction = (date, name, ammount)

      # In order to sum up figures, it is necessary to seperate values into a positive and negative colum
      # The following loop checks for the presences of a "-", if found, the negative value is save as outgoing
      # otherwise it is saved as incomming

      outgoing = ""
      incomming = ""
      for line in temp_transaction[2]:
        if "-" in temp_transaction[2]:
          outgoing = temp_transaction[2]
        else:
          incomming = temp_transaction[2]
      # The category variable in the list is initially defined
      # as "Undefined" as a catch-all for unknown transactions
      category = ('Undefined')
      # Create a temporary list to hold the current values of
      # date, name, outgoing, incomming, category
      temp_transaction = (date, name, outgoing, incomming, category)
      full_transactions.append(temp_transaction)        # append this to the full transaction list

      # Now we need to add the categories section. Up until this point category is Undefined
      # Check for merchant names in the lists. If there, add category and append to transactions list

      for super in Arrays.SUPERMARKETS:
        if super in transaction[2]:
          category = "Food Shopping"
          temp_transaction = (date, name, outgoing, incomming, category)
          transactions.append(temp_transaction)

      for travel in Arrays.TRAVEL:
        if travel in transaction[2]:
          category = "Travel"
          temp_transaction = (date, name, outgoing, incomming, category)
          transactions.append(temp_transaction)

      for subs in Arrays.SUBSCRIPTIONS:
        if subs in transaction[2]:
          category = "Subscription Service"
          temp_transaction = (date, name, outgoing, incomming, category)
          transactions.append(temp_transaction)

      for shopping in Arrays.SHOPPING:
        if shopping in transaction[2]:
          category = "Other Shopping"
          temp_transaction = (date, name, outgoing, incomming, category)
          transactions.append(temp_transaction)

      for entert in Arrays.ENTERTAINMENT:
        if entert in transaction[2]:
          category = "Cafe's, Restaurants & Entertainment"
          temp_transaction = (date, name, outgoing, incomming, category)
          transactions.append(temp_transaction)

      for serv in Arrays.SERVICES:
        if serv in transaction[2]:
          category = "Services and Utilities"
          temp_transaction = (date, name, outgoing, incomming, category)
          transactions.append(temp_transaction)

      # compare the tuples and remove duplicates of name, date and amount
      for x in transactions:
        for y in full_transactions:
          if x[0] == y[0] and x[1] == y[1] and x[2] == y[2]:
            full_transactions.remove(y)

      # create a list to hold the final transactions,
      # then append the categorised and uncategorised lists and print to csv file
      final_transactions = []
      final_transactions = full_transactions + transactions
      df = pd.DataFrame(final_transactions)
      df.to_csv('final_banking.csv', index = False, header=True)
