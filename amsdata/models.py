from django.db import models


# 系统配置
class Config(models.Model):
    title = models.CharField('网站名称',max_length=128)
    url = models.CharField('网站url',max_length=128)
    murl = models.CharField('手机网站url',max_length=128)
    logo = models.CharField('logoimg',max_length=128)
    logowidth = models.CharField('logo宽度',max_length=128)
    logoheight = models.CharField('logo高度',max_length=128)
    logoright = models.CharField('logo右侧内容',max_length=128)
    name = models.CharField('联系人',max_length=128)
    phone = models.CharField('手机',max_length=128)
    mail = models.CharField('邮箱',max_length=128)
    tel = models.CharField('电话',max_length=128)
    fax = models.CharField('传真号',max_length=128)
    qq = models.CharField('QQ',max_length=128)
    zip = models.CharField('邮编',max_length=128)
    addr = models.CharField('地址',max_length=128)
    daohangnr = models.CharField('频道导航信息',max_length=128)
    copyright = models.CharField('版权信息',max_length=128)
    beian = models.CharField('ICP备案编号',max_length=128)
    keywords = models.CharField('网页关键字',max_length=128)
    description = models.CharField('网站描述	',max_length=128)
    template = models.CharField('模板名称',max_length=128)
    off_sm = models.CharField('网站消息',max_length=128)
    zztj = models.CharField('站长统计',max_length=128)

# 单页频道
class Singlepage(models.Model):
    display_c = ((0,'不显示'),(1,'显示'))
    title = models.CharField('网页标题',max_length=128)
    keywords = models.CharField('网页关键词',max_length=128)
    description = models.CharField('网页描述',max_length=128)
    display = models.SmallIntegerField('是否前台显示',choices=display_c)
    weight = models.IntegerField('权重',max_length=128)
    content = models.TextField('页面内容')
    creat_at = models.DateTimeField('创建时间')


# 视频分类
class VideoType(models.Model):
    display_c = ((0,'不显示'),(1,'显示'))
    title = models.CharField('类名称',max_length=128)
    url = models.CharField('地址',max_length=128,unique=True)
    weight = models.IntegerField('权重', max_length=128)

# 视频频道
class Video(models.Model):
    display_c = ((0,'不显示'),(1,'显示'))
    vt = models.ForeignKey('VideoType')
    title = models.CharField('视频标题',max_length=128)
    display = models.SmallIntegerField('是否前台显示', choices=display_c,default=1)
    weight = models.IntegerField('权重',default=1)
    img = models.CharField('标题略缩图', max_length=256,null=True,blank=True)
    url = models.CharField('视频地址', max_length=256)


# 新闻分类
class NewsType(models.Model):
    display_c = ((0,'不显示'),(1,'显示'))
    title = models.CharField('类名称',max_length=128)
    keywords = models.CharField('关键字',max_length=128)
    url = models.CharField('地址',max_length=128,unique=True)
    weight = models.IntegerField('权重', max_length=128)

# 新闻频道
class News(models.Model):
    display_c = ((0,'不推荐'),(1,'推荐'))
    nt = models.ForeignKey('NewsType')
    title = models.CharField('新闻标题',max_length=128)
    color = models.CharField('标题颜色',max_length=7)
    img = models.CharField('标题略缩图', max_length=256, null=True, blank=True)
    summary = models.CharField('内容简介', max_length=255)
    keywords = models.CharField('关键字', max_length=128)
    url = models.CharField('外部链接', max_length=256)
    source = models.CharField('新闻来源', max_length=256)
    author = models.CharField('作者', max_length=256)
    data = models.DateTimeField('发布时间')
    recommend = models.SmallIntegerField('是否推荐', choices=display_c,default=1)
    weight = models.IntegerField('权重',default=1)


#  服务项目
class ServiceProject(models.Model):
    name = models.CharField('项目名称',max_length=128)
    img = models.CharField('项目图片', max_length=256, null=True, blank=True)
    summary = models.CharField('简单说明', max_length=100)
    keywords = models.TextField('服务详情')
    weight = models.IntegerField('权重',default=1)

#  服务项目
class ServiceProcess(models.Model):
    name = models.CharField('项目名称',max_length=128)
    img = models.CharField('项目图片', max_length=256, null=True, blank=True)
    width = models.IntegerField('宽度',default=55)
    height = models.IntegerField('高度',default=60)
    summary = models.CharField('服务说明', max_length=100)
    weight = models.IntegerField('权重',default=1)



