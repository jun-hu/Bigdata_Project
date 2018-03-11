import urllib.parse as parse

values={
'a':103,
'b':104}

data=parse.urlencode(values)
print(data)

