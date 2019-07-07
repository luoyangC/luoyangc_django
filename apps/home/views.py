import os
from datetime import datetime

from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.random_str import generate_random_str
from utils.tulin_talk import talk
from luoyangc.settings import HOST_URL


User = get_user_model()


class IndexView(View):
    """
    主页测试
    """
    @staticmethod
    def get(request):
        return render(request, 'demo.html')


class TalkView(APIView):
    """图灵机器人接口"""
    def post(self, request):
        result = talk(request.data['info'], request.data['userid'])
        return Response({'code': 100000, 'text': result})


class UploadView(APIView):
    """
    上传文件接口
    """
    parser_classes = (MultiPartParser,)
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    def post(self, request):

        code = 0
        msg = 'fail'

        file = request.FILES.get('file', None)

        upload_type = request.data.get('upload_type', None)

        if upload_type == 'user_img':

            user = request.user

            file_type = file.content_type.split('/')
            if file_type[0] == 'image':

                year = datetime.now().year
                month = datetime.now().month

                local_path = 'media/image/user/{}/{}/'.format(year, month)

                if not os.path.exists(local_path):
                    os.makedirs(local_path)

                local_file = local_path + generate_random_str() + '.' + file_type[1]

                destination = open(local_file, 'wb+')
                for chunk in file.chunks():
                    destination.write(chunk)
                destination.close()

                user.image = local_file[6:]
                user.save()

                return Response({'code': code, 'message': msg, 'url': HOST_URL + local_file})

            return Response({'code': 201, 'message': 'type error'})

        elif upload_type == 'editor_img':

            file_type = file.content_type.split('/')
            if file_type[0] == 'image':

                year = datetime.now().year
                month = datetime.now().month

                local_path = 'media/editor/{}/{}/'.format(year, month)

                if not os.path.exists(local_path):
                    os.makedirs(local_path)

                local_file = local_path + generate_random_str() + '.' + file_type[1]

                destination = open(local_file, 'wb+')
                for chunk in file.chunks():
                    destination.write(chunk)
                destination.close()

                return Response({'code': code, 'message': msg, 'url': HOST_URL + local_file})

            return Response({'code': 201, 'message': 'type error'})

        elif upload_type == 'article_img':

            file_type = file.content_type.split('/')
            if file_type[0] == 'image':

                year = datetime.now().year
                month = datetime.now().month

                local_path = 'media/image/article/{}/{}/'.format(year, month)

                if not os.path.exists(local_path):
                    os.makedirs(local_path)

                local_file = local_path + generate_random_str() + '.' + file_type[1]

                destination = open(local_file, 'wb+')
                for chunk in file.chunks():
                    destination.write(chunk)
                destination.close()

                return Response({'code': code, 'message': msg, 'url': HOST_URL + local_file})

            return Response({'code': 201, 'message': 'type error'})
