from django.shortcuts import render
# Create your views here.
from myblog import settings
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
django.setup()


def global_setting(request):
    # 站点基本信息
    TITLE = settings.TITLE
    SITE_DESC = settings.DESC
    SITE_KEYWORD = settings.KEYWORD
    # 分类信息获取（导航数据）
    # 文章归档数据
    # 广告数据（同学们自己完成）
    # 标签云数据（同学们自己完成）
    # 友情链接数据（同学们自己完成）
    # 文章排行榜数据（按浏览量和站长推荐的功能同学们自己完成）
    # 评论排行
    return locals()


def index(request):
    title = "首页"
    return render(request, "index.html", locals())


def about(request):
    title = "关于我"
    return render(request, "about.html", locals())


def gbook(request):
    title = "留言"
    return render(request, "gbook.html", locals())


def info(request):
    title = "学无止境"
    return render(request, "info.html", locals())


def life(request):
    title = "慢生活"
    return render(request, "life.html", locals())


def list(request):
    title = "学无止境"
    return render(request, "list.html", locals())


def time(request):
    title = "时间轴"
    return render(request, "time.html", locals())


def share(request):
    title = "模板分享"
    return render(request, "share.html", locals())
