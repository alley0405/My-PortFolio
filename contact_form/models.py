from django.db import models

class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    project_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
