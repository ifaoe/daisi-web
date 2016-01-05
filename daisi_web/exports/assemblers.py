import xlsxwriter as xw

def bsh_export(session):
    workbook = xw.Workbook('bsh_export-%s' % session)
    workbook.add_worksheet('Tripdaten')
    


