from django.shortcuts import render, redirect
from django.views.generic.base import View
from .form import CommentsForm
from .models import Ticket


class TicketView(View):
    def get(self, request):
        tickets = Ticket.objects.all()
        return render(request, 'site_tb/site_tb.html', {'ticket_list': tickets})


class TicketDetail(View):
    def get(self, request, pk):
        ticket = Ticket.objects.get(id=pk)
        return render(request, 'site_tb/question.html', {'ticket': ticket})


class QuestionDetail(View):
    def get(self, request):
        return render(request, 'site_tb/answer.html')


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post.id = pk
            form.save()
        return redirect(f'/{pk}')


