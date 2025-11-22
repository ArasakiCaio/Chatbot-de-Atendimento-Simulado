from django.db import models

class User(models.Model):
    userTypes = (
        ('A', 'User A'),
        ('B', 'User B'),
    )

    type = models.CharField(
        max_length=1,
        choices=userTypes,
        unique=True,
    )

    def __str__(self):
        return f"Usuário {self.userTypes}"
    
class Message(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='messages'
    )
    text = models.TextField()
    date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Mensagem de {self.user} - {self.date.strftime('%d/%m/%Y %H:%M')}"
    
class Response(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        related_name='response'
    )
    text = models.TextField()
    date = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"Resposta para {self.message.user} = {self.date.strftime('%d/%m/%Y %H:%M')}"