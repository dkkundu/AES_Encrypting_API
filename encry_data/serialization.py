from rest_framework import serializers
from encry_data.models import UserBankInformation
from .system import decrypt


key = 'AAAAAAAAAAAAAAAA'  # Must Be 16 char for AES128


class UserBankInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBankInformation
        fields = ("name", "email", "bank_account", "photo", "bank_pin", "ref")
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
            'bank_account': {'required': True},
            'photo': {'required': True},
            'bank_pin': {'required': True},
            'ref': {'required': True},
        }


class BankInformationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=True)
    email = serializers.CharField(max_length=255, required=True)
    bank_account = serializers.CharField(max_length=255, required=True)
    photo = serializers.CharField(max_length=255, required=True)


class UserBankInformationSerializer2(serializers.ModelSerializer):
    print()
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    bank_account = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()
    bank_pin = serializers.SerializerMethodField()
    ref = serializers.SerializerMethodField()

    class Meta:
        model = UserBankInformation
        fields = ("name", "email", "bank_account", "photo", "bank_pin", "ref")

    def get_name(self, obj):
        bytes_part = obj.name.split("'")[1]
        return str(decrypt(bytes_part.encode('utf-8'), key)).split("'")[1]

    def get_email(self, obj):
        bytes_part = obj.email.split("'")[1]
        return str(decrypt(bytes_part.encode('utf-8'), key)).split("'")[1]

    def get_bank_account(self, obj):
        bytes_part = obj.bank_account.split("'")[1]
        return str(decrypt(bytes_part.encode('utf-8'), key)).split("'")[1]

    def get_photo(self, obj):
        bytes_part = obj.photo.split("'")[1]
        return str(decrypt(bytes_part.encode('utf-8'), key)).split("'")[1]

    def get_bank_pin(self, obj):
        bytes_part = obj.bank_pin.split("'")[1]
        return str(decrypt(bytes_part.encode('utf-8'), key)).split("'")[1]

    def get_ref(self, obj):
        bytes_part = obj.ref.split("'")[1]
        return str(decrypt(bytes_part.encode('utf-8'), key)).split("'")[1]
