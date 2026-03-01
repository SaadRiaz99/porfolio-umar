from django.db import models


class Contact_message(models.model):
    name = models.CharField(max_length=50 , null=True , blank=True)
    email = models.EmailField(max_length=100 , null=True , blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def _str__(self):
        return f"{self.name} and {self.email}" 

