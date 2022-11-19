from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authtoken.models import Token
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import LoginSerializer, UserSerializer


class LoginApi(GenericAPIView):
    
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            serializer = UserSerializer(user, many=False, context={'request': request})
            token = Token.objects.get_or_create(user=user)[0].key
            data = {'token': f'{token}',}
            profile = serializer.data
            data.update(profile)    
            return Response(data, status=200)
        return Response({'detail': 'Не существует пользователя или неверные данные'})  
    
