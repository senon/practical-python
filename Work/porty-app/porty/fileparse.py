# fileparse.py
#
# Exercise 3.4-3.7
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with selecting out columns of interest 
    and type conversions.
    '''
    # if select != None and has_headers == False:
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    records = []
    rows = csv.reader(file, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering 
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select
    
    for rowno, row in enumerate(rows, start=1):
        if not row:     # Skip rows with no data
            continue
        
        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices ]
        
        # Apply type conversion to the row
        if types:
            try:
                row = [ func(val) for func, val in zip(types, row) ]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        # Make a dictionary or a tuple
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)                
        records.append(record)

    return records
