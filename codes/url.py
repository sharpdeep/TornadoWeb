#coding=utf-8
"""
the url structure of website
url.py用于设置网站的目录结构；
url列表列出了所有的目录和对应的处理类
"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')  #兼容汉字

from handlers.index import IndexHandler
from handlers.user import UserHandler

url = [
        (r'/',IndexHandler),
        (r'/user',UserHandler),
]
