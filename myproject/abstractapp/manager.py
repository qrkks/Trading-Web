from django.db import models
from typing import List
from django.db.models import QuerySet


class CommonManager(models.Manager):
    def active(self) -> QuerySet:
        """
        Returns a QuerySet of active objects.

        Args:
            self: The instance of the class.

        Returns:
            QuerySet: A QuerySet of active objects.
        """
        return self.filter(is_active=True)

    def inactive() -> List:
        """Filter out the inactive items.

        Returns:
            List: A list of inactive items.
        """
        return filter(is_active=False)
