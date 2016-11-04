from BeautifulSoup import BeautifulSoup
import urllib2

def extract_basic_og_info(url): 
    '''
    This Fuction mainly returns basic OG info. 
    This includes title, image, url, type and description.
    '''
    if not url:
        raise Exception("Please pass the URL.Can not retrive OG information without URL.")
    resp = {}
    response = urllib2.urlopen(url)
    html = response.read()
    parsed_html = BeautifulSoup(html)
    resp = {'title': _extract_og_key(parsed_html, 'title'),
            'image': _extract_og_key(parsed_html, 'image'),
            'url': _extract_og_key(parsed_html, 'url'),
            'type': _extract_og_key(parsed_html, 'type'),
            'description': _extract_og_key(parsed_html, 'description')
            }
    print resp
    return resp


def extract_optional_og_info(url):
    if not url:
        raise Exception("Please pass the URL.Can not retrive OG information without URL.")
    resp = {}
    response = urllib2.urlopen(url)
    html = response.read()
    parsed_html = BeautifulSoup(html)
    resp = {'audio': _extract_og_key(parsed_html, 'audio'),
            'determiner': _extract_og_determiner(parsed_html, 'determiner'),
            'locale': _extract_og_locale(parsed_html, 'locale'),
            'site_name': _extract_og_type(parsed_html, 'site_name'),
            'video': _extract_og_description(parsed_html, 'video')
            }
    print resp
    return resp


def _extract_og_key(html, og_key = 'type'): 
    og_data = html.find(attrs = {'property':'og:%s' %(og_key)}) or html.find(attrs = {'name': 'og:%s' %(og_key)})
    return og_data.get('content') if og_data else None

if __name__ == '__main__':
    extract_basic_og_info('http://www.jetsetter.com/hotels/new-orleans/louisiana/8113/ace-hotel-new-orleans?nm=marketsplash&rid=2&cl=4&ca=todays-sales')

     
