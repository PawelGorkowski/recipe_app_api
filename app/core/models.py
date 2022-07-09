"""
Database models.
"""

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Recipe(models.Model):
    """Recipe object."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        """Return string representation of the object."""
        return self.title

    # def get_absolute_url(self):
    #     """Return URL for recipe detail."""
    #     return f"/recipe/{self.id}"

    # def get_total_price(self):
    #     """Return total price of the recipe."""
    #     return self.price * self.time_minutes

    # def get_total_time(self):
    #     """Return total time of the recipe."""
    #     return self.time_minutes

    # def get_ingredients(self):
    #     """Return list of ingredients."""
    #     return self.ingredient_set.all()

    # def get_steps(self):
    #     """Return list of steps."""
    #     return self.step_set.all()

    # def get_tags(self):
    #     """Return list of tags."""
    #     return self.tag_set.all()
