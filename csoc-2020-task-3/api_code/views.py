from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from .serializers import TodoCreateSerializer, TodoSerializer
from rest_framework import viewsets 
from .models import Todo


"""
TODO:
Create the appropriate View classes for implementing
Todo GET (List and Detail), PUT, PATCH and DELETE.
"""


class TodoCreateView(generics.GenericAPIView):
    """
    TODO:
    Currently, the /todo/create/ endpoint returns only 200 status code,
    after successful Todo creation.
    Modify the below code (if required), so that this endpoint would
    also return the serialized Todo data (id etc.), alongwith 200 status code.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = TodoCreateSerializer

    def post(self, request):
        """
        Creates a Todo entry for the logged in user.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            return Response({
                'id':instance.id,
                'title':instance.title,
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# class TodoListView(generics.GenericAPIView):
#     permission_classes = (permissions.IsAuthenticated, )
#     serializer_class = TodoSerializer
#     def get(self, request, *args, **kwargs):
#         try:
#             header=request.headers['Authorization']
#         except Exception:
#             return Response({'detail':"Authentication credentials were not provided"}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             token = header.split(' ')[1]
#             try:
#                 user = Token.objects.get(key=token).user
#             except Exception:
#                 return Response({'detail':"Authentication credentials were not provided"}, status=status.HTTP_401_UNAUTHORIZED)
#             else:
#                 def get_queryset(self):
#                     queryset = Todo.objects.filter(creator=user)
#                     return queryset
#                 queryset = get_queryset(self)
#                 serializer = self.get_serializer(queryset, many = True)
#                 return Response(serializer.data,status=status.HTTP_200_OK)

class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer