#!/usr/bin/env python
from bda.awstatsparser.parser import ParsedStatistics
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(formatter)
logger.addHandler(console)

AWSTATS_DIR = '/files/var/awstats/'

class Statistics:
    
    def __init__(self, journal):
        
        self.journal = journal
        data_dir = AWSTATS_DIR + self.journal
        if not os.path.isdir(data_dir):
            logger.error("Directory %s does not exist" % data_dir)
        logger.info("Parsing %s" % data_dir)
        self.parser = ParsedStatistics(self.journal, data_dir )
        self.available = self.parser.available
        
    def available_years(self):
        """Return a list of years (int) for which data are available """

        years = [int(y[2:6]) for y in self.parser.available]
        return list(set(years))

    def months(self, year):
        """Return the month of a given year in awstats MMYYYY format"""

        return ["%02d%s" % (m, year) for m in range(1, 13)]

    def get_data(self, year, urls):
        """return the access statistics of a given url and year"""
        
        months = self.months(year)
        entries = {}
        for url in urls:
            entries[url] = dict.fromkeys(months)

        for month in months:
            if month in self.available:
                # probably not the most elegant way, but sometimes getting parser[month]
                # fails although it is in self.available   
                try:
                    month_parser = self.parser[month]
                except:
                    month_parser = {}
             
                sider = month_parser.get('SIDER',None)
                #sider = self.parser[month].get('SIDER',None)
                if sider:
                    for url in urls:
                        stats = sider.get(url, None)
                        if stats:
                            entries[url][month] = int(stats.get('entry', 0))
                        else:
                            entries[url][month] = 0
        return entries

if __name__ == '__main__':
    
    #urls = ['/archiv/2010/2723/dippArticle.xml']#, '/archiv/2010/2723/SomaliWritingsPDF','/archiv/2010/2723']
    #urls = ['/archiv/2010/2723/SomaliWritingsPDF','/archiv/2010/2723']
    urls = ['/archiv/2010/2723']
    stats = Statistics('afrika')
    year = 2015
    data =  stats.get_data(year, urls)
    for url in stats.get_data(year, urls).keys():
        print url, data[url] 
