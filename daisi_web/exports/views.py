from django.shortcuts import render
from django.db import connections
from django.shortcuts import render_to_response

# Create your views here.

def BshExport(request, project):
    template_name = "export.html"
    cursor = connections['jalapeno'].cursor()
    cursor.execute("SELECT * FROM daisi_web.census_status WHERE session=%s",(project,))
    (session, count, pre, final, conflict) = cursor.fetchone()
    data = {
        'session': session,
        'count': count,
        'pre_p': round(pre/count*100),
        'pre': pre,
        'final_p': round(final/count*100),
        'final': final,
        'conflict_p': round(conflict/count*100),
        'conflict': conflict
    }
    return render_to_response(template_name, data)