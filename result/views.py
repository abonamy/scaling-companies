from django.views import generic

from rest_framework import viewsets

from .models import Company
from .serializers import CompanySerializer


class IndexView(generic.ListView):
    model = Company


class DetailView(generic.DetailView):
    model = Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
