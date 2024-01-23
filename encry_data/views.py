# from rest_framework.permissions import AllowAny,
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UserBankInformation
from .serialization import UserBankInformationSerializer, UserBankInformationSerializer2
from .system import encrypt
# Create your views here.


class EncryptDataView(APIView):
    model = UserBankInformation
    serializer_class = UserBankInformationSerializer
    key = 'AAAAAAAAAAAAAAAA'  # Must Be 16 char for AES128

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['name'] = encrypt(serializer.validated_data['name'], self.key)
            serializer.validated_data['email'] = encrypt(serializer.validated_data['email'], self.key)
            serializer.validated_data['bank_account'] = encrypt(serializer.validated_data['bank_account'], self.key)
            serializer.validated_data['photo'] = encrypt(serializer.validated_data['photo'], self.key)
            serializer.validated_data['bank_pin'] = encrypt(serializer.validated_data['bank_pin'], self.key)
            serializer.validated_data['ref'] = encrypt(serializer.validated_data['ref'], self.key)
            serializer.save()
            return Response({"success": True, "message": "Saved",
                             "data": serializer.data},
                            status=status.HTTP_200_OK)  # noqa
        else:
            return Response({"success": False, "message": "Error in serializing data",
                             "errors": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)  # noqa


class EncryptDatagetView(APIView):
    model = UserBankInformation
    serializer_class = UserBankInformationSerializer2
    key = 'AAAAAAAAAAAAAAAA'  # Must Be 16 char for AES128

    def get(self, request, *args, **kwargs):
        obj = UserBankInformation.objects.filter(pk=self.kwargs["id"]).first()
        serializer = self.serializer_class(obj, many=False)

        return Response({"success": True, "message": "Saved",
                         "data": serializer.data},
                        status=status.HTTP_200_OK)  # noqa

