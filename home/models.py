from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email= models.CharField(max_length=50)

    #def __repr__(self):
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email}"
    

