from rest_framework import generics
from .serializers import BanksSerializer, BranchSerializer
from .models import Banks, Branches
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class GetBankView(generics.ListAPIView):
    serializer_class = BranchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Branches.objects.all()
        bank_name = self.request.query_params.get('name', None)
        city = self.request.query_params.get('city', None)
        if bank_name and city:
            queryset = queryset.filter(bank__name=bank_name.upper(),
                                       city=city.upper())
        elif bank_name:
            queryset = queryset.filter(bank__name=bank_name.upper())
        elif city:
            queryset = queryset.filter(city=city.upper())
        return queryset


class DetailsBankView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Banks.objects.all()
    serializer_class = BanksSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class DetailsBranchView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
