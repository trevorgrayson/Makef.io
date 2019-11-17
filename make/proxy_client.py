from urllib.parse import urlparse
from http.client import HTTPSConnection

from make.config import TARGET_HOST

class ProxyClient:
    def __init__(self, base_url):
        self.base_url = base_url

        url = urlparse(self.base_url % 'none')
        self.conn = HTTPSConnection(url.netloc)


    def url(self, name):
        url = urlparse(self.base_url % name)
        return url.path + "?" + url.query

    def read(self, name):
        self.conn.request('GET', self.url(name))
        resp = self.conn.getresponse()

        if resp.status == 200:
            return resp.read().decode('utf-8')
        else:
            resp.read()
            raise Exception(f"Proxy HTTP Read exception: {resp.status}")
        


if __name__ == '__main__':
    client = ProxyClient(TARGET_HOST)
    print(client.read('python'))
