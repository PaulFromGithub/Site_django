from django.contrib import admin
from .models import Ticket, Comments, Question, Answer


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text_questions', 'question')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text_answer', 'answer')