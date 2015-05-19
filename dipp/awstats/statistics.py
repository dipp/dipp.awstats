#!/usr/bin/env python
from bda.awstatsparser.parser import ParsedStatistics

AWSTATS_DIR = '/files/var/awstats/'

class Statistics:
    
    def __init__(self, journal):
        
        self.journal = journal
        self.parser = ParsedStatistics(self.journal, AWSTATS_DIR + self.journal)
        
    def available_years(self):
        """Return a list of years (int) for which data are available """

        years = [int(y[2:6]) for y in self.parser.available]
        return list(set(years))

    def months(self, year):
        """Return the month of a given year in awstats MMYYYY format"""

        return ["%02d%s" % (m, year) for m in range(1, 13)]

    def get_data(self, year, urls):
        """return the access statistics of a given url an year"""
        
        months = self.months(year)
        entries = {}
        for url in urls:
            entries[url] = dict.fromkeys(months)

        for month in months:
            if month in self.parser.available:
                sider = self.parser[month].get('SIDER',None)
                for url in urls:
                    stats = sider.get(url, None)
                    if stats:
                        entries[url][month] = int(stats.get('entry', 0))
                    else:
                        entries[url][month] = 0
        return entries

if __name__ == '__main__':
    
    urls = ['/archiv/2010/2723/dippArticle.xml']#, '/archiv/2010/2723/SomaliWritingsPDF','/archiv/2010/2723']
    #urls = ['/archiv/2010/2723/SomaliWritingsPDF','/archiv/2010/2723']
    #urls = ['/archiv/2010/2723']
    stats = Statistics('afrika')
    
    data =  stats.get_data(2013, urls)
    for url in stats.get_data(2013, urls).keys():
        print url, data[url] 
