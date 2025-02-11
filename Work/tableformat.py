class TableFormatter:
    def headings(self, headers):

        '''
        Emit the table headings.
        '''
        print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
        print(('-' * 10 + ' ') * len(headers))

        raise NotImplementedError
    
    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError