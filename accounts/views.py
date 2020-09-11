from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.viewsets import ViewSet

from accounts.models import *
from accounts.serializers import *


class AccountViewSet(ViewSet):
    serializer_class = AccountSerializer

    @action(methods=['POST'], detail=False)
    def get_account_from_user_id(self, request):
        data = request.data
        user_id = data.get('user_id')

        account = Account.objects.filter(user_id=user_id).first()
        serializer = AccountViewSet.serializer_class(account)

        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def create_account(self, request):
        data = request.data
        user_id = data.get('user_id')
        dob = data.get('dob')

        # Get User via ID
        user = User.objects.filter(id=user_id).order_by("pk").first()

        if not user:
            return Response({
                'status': HTTP_400_BAD_REQUEST,
                'message': 'ERROR: User ID does not exist.',
            }, status=HTTP_400_BAD_REQUEST)

        # Create User's Account
        account = Account.objects.create(user=user, dob=dob)

        if account:
            serializer = AccountViewSet.serializer_class(account)
            return Response(serializer.data)

        return Response({
            'status': HTTP_400_BAD_REQUEST,
            'message': 'ERROR: Cannot create Account',
        }, status=HTTP_400_BAD_REQUEST)
