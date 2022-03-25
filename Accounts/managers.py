from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,**extra_fields):
        """

        to create our custom user with this cutomusermanger function create user

        """

        if not email:
            raise ValueError(("Please provide email"))
        
        email = self.normalize_email(email).lower()
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        """
        creating super user with this custom made fimction inside our cutom made user manager extended by BaseUserManager with
        given password anf email and phone no

        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('superuser must have staff=true'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('superuser must have superuser=true'))
        return self.create_user(email, password,**extra_fields)
        # return self.create_user(email,phone_no,password,**extra_fields)

        
