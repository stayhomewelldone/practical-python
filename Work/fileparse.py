# fileparse.py
#
# Exercise 3.3
import csv
from io import TextIOWrapper

def parse_csv(lines, select=None, types=[str, int, float], has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    x = isinstance(lines, TextIOWrapper)
    if not x:
        lines = open(lines)
    rows = csv.reader(lines, delimiter=delimiter)


    if has_headers:
    # Read the file headers
        headers = next(rows)

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        if not has_headers:
            raise RuntimeError('select argument requires column headers')
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
        
    for index, row in enumerate(rows):
        try: 
            if not row:     # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [ row[index] for index in indices ]
            if types: 
                row = [ func(val) for func, val in zip(types, row)]
            # Make a dictionary
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as e:
            if not silence_errors:
                print(f'Row {index} can\'t be converted {row}')
                print(e)
    
    return records

