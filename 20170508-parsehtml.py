# -*- coding: utf-8 -*-
from lxml import etree
import urllib

web = urllib.urlopen("http://www.whatsmypass.com/the-top-500-worst-passwords-of-all-time")
s = web.read()

html = etree.HTML(s)

## Get all 'tr'
tr_nodes = html.xpath('//table[@id="Report1_dgReportDemographic"]/tr')

## 'th' is inside first 'tr'
header = [i[0].text for i in tr_nodes[0].xpath("th")]

## Get text from rest all 'tr'
td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]