from datetime import datetime
from django.db import models


# 用户模型.
# 第一种：采用的继承方式扩展用户信息（本系统采用）
# 扩展：关联的方式去扩展用户信息
class User(models.Model):
    name = models.CharField('名字', max_length=20, blank=True, null=True)
    email = models.CharField('邮箱', max_length=20, blank=True, null=True)
    mobile = models.CharField('手机号码', max_length=11, blank=True, null=True, unique=True)
    url = models.URLField('个人网页地址', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.name


# Create your models here.
# class Banner(models.Model):
#     title = models.CharField('标题', max_length=100)
#     image = models.ImageField('轮播图', upload_to='banner/%Y%m',max_length=100)
#     url = models.URLField('访问地址', max_length=200)
#     index = models.IntegerField('顺序', default=100)
#     add_time = models.DateTimeField('添加时间', default=datetime.now)
#
#     class Meta:
#         verbose_name = '轮播图'
#         verbose_name_plural = verbose_name


# 自定义一个文章Model的管理器
# 1、新加一个数据处理的方法
# 2、改变原有的queryset
# class ArticleManager(models.Manager):
#     def distinct_date(self):
#         distinct_date_list = []
#         date_list = self.values('date_publish')
#         for date in date_list:
#             date = date['date_publish'].strftime('%Y/%m文章存档')
#             if date not in distinct_date_list:
#                 distinct_date_list.append(date)
#         return distinct_date_list


# # 文章模型
# class Article(models.Model):
#     title = models.CharField(max_length=50, verbose_name='文章标题')
#     desc = models.CharField(max_length=50, verbose_name='文章描述')
#     content = models.TextField(verbose_name='文章内容')
#     click_count = models.IntegerField(default=0, verbose_name='点击次数')
#     is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
#     date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
#     user = models.ForeignKey(User, verbose_name='用户')
#     category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
#     tag = models.ManyToManyField(Tag, verbose_name='标签')
#
#     objects = ArticleManager()
#
#     class Meta:
#         verbose_name = '文章'
#         verbose_name_plural = verbose_name
#         ordering = ['-date_publish']
#
#     def __unicode__(self):
#         return self.title
