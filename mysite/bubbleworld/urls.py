#coding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from bubbleworld import views

admin.autodiscover()

urlpatterns = [
    url(r'^accounts/login/$', views.user_login, name='user_login'),
    url(r'^accounts/logout/$', views.user_logout, name='user_logout'),
    url(r'^accounts/register/$',
        views.user_register,
        name='user_register'),
    url(r'^accounts/$', login_required(views.show_accounts), name='show_accounts'),
    url(r'^accounts/handle_apply/$', login_required(views.HandleApply.as_view()), name='handle_apply'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^section/(?P<section_pk>\d+)/$',
        views.section_index_detail,
        name='section_index_detail'),
    url(r'^modify_password/$',
        views.modify_password,
        name='modify_password'),
    url(r'^section_detail/$',
        views.SectionView.as_view(),
        name='section_detail'),
    url(r'^comment_detail/(?P<comment_pk>\d+)/$',
        views.comment_detail,
        name='comment_detail'),
    url(r'^like_comment/(?P<comment_pk>\d+)/$',
        login_required(views.like_comment),
        name='like_comment'),
    url(r'^dislike_comment/(?P<comment_pk>\d+)/$',
        login_required(views.dislike_comment),
        name='dislike_comment'),
    url(r'^post_detail/(?P<post_pk>\d+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^section_create/$',
        login_required(views.SectionCreate.as_view()),
        name='section_create'),
    url(r'^section_join/(?P<section_pk>\d+)/$',
        login_required(views.section_join),
        name='section_join'),
    url(r'^section_admin/(?P<section_pk>\d+)/$',
        login_required(views.section_admin),
        name='section_admin'),
    url(r'^comment_create/$',
        login_required(views.CommentCreate.as_view()),
        name='comment_create'),
    url(r'^commentreport_create/$',
        login_required(views.CommentReportCreate.as_view()),
        name='commentreport_create'),
    url(r'^book_create/$',
        login_required(views.BookCreate.as_view()),
        name='book_create'),
    url(r'^film_create/$',
        login_required(views.FilmCreate.as_view()),
        name='film_create'),
    url(r'^post_create/$',
        login_required(views.PostCreate.as_view()),
        name='post_create'),
    url(r'^post_delete/(?P<post_pk>\d+)/$',
        login_required(views.delete_post),
        name='post_delete'),
    url(r'^postpart_create/$',
        login_required(views.PostPartCreate.as_view()),
        name='postpart_create'),
    url(r'^postpartcomment_create/$',
        login_required(views.PostPartCommentCreate.as_view()),
        name='postpartcomment_create'),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^section_search/$', views.SectionSearchView.as_view(), name='section_search'),
    url(r'^captcha/$', 
        views.captcha, 
        name='captcha'),
     ]