from django.db import models
from django.contrib.auth import get_user_model
from crum import get_current_user

# Create your models here.

User = get_user_model()




class AbstractCommonModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='+', blank=True, null=True,
                                   default=None, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(User, related_name='+', blank=True, null=True,
                                   default=None, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
        ordering = ["-update_time"]

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super(AbstractCommonModel, self).save(*args, **kwargs)



class UserProfile(AbstractCommonModel):
    user = models.OneToOneField(User, models.CASCADE,
                                help_text="Specify a computer system login name for the person.")

    full_name = models.CharField(max_length=200, blank=True, null=True,
                                 help_text="Persons name that is not their surname nor their middle name "
                                           "(i.e., their first name).")

    sur_name = models.CharField(max_length=200, blank=True, null=True,
                                help_text="Persons individuals parent or assumed by marriage, and by which the"
                                          " individual is commonly known.")

    email = models.CharField(max_length=200, blank=True, null=True, help_text="Mail box addresses for the person.")
    mobile_num = models.CharField(max_length=32, blank=True, null=True, default=None,
                                  help_text="Personal Phone number.")
    dark_mode = models.BooleanField(default=False)