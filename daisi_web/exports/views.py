from django.shortcuts import render
from django.shortcuts import render_to_response
from django.db import connections
from django.shortcuts import HttpResponse, Http404, redirect
import json

from django.views.generic import TemplateView
from daisi_web.exports.assemblers import bsh_export, single_table_export, handle_exports
from daisi_web.exports.forms import ExportForm


# Create your views here.

def get_sessions(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        cursor = connections['jalapeno'].cursor()
        cursor.execute("SELECT DISTINCT session FROM daisi_web.project_list WHERE lower(session) LIKE lower(%s) ORDER BY session DESC",('%'+q+'%',))

        results = []
        for row in cursor.fetchall():
            session_json = {}
            session_json['id'] = row[0]
            session_json['label'] = row[0]
            session_json['value'] = row[0]
            results.append(session_json)

        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


class ExportView(TemplateView):
    template_name = "exports.html"


def get_excel(request):
    if 'excel' in request.POST:
        export = request.POST.get("export")
        session = request.POST.get("session")
        if export == "bsh_export":
            xlsx_data = bsh_export(session)
        else:
            xlsx_data = single_table_export(session, export)

        response = HttpResponse(xlsx_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s-%s.xlsx' % (export, session)
        return response
    else:
        return Http404


def get_export_data(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExportForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            export_session = form.cleaned_data['export_session']
            export_type = form.cleaned_data['export_type']
            export_format = form.cleaned_data['export_format']
            return redirect('export_running', session=export_session, export=export_type, filetype=export_format)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExportForm()

    return render(request, 'exports.html', {'form': form})


class ExportRunning(TemplateView):
    template_name = "export_running.html"


def process_export(request, session, export, filetype):
    if filetype == 'xlsx':
        xlsx_data = None
        if export == 'bsh':
            xlsx_data = bsh_export(session)
        else:
            xlsx_data = single_table_export(session, export)
        response = HttpResponse(xlsx_data, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s-%s.xlsx' % (export, session)
    return response
