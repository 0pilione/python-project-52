from django.db import models
from django.db.models import ProtectedError
from django.utils.translation import gettext_lazy as _


class Labels(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        if self.tasks.exists():
            raise ProtectedError(
                _('Cannot delete label'),
                self
            )
        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
