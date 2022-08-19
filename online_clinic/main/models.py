from django.db import models

class Divisions(models.Model):
    name = models.CharField(max_length=100, verbose_name='Подразделения')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.name}: {self.description}"

class Patient(models.Model):
    data_of_birth = models.DateField(verbose_name='Дата Рождения')
    divisions = models.ForeignKey(Divisions, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{self.data_of_birth}: {self.divisions}"