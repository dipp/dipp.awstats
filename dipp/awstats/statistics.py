#!/usr/bin/env python
from bda.awstatsparser.parser import ParsedStatistics

parser = ParsedStatistics('afrika','/files/var/awstats/afrika')

for month in parser.available:
    print month
    sider = parser[month].get('SIDER',None)
    if sider:
        stat = sider.get('/archiv/2013/3754/', None)
        print stat
