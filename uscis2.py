import re
import os
import time
import sys
from mechanize import Browser

num=sys.argv[1]
comp_str='FIRST'
while True:
    time.sleep(1)
    br = Browser()
    r=br.open("https://egov.uscis.gov/casestatus/landing.do")
    print br.geturl()
    print br.title()
    br.select_form(name="caseStatusForm")
    # Browser passes through unknown attributes (including methods)
    # to the selected HTMLForm (from ClientForm).
    print num
    br["appReceiptNum"] = str(num)  # (the method here is __setitem__)
    response = br.submit()  # submit current form
    stxatus=response.get_all_header_names()
    #print status
    text= br.response().read()
    
    result = re.search('<h1>(.*)</h1>', text).group(1)
    print result
    if result!=comp_str:
	if comp_str=='FIRST':
		comp_str=result
		continue;
	else:
	        break
    time.sleep(60*10)

duration = 1000000  # second
freq = 1000  # Hz
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))        
#print br.geturl()
#print str(response)

#print br.response().read()
