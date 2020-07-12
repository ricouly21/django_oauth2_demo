from django.contrib import admin

from accounts.models import Account


@admin.register(Account)
class AccountsAdmin(admin.ModelAdmin):

    @staticmethod
    def username(instance):
        return instance.user.username

    @staticmethod
    def first_name(instance):
        return instance.user.first_name

    @staticmethod
    def last_name(instance):
        return instance.user.last_name

    list_display = [
        'username',
        'first_name',
        'last_name',
        'dob'
    ]

