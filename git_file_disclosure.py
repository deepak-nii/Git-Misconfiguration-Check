import http.client
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file', type=argparse.FileType('r'))
args = parser.parse_args()

gitDir = ['/.git/','/.git/HEAD']
for line in args.file.readlines():
    conn = http.client.HTTPSConnection(line.strip())
    for abc in gitDir:
        conn.request("GET",abc)
        res = conn.getresponse()
        res.read()
        if (res.status == 200):
            print (line.strip()+' is vulnerable')
            break
