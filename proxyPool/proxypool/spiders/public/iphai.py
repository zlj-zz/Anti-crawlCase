from proxypool.schemas.proxy import Proxy
from proxypool.spiders.base import BaseSpider
import re

BASE_URL = 'http://www.iphai.com/'


class IPHaiSpider(BaseSpider):
    """
    iphai crawler, http://www.iphai.com/
    """
    urls = [BASE_URL]

    def parse(self, html):
        """
        parse html file to get proxies
        :return:
        """
        find_tr = re.compile('<tr>(.*?)</tr>', re.S)
        trs = find_tr.findall(html)
        for s in range(1, len(trs)):
            find_ip = re.compile(r'<td>\s+(\d+\.\d+\.\d+\.\d+)\s+</td>', re.S)
            re_ip_address = find_ip.findall(trs[s])
            find_port = re.compile(r'<td>\s+(\d+)\s+</td>', re.S)
            re_port = find_port.findall(trs[s])
            for address, port in zip(re_ip_address, re_port):
                proxy = Proxy(host=address.strip(), port=int(port.strip()))
                yield proxy
