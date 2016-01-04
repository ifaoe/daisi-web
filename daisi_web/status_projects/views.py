#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db import connections

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
    
class ProjectData(TemplateView):
    template_name = "status.html"
    def project_list(self):
        cursor = connections['jalapeno'].cursor()
        cursor.execute("SELECT owpas, year, session, project FROM daisi_web.web_view_project_list WHERE project NOT LIKE 'Test%' ORDER BY owpas, year, session DESC")
        project_dictionary = {};
        for owpas, year, session, project in cursor.fetchall():
            project_dictionary.setdefault(owpas,{}).setdefault(year,{}).setdefault(session,[]).append(project)
        return project_dictionary

def ProjectProgress(request, project):
    template_name = "status_project.html"
    cursor = connections['jalapeno'].cursor()
    cursor.execute("SELECT * FROM daisi_web.census_status WHERE session=%s",(project,))
    res = cursor.fetchone()
    if res is None:
        return render_to_response("status_project_404.html", {'session':project})
    (session, count, pre, final, conflict) = res

    cursor.execute("SELECT count, rejected, watched FROM daisi_web.raw_census_status WHERE session=%s",(project,))
    (pre_count, rejected, watched) = cursor.fetchone()
    data = {
        'session': session,
        'count': count,
        'pre_p': round(pre/count*100),
        'pre': pre,
        'final_p': round(final/count*100),
        'final': final,
        'conflict_p': round(conflict/count*100),
        'conflict': conflict,
        'pre_count': pre_count,
        'pre_clean': pre_count-rejected,
        'rejected': rejected,
        'rejected_p': round(rejected/pre_count*100),
        'watched': watched,
        'watched_p': round(watched/(pre_count-rejected)*100)
    }
    return render_to_response(template_name, data)




