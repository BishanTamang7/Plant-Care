from django.db import models
from django.conf import settings
from nursery.models import Plant

class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wishlists"
    )
    plant = models.ForeignKey(
        Plant, on_delete=models.CASCADE, related_name="wishlisted_by"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'plant')

    def __str__(self):
        return f"{self.user.username} → {self.plant.name}"