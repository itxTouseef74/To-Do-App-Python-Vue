from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializer import TodoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication 
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from .serializer import UserSignupSerializer

class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer


class TodoView(APIView):
     authentication_classes=[JWTAuthentication]
     permission_classes=[IsAuthenticated]
     def get(self , request):
          user=request.user
          print(user)
          todos= Todo.objects.filter(user=user)
          serializer = TodoSerializer(todos , many=True)
          return Response({
               'status':True,
               'data' :serializer.data,
               'message':'todo fetched successfully'

          })
     def post(self , request):
        try:
            user = request.user
            data = request.data
            data['user'] = user.id
            serializer =TodoSerializer(data=data)

            if not serializer.is_valid():
                return Response({
                    'status':False,
                    'message':'invalid fields',
                    'data':serializer.errors
                })
              
            serializer.save()
            return Response({
                'status':True,
                'messsage':'Todo is created',
                'data':serializer.data
            })
        except Exception as e:
            return Response ({
                'status':False,
                'message':'something went wrong',
                 'data': {'error_message': str(e)}
            })
        
     def patch(self , request):
        try:
            data=request.data
            if not data.get('uuid'):
                return Response ({
                'status':False,
                'message':'uuid is required',
                 'data':{}
                })
            obj=Todo.objects.filter(uuid= data.get('uuid'))

            if not obj.exists():
                 return Response ({
                'status':False,
                'message':'invalid uuid',
                 'data': {'error_message': str(e)}
                })
            serializer = TodoSerializer(obj[0] , data=data ,partial=True)
            if not serializer.is_valid():
                return Response({
                    'status':False,
                    'message':'invalid fields',
                    'data':serializer.errors
                })
              
            serializer.save()
            return Response({
                'status':True,
                'messsage':'Todo is created',
                'data':serializer.data
            })
        except Exception as e:
            return Response ({
                'status':False,
                'message':'something went wrong',
                'data': {'error_message': str(e)}
            })

     def delete(self, request):
        try:
            data = request.data
            if not data.get('uuid'):
                return Response({
                    'status': False,
                    'message': 'uuid is required',
                    'data': {}
                })

            obj = Todo.objects.filter(uuid=data.get('uuid'))

            if not obj.exists():
                return Response({
                    'status': False,
                    'message': 'invalid uuid',
                    'data': {}
                })
            
            obj.delete()

            return Response({
                'status': True,
                'message': 'Todo is deleted successfully',
                'data': {}
            })

        except Exception as e:
            return Response({
                'status': False,
                'message': 'something went wrong',
                'data': {'error_message': str(e)}
            })
