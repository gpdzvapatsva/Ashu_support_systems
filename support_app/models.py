from django.db import models

# Create your models here.
class SupportWorkers(models.Model):
    Status_choices = [
        ('waiting', 'Waiting'),
        ('assigned', 'Assigned'),
        ('completed', 'Completed')
    ]
    name=models.CharField(max_length=30)
    surname=models.CharField(max_length=30)
    specialisation=models.CharField(max_length=30, blank=True)
    is_active=models.BooleanField(default=True)
    status = models.CharField(
        max_length=20,
        choices=Status_choices,
        default='waiting'
    )
    assigned_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['name']
    def __str__(self):
        return self.name
