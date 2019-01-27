from django.http import HttpResponse

from django.template import loader

def index(request):
    # getting template
    template = loader.get_template('index.html')

    # render template
    return HttpResponse(template.render())