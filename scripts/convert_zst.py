import csv
import json
import wget
import pandas
import zstandard as zstd
import io
import re
import requests
from bs4 import BeautifulSoup


REDDIT_URL  = "https://files.pushshift.io/reddit/"

# collects URLs for monthly dumps, has to be robust to file type changes
def gather_dump_urls(base_url, mode):
    page    = requests.get(base_url + mode)
    soup    = BeautifulSoup(page.content, 'lxml')
    files   = [it for it in soup.find_all(attrs={"class":"file"})]
    f_urls  = [tg.find_all(lambda x:x.has_attr('href'))[0]['href']
               for tg in files if len(tg.find_all(lambda x:x.has_attr('href'))) > 0]
    date_to_url    = {}
    for url_st in f_urls:
        ls  = re.findall(r"20[0-9]{2}-[0-9]{2}", url_st)
        if len(ls) > 0:
            yr, mt  = ls[0].split('-')
            date_to_url[(int(yr), int(mt))] = base_url + mode + url_st[1:]
    return date_to_url

# select valid top-level comments
def valid_comment(a):
    res = len(a['body'].split()) > 2 and \
          not a['body'].startswith('Your submission has been removed') and \
          a['author'] != 'AutoModerator' and a['parent_id'] == a['link_id']
    return res


# fh = open("./test.zst", 'rb')
# dctx = zstd.ZstdDecompressor(max_window_size=2147483648)
# stream_reader = dctx.stream_reader(fh)
# f = io.TextIOWrapper(stream_reader, encoding='utf-8')

# res = []



# for i, l in enumerate(f):
#     res.append(l.strip())

# # with open("./test.zst", "rb") as f:     
# #     data = f.read()

# # compressor = zstandard.ZstdCompressor()

# # dctx = zstandard.ZstdDecompressor()
# # decompressed = dctx.decompress(data, max_output_size=1048576)

# fo = open('data.json', "w")
# json.dump(res, fo, ensure_ascii=False, indent=4)
# fo.close()

# # with open('data.json', 'w', encoding='utf-8') as f:
# #     json.dump([l.strip() for l in enumerate(f)], f, ensure_ascii=False, indent=4) 