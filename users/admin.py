from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import User
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class UserForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email already used")
        return email

    class Meta:
        model = User
        exclude = ()


class UserCreationForm(UserForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
       (None, {'fields': ('email', 'password')}),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'groups', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', )
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    add_form = UserCreationForm

admin.site.register(User, UserAdmin)