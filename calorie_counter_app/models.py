from django.db import models

# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"

    class Meta:
        ordering = ['-created_at']