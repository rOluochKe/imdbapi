from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import movie_list, movie_details
from .views import (WatchlistListView, WatchlistDetailView, 
                    StreamPlatformListView, StreamPlatformDetailView, StreamPlatformView,
                    ReviewListView, ReviewDetailView, ReviewCreateView, UserReviewReview,
                    WatchlistListGenericView)

router = DefaultRouter()
router.register('', StreamPlatformView, basename='streamplatform')

urlpatterns = [
    path('list/', WatchlistListView.as_view(), name='movie-list'),
    path('<int:pk>/', WatchlistDetailView.as_view(), name='movie-detail'),
    path('list-two/', WatchlistListGenericView.as_view(), name='watch-list'),

    # path('stream/', StreamPlatformListView.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailView.as_view(), name='stream-detail'),

    path('', include(router.urls)),

    # path('review/', ReviewListView.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    path('<int:pk>/review-create/', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/review/', ReviewListView.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),

    path('reviews/', UserReviewReview.as_view(), name='user-review-detail'),
]