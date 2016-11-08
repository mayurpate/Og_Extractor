from BeautifulSoup import BeautifulSoup
import urllib2

BASIC_OG_METADATA = ['title', 'image', 'url', 'type']
OPTIONAL_OG_METADATA = ['audio', 'determiner', 'locale', 'description', 'site_name', 'video']

class PyOG(object):
    
    def __init__(self, url = None):
        if not url:
            raise Exception("Please pass the URL.Can not retrive OG information without URL.")
        self.og_data = {}
        response = urllib2.urlopen(url)
        html = response.read()
        parsed_html = BeautifulSoup(html)
        self.og_data = {'title': self.extract_og_key(parsed_html, 'title'),
                    'image': self.extract_og_key(parsed_html, 'image'),
                    'url': self.extract_og_key(parsed_html, 'url'),
                    'type': self.extract_og_key(parsed_html, 'type'),
                    'description': self.extract_og_key(parsed_html, 'description'),
                    'audio': self.extract_og_key(parsed_html, 'audio'),
                    'determiner': self.extract_og_key(parsed_html, 'determiner'),
                    'locale': self.extract_og_key(parsed_html, 'locale'),
                    'site_name': self.extract_og_key(parsed_html, 'site_name'),
                    'video': self.extract_og_key(parsed_html, 'video')
                }
    
    def extract_og_key(self, html, og_key = 'type'): 
        og_data = html.find(attrs = {'property':'og:%s' %(og_key)}) or \
                                html.find(attrs = {'name': 'og:%s' %(og_key)})
        return og_data.get('content') if og_data else None

    def extract_basic_og_metadata(self):
        basic_og_data = {}
        if not self.og_data:
            raise Exception("Can not extract basic info without PyOG object. Please initiate PyOG object with URL.")
        for key,val in self.og_data.iteritems():
            if key in BASIC_OG_METADATA:
                basic_og_data.update({key:val})
        return basic_og_data

    def extract_optional_og_metadata(self):
        optional_og_data = {}
        if not self.og_data:
            raise Exception("Can not extract basic info without PyOG object. Please initiate PyOG object with URL.")
        for key,val in self.og_data.iteritems():
            if key in OPTIONAL_OG_METADATA:
                optional_og_data.update({key:val})
        return optional_og_data


if __name__ == '__main__':
    og_object = PyOG('http://www.imdb.com/title/tt2543164/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2495768482&pf_rd_r=01VA8VJV6TES3DRV8JKV&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_otw_t1')
    print og_object.og_data
    basic_og_data = og_object.extract_basic_og_metadata()
    print basic_og_data
    optional_og_data = og_object.extract_optional_og_metadata()
    print optional_og_data
