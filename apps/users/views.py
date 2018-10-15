from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.serializers import User, UserRegisterSerializer, EmailVerifySerializer, UserDetailSerializer
from utils.email_send import send_email
from utils.permissions import IsSelfOrReadOnly

# Create your views here.


class EmailCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):

    serializer_class = EmailVerifySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        send_email(email, send_type='register')
        return Response({'email': email}, status=status.HTTP_201_CREATED)


class UserViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):

    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # 动态配置Serializer
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserRegisterSerializer
        return UserDetailSerializer

    # 动态设置验证类型
    def get_permissions(self):
        if self.action == 'create':
            return []
        return [IsSelfOrReadOnly()]

    def list(self, request, *args, **kwargs):
        queryset = request.user

        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
