from django.urls import path
from .views import JobListingListCreateView, JobListingDetailView

urlpatterns = [
    path('job_listings/', JobListingListCreateView.as_view(), name='job-listing-list-create'),
    path('job_listings/<int:pk', JobListingDetailView.as_view(), name='job-listing-detail')
]