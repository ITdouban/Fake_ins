from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from ins_api import views
urlpatterns = format_suffix_patterns([

	url(r'Application/',views.apiApplication),

	url(r'user/detail/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
	url(r'user/register/$',views.UserRegister.as_view()),
	url(r'user/register/activation/$',views.UserRegisterVerification.as_view()),
	url(r'user/login/$',views.UserToken.as_view()),
	url(r'user/checkout/$',views.Accounts.as_view()),
	url(r'user/password/$',views.PasswordForget.as_view()),

	url(r'post/brief/(?P<pk>[0-9]+)/$',views.ShortPost.as_view()),
	url(r'home/post/$',views.PostList.as_view()),

	url(r'dynamic/$', views.PostsAPI.as_view()),

	url(r'timestamp/$',views.Test.as_view()),

])