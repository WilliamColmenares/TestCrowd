from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.CharField(max_length=3, choices=(("Cat", "Cat"), ("Dog", "Dog")))
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True)

    def __str__(self):
        return f'Pet: {self.pet} | Name: {self.name} | birthday: {self.birthday}'
