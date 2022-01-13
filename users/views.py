from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, UserProfileSerializers, FileuploadSerializers
from .models import NewUser, UserProfile, Fileupload
import jwt, datetime
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 
from rest_framework.generics import RetrieveAPIView
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Create your views here.
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

 
class RegisterView(ModelViewSet):
    serializer_class = UserSerializer
    serializer = UserSerializer
    def post(self, request, *args, **kwargs):
        serializer.self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "messsage":"kucisdu",

            })

    queryset = NewUser.objects.all()   


class LoginView(APIView):
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # serializer_class = UserSerializer
    # queryset = NewUser.objects.all() 
    # def get_token(self):
    #     return self.request.user
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = NewUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            
        }
        return response



class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = NewUser.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


####youebe

class NewUserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = NewUser.objects.all()

class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializers
    queryset = UserProfile.objects.all()


class FileuploadView(ModelViewSet):
    serializer_class = FileuploadSerializers
    queryset = Fileupload.objects.all()
