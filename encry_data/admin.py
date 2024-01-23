from django.contrib import admin
# Register your models here.
from encry_data.models import UserBankInformation


@admin.register(UserBankInformation)
class UserThemeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'bank_account', 'bank_pin'
    )
