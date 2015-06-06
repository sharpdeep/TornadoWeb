#coding=utf-8

import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='1606772363',db='sharpdeeptest',charset='utf8')

cur = conn.cursor()
