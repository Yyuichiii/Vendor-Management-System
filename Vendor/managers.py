from django.contrib.auth.models import BaseUserManager


class MyVendorManager(BaseUserManager):
    def create_user(self, vendor_code,name,contact_details=None,address=None,password=None,password2=None):
        """
        Creates and saves a User with the given vendor_code, name and password.
        """
        if not vendor_code:
            raise ValueError("Users must have an vendor_code")

        user = self.model(
            vendor_code=vendor_code,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, vendor_code, name,password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            vendor_code,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user