from django.shortcuts import render, redirect
from django.views.generic.base import View
from .form import CommentsForm
from .models import Ticket


class TicketView(View):
    def get(self, request):
        tickets = Ticket.objects.all()
        return render(request, 'site_tb/site_tb.html', {'ticket_list': tickets})


class TicketDetail(View):
    def get(self, request, ticket_slug):
        ticket = Ticket.objects.get(slug=ticket_slug)
        return render(request, 'site_tb/question.html', {'ticket': ticket})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect('/')


