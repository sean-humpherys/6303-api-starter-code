# DO NOT change this code. You may view the code to see how the unit test functions
# Purpose: Tests if the stock data is imported correctly

import sqlite3

db_name = "Stock data.db"
correct_record_count = 205

with sqlite3.connect(db_name) as conn:
    print("----- Test 1 -----")
    # Test Record count
    sql_command = "Select count(*) from Prices"
    cursor = conn.execute(sql_command)
    for row in cursor:
        if row[0] == correct_record_count:
            print(f"*** PASSES. Record count correct {correct_record_count}.")
        else:
            print(
                f"*** FAIL. Record Count: {row[0]}. Should be {correct_record_count}. Need to try again.")
    print("----- Test 2 -----")

    # Test for not removing the column names from the source files.
    correct_record_count = 0  # should not have text in the numeric fields
    sql_command = "Select count(*) from Prices where Date = 'Date' or ClosingPrice = 'ClosingPrice' or Volume = 'Volumne'"
    cursor = conn.execute(sql_command)
    for row in cursor:
        if row[0] > correct_record_count:
            print(f"*** FAIL. Column headers were not removed from the source files before importing the data. Need to try again.")
        else:
            print(
                f"*** PASSES. Column headers successful removed before importing data. ")
    print("----- Test 3 -----")

    # Test for correct data values
    correct_record_count = 5
    sql_command = "Select count(*) from Prices where Date in ('10/20/2022', '9/13/2022', '6/30/2022','4/1/2022', '1/12/2022' )"
    cursor = conn.execute(sql_command)
    for row in cursor:
        if row[0] == correct_record_count:
            print(f"*** PASSES. Found correct data values.")
        else:
            print(
                f"*** FAIL. Missing key data vales or data is duplicated. Need to try again. ")
