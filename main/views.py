import hashlib
from django.shortcuts import render_to_response
from django.template import RequestContext
from hideURL.main.models import *
from django.core.context_processors import csrf

def hideURL(request, md5sum=None):
    hideURL = None
    new_hideURL = None

    if request.method == 'POST':
        if request.POST.has_key('direct_url'):
            direct_url = request.POST['direct_url']
            md5sum = hashlib.md5(request.POST['direct_url']).hexdigest()
            try:
                new_hideURL = HideURL.objects.get(md5sum = md5sum)
            except HideURL.DoesNotExist:
                new_hideURL = HideURL(md5sum = md5sum, url = direct_url)
                new_hideURL.save()
    elif md5sum:
        try:
            hideURL = HideURL.objects.get(md5sum = md5sum)
        except HideURL.DoesNotExist:
            pass

    context = {
        'hideURL': hideURL,
        'new_hideURL': new_hideURL,
    }
    #r = {}
    #r.update(csrf(request))
    return render_to_response('main/hideURL.html', context,
        context_instance = RequestContext(request))

