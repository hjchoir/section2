import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://post.phinf.naver.net/20150815_34/pepsiman517_1439610314568pDgJw_JPEG/mug_obj_143961031451425077.jpg"
htmlURL = "http://google.com"

savePath1 = "D:/최혜진/python/pythonCrawling/section2/test1.jpg"
savePath2 = "D:/최혜진/python/pythonCrawling/section2/index.html"


dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL,savePath2)

print("다운로드 완료!")
