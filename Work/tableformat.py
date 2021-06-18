# tableformat.py
#
class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headers
        '''
        raise NotImplementedError()
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Output data in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
    
class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print('<th>%s</th>' % h, end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>%s</td>' % d, end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name
    '''
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {fmt}')
    
    return formatter

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [ str(getattr(obj, colname)) for colname in columns ]
        formatter.row(rowdata)