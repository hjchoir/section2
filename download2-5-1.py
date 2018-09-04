from urllib.parse import urljoin

baseUrl = "http://hr.hani.co.kr/Huga/Huga01.html"

print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../index.html"))
print(">>", urljoin(baseUrl, "../img/img.jpg"))
