#!/usr/bin/env python
from bda.awstatsparser.parser import ParsedStatistics

class Statistics:
    
    def __init__(self, year, journal, urls):
        
        self.journal = journal
        self.year = year
        self.urls = urls
        self.parser = ParsedStatistics(self.journal, '/files/var/awstats/' + self.journal)
        
    def available_years(self):
        years = [int(y[2:6]) for y in self.parser.available]
        return list(set(years))

    def get_data(self):
        
        months = ["%02d%s" % (m, self.year) for m in range(1, 13 )]
        for month in months:
            if month in self.parser.available:
                try:
                    sider = self.parser[month].get('SIDER',None)
                    for url in self.urls:
                        stat = sider.get(url, None)
                except:
                    stat = ":("
            print month, stat
             

if __name__ == '__main__':
    
    urls = ['/archiv/2013/3754/']
    stats = Statistics(2014, "afrika", urls)
    print stats.available_years()
    #print stats.get_data()
