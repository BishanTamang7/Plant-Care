from django.db import models
from django.conf import settings

class Plant(models.Model):
    CATEGORY_CHOICES = [
        ("indoor", "Indoor"),
        ("outdoor", "Outdoor"),
        ("succulent", "Succulent"),
        ("flowering", "Flowering"),
        ("herbal", "Herbal"),
    ]

    CARE_LEVEL_CHOICES = [
        ("easy", "Easy"),
        ("moderate", "Moderate"),
        ("difficult", "Difficult"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="plants/")
    care_instructions = models.TextField()
    care_level = models.CharField(
        max_length=10,
        choices=CARE_LEVEL_CHOICES,
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="plants",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.category})"