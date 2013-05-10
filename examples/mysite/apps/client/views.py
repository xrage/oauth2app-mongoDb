#-*- coding: utf-8 -*-


from django.shortcuts import render_to_response
from django.template import RequestContext
from oauth2app.models import Client, AccessToken, Code
from base64 import b64encode
from django.contrib.auth.decorators import login_required

@login_required
def client(request, client_id):
    client = Client.objects.get(key=client_id)
    template = {
        "client":client,
        "basic_auth":"Basic %s" % b64encode(client.key + ":" + client.secret),
        "codes":Code.objects.filter(user=request.user, client=client.id),
        "access_tokens":AccessToken.objects.filter(user=request.user, client=client.id)}
    template["error_description"] = request.GET.get("error_description")
    return render_to_response(
        'client/client.html', 
        template, 
        RequestContext(request))