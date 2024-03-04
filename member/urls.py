from django.urls import path

from member.views import MemberJoinView, MemberCheckIdView, MemberLoginView, MemberMyPageView

app_name = 'member'

urlpatterns = [
    path('join/', MemberJoinView.as_view(), name='join'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('check-id/api/', MemberCheckIdView.as_view(), name='check-id'),
    path('mypage/', MemberMyPageView.as_view(),name='mypage')
]
