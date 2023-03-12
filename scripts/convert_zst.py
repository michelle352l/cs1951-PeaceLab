import csv
import json
import wget
import pandas
import zstandard

url = "https://files.pushshift.io/reddit/comments/RC_2008-01.zst"
response = wget.download(url, "./test.zst")

with open("./test.zst", "rb") as f:     
    data = f.read()

compressor = zstandard.ZstdCompressor()

dctx = zstandard.ZstdDecompressor()
decompressed = dctx.decompress(data, max_output_size=1048576)

with open('test.txt', 'w') as f:
    f.writelines(decompressed)