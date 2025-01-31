#coding:utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import fields
from django.db.models import signals
from django.urls import reverse
from ckeditor.fields import RichTextField
import datetime
from django.utils import timezone


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(
            upload_to='photo',
            default = '/static/open-iconic/png/person-3x.png',
            verbose_name = u'头像'
            )
    #权限默认为0，即已注册用户, 1为被封禁, 2为系统管理员
    privilege = models.IntegerField(
            default = 0,
            verbose_name = u'权限'
            )
    
    class Meta:
        db_table = 'user'
        #可读性名字（及其复数形式）
        verbose_name = u'用户'
        verbose_name_plural = u'用户'
        ordering = ['-date_joined']
    
    #无需重写__str__，会自动生成
    def __unicode__(self):
        return self.get_username()


class Navigation(models.Model):
    name = models.CharField(
            max_length = 30,
            verbose_name = u'导航'
            )
    url = models.CharField(
            max_length = 250,
            verbose_name = u'地址'
            )
    
    created_time = models.DateTimeField(
            u'创建时间',
            default = datetime.datetime.now
            )
    
    class Meta:
        db_table = 'navigation'
        verbose_name = u'导航'
        verbose_name_plural = u'导航'
        ordering = ['-created_time']
    
    def __unicode__(self):
        return self.name

    
class Section(models.Model):
    name = models.CharField(
            max_length = 50,
            verbose_name = u'名称'
            )
    author = models.CharField(
            default = "",
            max_length = 50,
            verbose_name = u'作者'
            )
    # 1-书籍主页，2-影视主页， 3-话题主页， 4-小组主页，5-书籍, 6-影视， 7-话题, 8-小组
    section_type = models.IntegerField(
            default = 0
            )
    director = models.CharField(
            default = "",
            max_length = 50,
            verbose_name = u'导演'
            )
    actor = models.CharField(
            default = "",
            max_length = 100,
            verbose_name = u'演员'
            )
    author_description = models.CharField(
            max_length = 2000,
            verbose_name = u'作者描述'
            )
    admins = models.ManyToManyField(
            'User',
            blank = True,
     #       null = True,
            related_name = 'admins',
            verbose_name = u'管理员'
            )
    users = models.ManyToManyField(
            'User',
            blank = True,
     #       null = True,
            related_name = 'users',
            verbose_name = u'用户'
            )
    parent_section = models.ForeignKey(
            'self',
            blank = True,
            null = True,
            on_delete = models.CASCADE,
            related_name = 'section_parent_section',
            )
    description = models.CharField(
            max_length = 2000,
            verbose_name = u'描述'
            )
    img = models.ImageField(
            upload_to='photo',
            verbose_name = u'图像'
            )
    content_number = models.IntegerField(
            default = 0
            )
    star = models.DecimalField(
            default = 0,
            max_digits = 2,
            decimal_places = 1
            )
    
    created_at = models.DateTimeField(
            default = timezone.now
            )
    updated_at = models.DateTimeField(
            default = timezone.now
            )

    class Meta:
        db_table = 'section'
        verbose_name = u'区块'
        verbose_name_plural = u'区块'
        ordering = ['-content_number']
    
    def __unicode__(self):
        return self.name
    def get_join_url(self):
        return reverse('section_join',  args = [str(self.pk)])
    def get_admin_url(self):
        return reverse('section_admin',  args = [str(self.pk)])
    def get_absolute_url(self):
        return reverse("section_details",  args = [str(self.pk)])
    
    
class Post(models.Model):
    title = models.CharField(
            max_length = 20,
            verbose_name = u'标题'
            )
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete = models.CASCADE,
            related_name = 'post_author',
            )
    #3-话题， 4-小组
    type_post = models.IntegerField(
            default = 0
            )
    section = models.ForeignKey(
            Section,
            on_delete = models.CASCADE,
            related_name = 'post_section',
            )
    view_times = models.IntegerField(
            default = 0
            )
    content_number = models.IntegerField(
            default = 0
            )
    last_response = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete = models.CASCADE,
            related_name = 'post_last_responce',
            )
    
    upper_placed = models.BooleanField(
            default = False
            )
    #是否加精
    essence = models.BooleanField(
            default = False
            )
    
    created_at = models.DateTimeField(
            default = timezone.now
            )
    updated_at = models.DateTimeField(
            default = timezone.now
            )
    
    class Meta:
        db_table = 'post'
        verbose_name = u'主题帖'
        verbose_name_plural = u'主题帖'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.title
    
    def description(self):
        return u' %s 发表了主题帖 %s' % (self.author, self.title)
    
    def get_absolute_url(self):
        return reverse("post_detail",  args = [str(self.pk)])
    def get_top_url(self):
        return reverse("post_top",  args = [str(self.pk)])
    def get_useful_url(self):
        return reverse("post_useful",  args = [str(self.pk)])
    def get_delete_url(self):
        return reverse("post_delete",  args = [str(self.pk)])
    def cancel_useful_url(self):
        return reverse("cancel_post_useful",  args = [str(self.pk)])
    def cancel_top_url(self):
        return reverse("cancel_post_top",  args = [str(self.pk)])
    
    
class PostPart(models.Model):
    post = models.ForeignKey(
            Post,
            related_name = 'post',
            on_delete = models.CASCADE
            )
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name = 'postpart_author',
            on_delete = models.CASCADE
            )
    content = RichTextField(
            verbose_name = u'内容'
            )
    #3-话题， 4-小组
    type_postpart = models.IntegerField(
            default = 0
            )
    content_number = models.IntegerField(
            default = 0
            )
    last_response = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete = models.CASCADE,
            related_name = 'postpart_last_responce',
            )
    created_at = models.DateTimeField(
            default = timezone.now
            )
    updated_at = models.DateTimeField(
            default = timezone.now
            )
    
    class Meta:
        db_table = 'postpart'
        verbose_name = u'间贴'
        verbose_name_plural = u'间贴'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.title
    
    def description(self):
        return u' %s 回复了帖子（%s）： %s' % (
                self.author, self.post, 
                self.content)

class PostPartComment(models.Model):
    postpart =  models.ForeignKey(
            PostPart,
            related_name = 'postpart',
            on_delete = models.CASCADE
            )
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name = 'postpartcomment_author',
            on_delete = models.CASCADE
            )
    #3-话题， 4-小组
    type_postpartcomment = models.IntegerField(
            default = 0
            )
    content = models.TextField(
            verbose_name = u'内容'    
            )
    created_at = models.DateTimeField(
            default = timezone.now
            )
    updated_at = models.DateTimeField(
            default = timezone.now
            )
    
    class Meta:
        db_table = 'postpartcomment'
        verbose_name = u'间贴评论'
        verbose_name_plural = u'间贴评论'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.title
    
    def description(self):
        return u' %s 回复了帖子（%s）： %s' % (
                self.author, self.postpart.post, 
                self.content)

class AdminApply(models.Model):
    section = models.ForeignKey(
            Section,
            on_delete = models.CASCADE,
            related_name = 'adminapply_section',
            )
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name = 'adminapply_author',
            on_delete = models.CASCADE
            )
    created_at = models.DateTimeField(
            default = timezone.now
            )

    
    class Meta:
        db_table = 'adminapply'
        verbose_name = u'管理员申请'
        verbose_name_plural = u'管理员申请'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.user + self.section
    
    def description(self):
        return u' %s 申请了管理员（%s）' % (
                self.user, self.section)
    def get_pass_url(self):
        return reverse('pass_apply',  args = [str(self.pk)])
    def get_refuse_url(self):
        return reverse('refuse_apply',  args = [str(self.pk)])

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Comment(models.Model):
    title = models.CharField(
            max_length = 20,
            verbose_name = u'标题'
            )
    section = models.ForeignKey(
            Section,
            related_name = 'comment_section',
            on_delete = models.CASCADE
            )
    #1-书籍， 2-影视
    type_comment = models.IntegerField(
            default = 0
            )
    star = IntegerRangeField(default=3,min_value=0, max_value=5,verbose_name = u'评分')
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name = 'comment_author',
            on_delete = models.CASCADE
            )
    content = RichTextField(
        verbose_name = u'内容'
        )
    like_number = models.IntegerField(
            default = 0
            )
    dislike_number = models.IntegerField(
            default = 0
            )
    like_user = models.ManyToManyField(
            'User',
            blank = True,
     #       null = True,
            related_name = 'like_user'
            )
    dislike_user = models.ManyToManyField(
            'User',
            blank = True,
     #       null = True,
            related_name = 'dislike_user'
            )
    
    created_at = models.DateTimeField(
            default = timezone.now
            )
    updated_at = models.DateTimeField(
            default = timezone.now
            )
    
    class Meta:
        db_table = 'comment'
        verbose_name = u'评论'
        verbose_name_plural = u'评论'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.title
    
    def description(self):
        return u' %s 添加了评论（%s）： %s' % (
                self.author, self.section, 
                self.content)
    def get_absolute_url(self):
        return reverse('comment_detail',  args = [str(self.pk)])
    def get_like_url(self):
        return reverse('like_comment',  args = [str(self.pk)])
    def get_dislike_url(self):
        return reverse('dislike_comment',  args = [str(self.pk)])
    
class CommentReport(models.Model):
    comment = models.ForeignKey(
            Comment,
            related_name = 'commentreport_comment',
            on_delete = models.CASCADE
            )
    status = models.BooleanField(
            default = False
            )
    author = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name = 'commentreport_author',
            on_delete = models.CASCADE
            )
    title = models.CharField(
            max_length = 40,
            verbose_name = u'标题'
            )
    content = models.TextField(
            verbose_name = u'内容'
            )
    
    created_at = models.DateTimeField(
            default = timezone.now
            )
    updated_at = models.DateTimeField(
            default = timezone.now
            )
    
    class Meta:
        db_table = 'commentreport'
        verbose_name = u'评论举报'
        verbose_name_plural = u'评论举报'
        ordering = ['-created_at']
    
    def __unicode__(self):
        return self.title
    def get_pass_url(self):
        return reverse('pass_report',  args = [str(self.pk)])
    def get_refuse_url(self):
        return reverse('refuse_report',  args = [str(self.pk)])
   

    
    
def post_save(sender, instance, signal, *args, **kwargs):
    entity = instance
    section = entity.section
    section.content_number += 1
    section.save()
    
def post_delete(sender, instance, signal, *args, **kwargs):
    entity = instance
    section = entity.section
    section.content_number -= 1
    section.save()

def postpart_save(sender, instance, signal, *args, **kwargs):
    entity = instance
    post = entity.post
    post.content_number += 1
    post.save()
    
def postpart_delete(sender, instance, signal, *args, **kwargs):
    entity = instance
    post = entity.post
    post.content_number -= 1
    post.save()

def comment_save(sender, instance, signal, *args, **kwargs):
    entity = instance
    section = entity.section
    section.content_number += 1
    section.save()
    
def comment_delete(sender, instance, signal, *args, **kwargs):
    entity = instance
    section = entity.section
    section.content_number -= 1
    section.save()
    

    
#注册消息响应函数
signals.post_save.connect(comment_save, sender=Comment)
signals.post_delete.connect(comment_delete, sender=Comment)
signals.post_save.connect(post_save, sender=Post)
signals.post_delete.connect(post_delete, sender=Post)
signals.post_save.connect(postpart_save, sender=PostPart)
signals.post_delete.connect(postpart_delete, sender=PostPart)

    
    
    
    
    
    
    
    
    
    