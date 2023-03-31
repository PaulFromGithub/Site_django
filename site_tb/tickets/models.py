from django.db import models


class Ticket(models.Model):
    title = models.CharField('Номер билета', max_length=100)
    author = models.CharField('Автор', max_length=100)
    date = models.DateField('Дата публикации')
    img = models.ImageField('Изображение', upload_to='image/%Y')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    text_questions = models.TextField('Текст вопроса')
    question = models.ForeignKey(Ticket, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.text_questions}'


class Answer(models.Model):
    text_answer = models.TextField('Текст ответа')
    answer = models.ForeignKey(Question, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'{self.text_answer}'


class Comments(models.Model):
    """Комментарий"""
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст комментария')
    post = models.ForeignKey(Ticket, verbose_name='Публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name}, {self.post}'
