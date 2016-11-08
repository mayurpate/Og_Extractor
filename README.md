# Og_Extractor
Python Library to Extract Open Graph Information from HTML Page.

This library extracts open graph information from HTML page. The URL for the HTML page will be the input to the library.

Usage:

```python
import PyOG

og_meta = PyOG("http://www.imdb.com/title/tt2543164/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2495768482&pf_rd_r=01VA8VJV6TES3DRV8JKV&pf_rd_s=right-4&pf_rd_t=15061&pf_rd_i=homepage&ref_=hm_otw_t1")

print og_meta.og_data    =>   This data will have complete list of OG tags

basic_og_data = og_meta.extract_basic_og_metadata()  => This will output OG data for basic tags such as URL, title, image etc.

optional_og_data = og_meta.extract_optional_og_metadata() => This will output OG data for optional tags such as audio, video, description etc.
```


