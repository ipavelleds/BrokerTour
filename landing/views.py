#coding: utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import Tour, Proposal
from forms import ProposalForm
import json


def landing_render(request):
    return render(request, 'index.html', {"tours": Tour.objects.all()})


def send_order(request):
    if request.method == 'POST':
        try:
            current_tour = Tour.objects.get(id=int(request.POST.get('tour')))
        except Tour.DoesNotExist:
            tours = Tour.objects.all()
            if tours:
                current_tour = tours[0]
            else:
                raise Exception('You should create at least one tour item')
        if request.POST["phone"]:
            try:
                proposal = Proposal.objects.get(phone=request.POST["phone"])
                # if we still here the client has already sent request
                form = ProposalForm(request.POST, instance=proposal)
            except Proposal.DoesNotExist:
                # new client
                form = ProposalForm(request.POST)
            if form.is_valid():
                data = json.dumps({"success": True})
                form.save()
            else:
                data = json.dumps({"success": False})
            return HttpResponse(data, content_type='application/json')
        else:
            data = json.dumps({"success": False, "error": "Не указан телефон"})
            return HttpResponse(data, content_type='application/json')
    return redirect('/')