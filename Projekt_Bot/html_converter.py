import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.google.de/search?source=hp&ei=v_6KX7D2Ac2ca5WfmvgC&q=gold+gold&oq=gold+gold&gs_lcp=CgZwc3ktYWIQAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAA6DggAEOoCELQCEJoBEOUCOgIILjoECAAQClCzCFiSKmCBK2gCcAB4AIAB1QKIAYAIkgEFOC4zLTGYAQCgAQGqAQdnd3Mtd2l6sAEG&sclient=psy-ab&ved=0ahUKEwjw0fms6rvsAhVNzhoKHZWPBi8Q4dUDCAY&uact=5')

print(r.text)

f = open('goldtest.html','w')
f.write(r.text)

f.flush()
f.close()




