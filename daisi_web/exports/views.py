from django.shortcuts import render
from django.shortcuts import render_to_response
from django.db import connections
from django.shortcuts import HttpResponse, Http404
import json

from django.views.generic import TemplateView


# Create your views here.

def get_sessions(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        cursor = connections['jalapeno'].cursor()
        cursor.execute("SELECT DISTINCT session FROM daisi_web.project_list WHERE session LIKE %s ORDER BY session DESC",('%'+q+'%',))

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


def get_excel(request, session, export):
    if 'excel' in request.POST:
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=%s-%s.xlsx' % (session, export)
        xlsx_data = WriteToExcel(weather_period, town)
        response.write(xlsx_data)
        return response
    else:
        return Http404

