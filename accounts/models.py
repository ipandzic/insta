from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """Create and save a User with the given email and password."""
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """Create and save a SuperUser with the given username and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)







class User(AbstractUser):
    objects = UserManager()
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="followed_by")
    email = models.EmailField(unique=True, blank=True)
    REQUIRED_FIELDS = []











# class UserProfileManager(models.Manager):
#     use_for_related_fields = True

#     def all(self):
#         qs = self.get_queryset().all()
#         try:
#             if self.instance:
#                 qs = qs.exclude(user=self.instance)
#         except:
#             pass
#         return qs

#     def toggle_follow(self, user, to_toogle_user):
#         user_profile, created = UserProfile.objects.get_or_create(user=user)
#         if to_toogle_user in user_profile.following.all():
#             user_profile.following.remove(to_toogle_user)
#             added = False
#         else:
#             user_profile.following.add(to_toogle_user)
#             added = True
#         return added

#     def is_following(self, user, followed_by_user):
#         user_profile, created = UserProfile.objects.get_or_create(user=user)
#         if created:
#             return False
#         if followed_by_user in user_profile.following.all():
#             return True
#         return False

#     def recommended(self, user, limit_to=10):
#         profile = user.profile
#         following = profile.get_following()
#         qs = self.get_queryset().exclude(user__in=following).exclude(id=profile.id).order_by("?")
#         return qs



# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE)
#     following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="followed_by")

 
#     objects = UserProfileManager()

#     def __str__(self):
#         return str(self.following.all().count())

#     def get_following(self):
#         users = self.following.all()
#         return users.exclude(username=self.user.username)

#     def get_follow_url(self):
#         return reverse_lazy("profiles:follow", kwargs={"username": self.user.username})

#     def get_absolute_url(self):
#         return reverse_lazy("profiles:detail", kwargs={"username": self.user.username})


# def post_save_user_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         new_profile = UserProfile.objects.get_or_create(user=instance)

# post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)
