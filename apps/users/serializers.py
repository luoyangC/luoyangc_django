"""
  Created by Amor on 2018-09-23
"""
from django.core.cache import cache
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

__author__ = '骆杨'


User = get_user_model()


class EmailVerifySerializer(serializers.Serializer):

    email = serializers.EmailField()
    send_type = serializers.CharField()

    def validate(self, attrs):
        if attrs['send_type'] == 'register':
            if User.objects.filter(email=attrs['email']).count():
                raise serializers.ValidationError('用户已存在')
        elif attrs['send_type'] == 'retrieve':
            if not User.objects.filter(email=attrs['email']).count():
                raise serializers.ValidationError('用户不存在')
        if cache.get(attrs['email']):
            raise serializers.ValidationError('距离上次发生不足5分钟，请查看邮件，或稍后再试')
        return attrs


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True, allow_blank=False, label='邮箱', help_text='邮箱',
                                  validators=[UniqueValidator(queryset=User.objects.all())])
    code = serializers.CharField(write_only=True, label='验证码', help_text='验证码')
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, label='密码', help_text='密码')

    def validate_code(self, code):
        verify_records = cache.get(self.initial_data['email'])
        if not verify_records:
            raise serializers.ValidationError('验证码过期')
        if verify_records[0] != 'register' or verify_records[1] != code:
            raise serializers.ValidationError('验证码错误')

    def validate(self, attrs):
        attrs['username'] = attrs['email']
        del attrs['code']
        return attrs

    class Meta:
        model = User
        fields = ('email', 'code', 'password')


class UserDetailSerializer(serializers.ModelSerializer):

    email = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'birthday', 'gender', 'image', 'mobile', 'email', 'homepage', 'profile', 'is_staff')
