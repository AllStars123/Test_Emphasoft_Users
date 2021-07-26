from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsAdminOrUser
from .models import User


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrUser, ]
