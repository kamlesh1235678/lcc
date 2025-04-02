from django.http import JsonResponse
from django.urls import path, re_path, include
from api.v1.module.matrial.matrial_controller import *
from api.v1.module.matrial.home_controller import *
from api.v1.module.matrial.labour_controller import *
from api.v1.module.matrial.contact_controller import *

urlpatterns = [
  path('', IndexView.as_view(), name='home'),
  path('matrial-list/', MatrialListView.as_view(), name='matrial-list'),
  path('matrial-add/', MatrialView.as_view(), name='matrial-add'),
  path('matrial-update/<int:pk>/', MatrialUpdateView.as_view(), name='matrial-update'),
  path('matrial-delete/', MatrialDeleteView.as_view(), name='matrial-delete'),
  path('about/', AboutView.as_view(), name='about'),
  path('contact/', ConatctView.as_view(), name='contact'),
  path('labour-list/', LabourListView.as_view(), name='labour-list'),
  path('labour-add/', LabourView.as_view(), name='labour-add'),
  path('labour-update/<int:pk>/', LabourUpdateView.as_view(), name='labour-update'),
  path('labour-delete/', LabourDeleteView.as_view(), name='labour-delete'),
  path('contact-list/', ContactListView.as_view(), name='contact-list'),
  path('contact-add/', ContactView.as_view(), name='contact-add'),
  path('contact-update/', ContactUpdateView.as_view(), name='contact-update'),
  path('contact-delete/', ContactDeleteView.as_view(), name='contact-delete'),
  path('matrial-fav/<int:matrial_id>/', FavoriteMatrialAdd.as_view(), name='matrial-fav'),
  path('labour-fav/<int:labour_id>/', FavoriteLabourAdd.as_view(), name='labour-fav'),
  path('matrial-com/<int:matrial_id>/', CompressionMatrialAdd.as_view(), name='matrial-com'),
  path('labour-com/<int:labour_id>/', CompressionLabourAdd.as_view(), name='labour-com'),
  path('fav-list/', FavList.as_view(), name='fav-list'),
  path('com-list/', ComList.as_view(), name='com-list'),
  path('labour-filter/', FilterLabour.as_view(), name='labour-filter/'),
  path('labour-review-add/<int:pk>/', LabourReviewView.as_view(), name='labour-review-add'),
  path('matrial-review-add/<int:pk>/', MatrialReviewView.as_view(), name='matrial-review-add'),

]

                                                                                                                                                                                         


                                                                                                                                                                                         