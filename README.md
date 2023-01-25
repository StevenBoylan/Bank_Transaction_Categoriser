# Bank Transaction Categoriser
This is a python script that takes a CSV input of monthly banking transactions separates them into "incoming" and "outgoing" transactions, then categorises each transaction. I created this script to learn how to import, process and export data in csv format. 

A future extension of this project will be functionalities to sum up transactions, totals and by category. 

## Description

This script categorises transactions from a csv file. The categoriser function is called from main with the name of the csv file.
•	categoriser.py has a series of loops that:
•	read in the data from csv,
•	get rid of unwanted data columns
•	tidies up the formats of the amounts
•	separates transactions into outgoing and incoming categories
•	then categorises the transaction according to the merchant-name in the transaction
•	saves this data to a csv file called 'final:banking.csv'

Although the code gets the job done, there are a few things that could be improved to make it more elegant and efficient.

### Dependencies

The Arrays file contains arrays with the names of merchants and their categories. This was manually created. In this file I have removed all but a couple of examples in each list.  

My raw csv file, ‘banking.csv’, is in the same directory as the code. 

## Authors

Steven Boylan

## Acknowledgments

Inspiration, code snippets, etc.
* [OpenAPI](https://openai.com/api/)

---
