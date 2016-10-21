# Excel .xlsx export routines using xlsxwriter
#
# xlsxwriter: http://xlsxwriter.readthedocs.org/


import xlsxwriter as xw
from io import BytesIO
from django.db import connections
from django.shortcuts import HttpResponse


def bsh_export(session):
    # get ftz version for export
    cursor = connections['jalapeno'].cursor()
    cursor.execute("SELECT DISTINCT regexp_replace(version, '[^0-9]+','','g') FROM projects WHERE project_id=%s", (session,))
    version_entry = cursor.fetchone()[0]

    # create output as bytefile in  memory
    output = BytesIO()

    # create the workbook and the first worksheet containing the BSH tripdata
    # keep the whole workbook in memory
    workbook = xw.Workbook(output, {'in_memory': True})
    trip_sheet = workbook.add_worksheet('Tripdaten')

    # get the database connection cursor from django
    cursor = connections['jalapeno'].cursor()
    cursor.execute('SELECT * FROM daisi_web.bsh_trip_view_ftz' + version_entry + ' WHERE cruiseno=%s', (session,))

    # get a list of description tuples containing column names, type, etc.
    description = cursor.description

    # Get the column names and write them to the first line
    for idx, name in enumerate(description):
        trip_sheet.write(0, idx, name[0])

    # iterate through the query result
    # write results to the corresponding column and row
    for idx, result in enumerate(cursor.fetchall()):
        for idy, entry in enumerate(result):
            trip_sheet.write(idx+1, idy, entry)

    # repeate for base and observation data
    base_sheet = workbook.add_worksheet('Basisdaten')

    cursor = connections['jalapeno'].cursor()
    cursor.execute('SELECT * FROM daisi_web.bsh_base_view_ftz' + version_entry + ' WHERE cruiseno=%s', (session,))

    description = cursor.description

    for idx, name in enumerate(description):
        base_sheet.write(0, idx, name[0])

    for idx, result in enumerate(cursor.fetchall()):
        for idy, entry in enumerate(result):

            base_sheet.write(idx+1, idy, entry)

    observation_sheet = workbook.add_worksheet('Observations')

    cursor = connections['jalapeno'].cursor()
    cursor.execute('SELECT * FROM daisi_web.bsh_observation_view_ftz' + version_entry + ' WHERE cruiseno=%s', (session,))

    description = cursor.description

    for idx, name in enumerate(description):
        observation_sheet.write(0, idx, name[0])

    for idx, result in enumerate(cursor.fetchall()):
        for idy, entry in enumerate(result):
            observation_sheet.write(idx+1, idy, entry)

    workbook.close()

    # find correct position in byte-stream
    output.seek(0)

    # return bytefile from memory ready to get written
    return output.read()


def single_table_export(session, table):
    # create output as bytefile in  memory
    output = BytesIO()

    # create the workbook and the first worksheet containing the BSH tripdata
    # keep the whole workbook in memory
    workbook = xw.Workbook(output, {'in_memory': True})
    trip_sheet = workbook.add_worksheet()

    # get the database connection cursor from django
    cursor = connections['jalapeno'].cursor()
    #!!!!
    #!!!! TODO:
    #!!!!
    # EXTREMLY dangerous
    # Have to validate the tablename beforehand or hardcode it!
    # Use dictionary with check
    if table not in ('daisi_qa_wrong_image', 'daisi_qa_double_mark', 'daisi_qa_double_anthro'):
        return "Error: Table does not exist."

    cursor.execute("SELECT * FROM daisi_web." + table + " WHERE session=%s", (session,))

    # get a list of description tuples containing column names, type, etc.
    description = cursor.description

    # Get the column names and write them to the first line
    for idx, name in enumerate(description):
        trip_sheet.write(0, idx, name[0])

    # iterate through the query result
    # write results to the corresponding column and row
    for idx, result in enumerate(cursor.fetchall()):
        for idy, entry in enumerate(result):
            trip_sheet.write(idx, idy, entry)

    workbook.close()

    # find correct position in byte-stream
    output.seek(0)

    # return bytefile from memory ready to get written
    return output.read()


def handle_exports(export_type, export_format, export_session):
    if export_format == 'xlsx':
        xlsx_data = None
        if export_type == 'bsh':
            xlsx_data = bsh_export(export_session)
        else:
            xlsx_data = single_table_export(export_session, export_type)
        response = HttpResponse(xlsx_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s-%s.xlsx' % (export_type, export_session)
    return response
