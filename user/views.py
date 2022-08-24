
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.contrib.auth.hashers import make_password, check_password


class Join(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        return render(request, 'user/join.html')

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        email = request.data.get('email', None)
        nickname = request.data.get('nickname', None)
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image="default_profile.jpg")

        return Response(status=200)


class Login(APIView):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        if email is None:
            return Response(status=500, data=dict(message='이메일을 입력해주세요'))

        if password is None:
            return Response(status=500, data=dict(message='비밀번호를 입력해주세요'))

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=500, data=dict(message='입력정보가 잘못되었습니다.'))

        if check_password(password, user.password) is False:
            return Response(status=500, data=dict(message='입력정보가 잘못되었습니다.'))

        request.session['loginCheck'] = True
        request.session['email'] = user.email

        return Response(status=200, data=dict(message='로그인에 성공했습니다.'))



    #
    #     user = User.objects.filter(email=email).first()
    #         # 여기서 filter는 쿼리셋을 리턴한다 - 리스트 형태로 리턴
    #         # first를 쓰면 리스트값 첫번째만 선택가능
    #         # 좋은점은 리스트 객체를 쓰지않고  User객체를 바로 쓸수있음
    #         # first를 쓰면 User.name 식으로 객체를 바로 사용가능하지만
    #         # first를 쓰지않으면 User[0] 처럼 유저리스트의 첫번째값을 빼서 쓰거나
    #         # for문을 돌려 하나씩 가져와서 사용해야함.
    #
    #


