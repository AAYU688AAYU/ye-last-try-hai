from django.conf import settings
from django.db import models

class Diagnosis(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='diagnoses'
    )
    fundus_image = models.ImageField(upload_to='fundus_images/')
    erg_data = models.FileField(upload_to='erg_data/', blank=True, null=True)
    result = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s diagnosis - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class ColorBlindTest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fundus_image = models.ImageField(upload_to='fundus_images/')
    erg_data = models.FileField(upload_to='erg_data/', null=True, blank=True)
    result_type = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    confidence = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s test - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class BloodTest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    report = models.FileField(upload_to='blood_reports/')
    hemoglobin = models.FloatField(null=True, blank=True)
    wbc = models.FloatField(null=True, blank=True)
    platelets = models.IntegerField(null=True, blank=True)
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
