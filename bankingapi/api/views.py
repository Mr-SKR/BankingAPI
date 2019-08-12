from rest_framework import generics
from .serializers import BanksSerializer, BranchSerializer
from .models import Banks, Branches
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class GetBankView(generics.ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Branches.objects.all()
        bank_name = self.request.query_params.get('bank', None)
        city = self.request.query_params.get('city', None)
        if bank_name and city:
            queryset = queryset.filter(bank__name=bank_name, city=city)
        elif bank_name:
            queryset = queryset.filter(bank__name=bank_name)
        elif city:
            queryset = queryset.filter(city=city)
        return queryset


class CreateBankView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsBankView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CreateBranchView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsBranchView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
