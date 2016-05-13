from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.
class OptionView(TemplateView):
    template_name = "options.html"


def switch_database(request, database):
    template_name = "options.html"
    request.session['database'] = database
    # return redirect('options')
    return render_to_response(template_name, context_instance=RequestContext(request))


def options(request):
    template_name = "options.html"

    return render_to_response(template_name, context_instance=RequestContext(request))
