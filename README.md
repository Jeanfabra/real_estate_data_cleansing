# real_estate_data_cleansing
Cleaning data from a slightly polluted CSV

Having as original file the output of real_estate_web_scraper (https://github.com/Jeanfabra/real_state_web_scraper) where we obtained a CSV with 
the information of some apartments in Colombia, we proceed to clean the data.

Basically, I wanted to leave the data in tabular form and replace some columns of type string to integer. 
The task did not present many inconveniences since the Data Frame used does not have many columns.
However, now we can go to a database engine and parse the information with no problem!

For the missing data on the number of bathrooms and rooms, I decided to leave them in None for a later review in MySQL.
