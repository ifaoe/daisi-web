#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db import connections
from math import floor

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import TemplateView
from django.shortcuts import render_to_response


class ProjectData(TemplateView):
    template_name = "status.html"

    def project_list(self):
        cursor = connections['jalapeno'].cursor()
        cursor.execute(
            "SELECT DISTINCT owpas, year, session FROM daisi_web.web_view_project_list ORDER BY owpas, year, session DESC")
        project_dictionary = {};
        for owpas, year, session in cursor.fetchall():
            project_dictionary.setdefault(owpas, {}).setdefault(year, []).append(session)
        return project_dictionary


def session_progress(request, session):
    template_name = "status_session.html"
    cursor = connections['jalapeno'].cursor()
    cursor.execute("SELECT project FROM daisi_web.web_view_project_list WHERE session=%s AND project NOT LIKE %s", (session,'Test%',))
    projects = []
    for row in cursor.fetchall():
        projects.append(row[0])
    return render_to_response(template_name, {'projects': projects})


def project_progress(request, project):
    template_name = "status_project.html"
    cursor = connections['jalapeno'].cursor()
    cursor.execute("SELECT * FROM daisi_web.census_status WHERE session=%s", (project,))
    res = cursor.fetchone()
    if res is None:
        return render_to_response("status_project_404.html", {'session': project})
    (session, count, pre, final, conflict) = res

    cursor.execute("SELECT count, rejected, watched FROM daisi_web.raw_census_status WHERE project=%s", (project,))
    (pre_count, rejected, watched) = cursor.fetchone()
    data = {
        'session': session,
        'count': count,
        'pre_p': floor(pre / count * 100),
        'pre': pre,
        'final_p': floor(final / count * 100),
        'final': final,
        'conflict_p': floor(conflict / count * 100),
        'conflict': conflict,
        'pre_count': pre_count,
        'pre_clean': pre_count - rejected,
        'rejected': rejected,
        'rejected_p': floor(rejected / pre_count * 100),
        'watched': watched,
        'watched_p': floor(watched / (pre_count - rejected) * 100)
    }
    return render_to_response(template_name, data)
