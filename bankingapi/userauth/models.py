from django.contrib.auth.models import AbstractUser


class SignUp(AbstractUser):

    def __str__(self):
        return str(self.username)
