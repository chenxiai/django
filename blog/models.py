from django.db import models


# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

# 通过定义class来自动生成表
class Article(models.Model):
    # 默认会生成自动增长的主键
    title = models.CharField(max_length=30, default='my title')
    content = models.TextField(null=True)

    # 特殊方法,print()函数显示对象信息时,默认就是调用此方法
    def __str__(self):
        return f"id={self.id},title={self.title},content={self.content}"
        # return "id:" + self.id + ",title:" + self.title + ",content:" + self.content
