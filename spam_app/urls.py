from django.urls import path
from . import app

urlpatterns = [
    path('', app.home, name='home'),
    path('predict/', app.predict_spam, name='predict'),
]
