from django.urls import path
from .views import one, two, three, four, five

app_name="first"
urlpatterns = [
    path('one/', one, name='one'),
    path('two/', two, name='two'),
    path('three/', three, name='three'),
    path('four/', four, name='four'),
    path('five/',five, name='five'),
]