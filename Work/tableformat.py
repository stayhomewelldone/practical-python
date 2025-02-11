


class FormatError(Exception):
    pass
class TableFormatter:
    def headings(self, headers):

        '''
        Emit the table headings.
        '''

        raise NotImplementedError
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        
        print()
        print(('-' * 10 + ' ') * len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
 
class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''

    def headings(self, headers):
        print(','.join(headers))
    
    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format:
    '''

    def headings(self, headers):
        print("<tr>", end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')
        
    
    def row(self, rowdata):
        print('<tr>', end='')
        for row in rowdata:
            print(f'<td>{row}</td>', end='')
        print('</tr>')

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError('Unknown table format %s' % fmt)
    return formatter

def print_table(portfolio, columns=[''], fmt=TextTableFormatter):
    '''
    Function for printing the report
    '''
    fmt.headings(columns)
    rowdata=[]
    for obj in portfolio:
          rowdata = [ str(getattr(obj,name)) for name in columns ]
          fmt.row(rowdata)