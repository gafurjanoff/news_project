from django.urls import path
from .views import news_list, news_detail,home_page_view


urlpatterns = [
    # path('', contact_page_view, name='contact_page'),
    path('', home_page_view, name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<int:id>/', news_detail, name='news_detail_page')
]