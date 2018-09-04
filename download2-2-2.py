import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "http://post.phinf.naver.net/20150815_34/pepsiman517_1439610314568pDgJw_JPEG/mug_obj_143961031451425077.jpg"
htmlURL = "http://google.com"

savePath1 = "D:/최혜진/python/pythonCrawling/section2/test1-2.jpg"
savePath2 = "D:/최혜진/python/pythonCrawling/section2/index-2.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb')
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")
