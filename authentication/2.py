from rest_framework import generics

from authentication.models import User
from authentication.serializers import CreateUserSerializer



# class LogoutView(APIView):
#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)
