from django.db import models

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    year = models.CharField(max_length=50) # e.g. "2023 - 2024"
    category = models.CharField(max_length=50) # e.g. "cert", "award", "academic", "project"
    description = models.TextField()
    icon = models.CharField(max_length=50, default="award") # Lucide icon name
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} @ {self.organization}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300) # technologies used
    date = models.CharField(max_length=50)
    description = models.TextField() # Supports markdown or bullet points
    tags = models.CharField(max_length=200) # comma separated
    doc_link = models.URLField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100) # SimpleIcons slug
    description = models.CharField(max_length=300)
    energy = models.IntegerField(default=80) # 0 to 100
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
