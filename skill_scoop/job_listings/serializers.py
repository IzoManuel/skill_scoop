from rest_framework import serializers
from .models import JobListing

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['id', 'title', 'company', 'location', 'description', 'url', 'skills']