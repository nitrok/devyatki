from django.db import models


# Create your models here.
class CarNumber(models.Model):
    question_text = models.CharField(max_length=200)
    published_at = models.DateTimeField(null=True, db_index=True)

    is_approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "car_numbers"
        ordering = ["-created_at"]
