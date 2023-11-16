from rest_framework import generics
from .models import JobListing
from .serializers import JobListingSerializer

class JobListingListCreateView(generics.ListCreateAPIView):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer

class JobListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
