# from dataclasses import field
from pyexpat import model
from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from .models import Ticket
# Create your views here.
class CreateTicket(CreateView):
    model  = Ticket
    fields = ['ticket_title','ticket_description']
    template_name = 'ticket/create_ticket.html'
    success_url = '/ticket/view'

class DeleteTicket(DeleteView):
    model = Ticket
    template_name = 'ticket/delete_ticket.html'
    success_url = '/ticket/view'

def index(request):
     return render(request, 'ticket/index.html')

class UpdateTicket(UpdateView):
    model = Ticket
    fields = ['ticket_title','ticket_description']
    template_name = 'ticket/update_ticket.html'

