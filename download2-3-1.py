import sys
import io
import urllib.request as req
from urllib.parse import urlparse
#import urllib.parse as parse

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://hr.hani.co.kr"

mem = req.urlopen(url)

#print(type(mem))

#print(type({}))
#print(type([]))
#print(type(()))

print("geturl", mem.geturl())
print("status", mem.status) # 200, 404, 403, 500
print("headers", mem.getheaders())
print("================")
print("info", mem.info())
print("code", mem.getcode())
print("read", mem.read(100))
print("================")
print("read", mem.read().decode("utf-8"))
print("================")
print(urlparse("http://hr.hani.co.kr/Huga/HugaList01?sort=e_day&sortdir=ASC"))
