from urllib2 import urlopen
import json
from pprint import pprint
from time import sleep

#numberof results per page
per_p = 100
#doi prefix to limit results
#10.1111 is the doi for molecular ecology, chage pre_doi and journal to what ever you want
pre_doi = 10.1111
journal = "Molecular Ecology"
dataset = [];
dataset2 = [];
count = 0;
#calculates the number of pages of data using per_p and the given doi prefix
#the time frame it looks at is currently 1day (1d) just after citations in url
#change time frame according to http://api.altmetric.com/docs/call_citations.html
url = 'http://api.altmetric.com/v1/citations/1d?key=e4370450513b6942dfb303c6262460d9&num_results=%s&doi_prefix=%s' % (per_p,pre_doi)
url_file = urlopen(url).read()
jdata = json.loads(url_file)
#add in an if statement to deal with over 100 pages
if jdata['query']['total'] / per_p +2 > 100:
	pages = 100
else:
	pages = jdata['query']['total'] / per_p +2

for pagee in range(1,pages):
#insert a sleep break between pages to avoid overloading servers
	sleep(0.5)
	
	url = 'http://api.altmetric.com/v1/citations/1w?key=e4370450513b6942dfb303c6262460d9&num_results=%s&page=%s&doi_prefix=%s' % (per_p,pagee,pre_doi)
#reads api page url and stores it as dictionary
	url_file = urlopen(url).read()
	jdata = json.loads(url_file)
#jdata is a dictionary where results: is the 2nd dict
#and it is a list of dictionaries, one for each article

#for each article that is in the specified journal the score history. The
#output is a list with a dictionary for each article
	for i in jdata['results']:
		if 'journal' in i:
			if i['journal'] == journal:
# mydict.get('dey') returns the contents if it exists but none if not
#				print i['cohorts'].get('sci')
				if isinstance(i['cohorts'],dict):
					if i['cohorts'].get('sci') == None:
						cohort = {'sci':0}
					else:
						cohort = {'sci':i['cohorts'].get('sci')}
					if i['cohorts'].get('pub')== None:
						cohort.update({'pub':0})
					else:
						cohort.update({'pub':i['cohorts'].get('pub')})
					if i['cohorts'].get('com')== None:
						cohort.update({'com':0})
					else:
						cohort.update({'com':i['cohorts'].get('com')})
					if i['cohorts'].get('doc')== None:
						cohort.update({'doc':0})
					else:
						cohort.update({'doc':i['cohorts'].get('doc')})
				else:
					cohort={'sci':0}
					cohort.update({'pub':0})
					cohort.update({'com':0})
					cohort.update({'doc':0})					
				cohort.update({'title':json.dumps(i.get('title'))[1:-1]})
				cohort.update({'url':json.dumps(i['url'])})
				cohort.update({'details_url':json.dumps(i.get('details_url'))})
				cohort.update({'image':json.dumps(i['images'].get('large'))})
				cohort.update({'count':count})
				dataset2.append(cohort)


				coordinates = [];
				#print cohort['sci']
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':0, 'past_score':i['history']['at']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':1, 'past_score':i['history']['at'] - i['history']['1d']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':2, 'past_score':i['history']['at'] - i['history']['2d']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':3, 'past_score':i['history']['at'] - i['history']['3d']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':4, 'past_score':i['history']['at'] - i['history']['4d']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':5, 'past_score':i['history']['at'] - i['history']['5d']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':6, 'past_score':i['history']['at'] - i['history']['6d']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':7, 'past_score':i['history']['at'] - i['history']['1w']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':30, 'past_score':i['history']['at'] - i['history']['1m']})
				coordinates.append({'title':cohort['title'],'url':cohort['url'],'details_url':cohort['details_url'],'image':cohort['image'],'count':cohort['count'],'sci':cohort['sci'], 'pub':cohort['pub'], 'com':cohort['com'], 'doc':cohort['doc'], 'd_ago':90, 'past_score':i['history']['at'] - i['history']['3m']})
				#coordinates.append({'d_ago':180, 'past_score':i['history']['at'] - i['history']['6m']})
				#coordinates.append({'d_ago':365, 'past_score':i['history']['at'] - i['history']['1y']})
				article_dict = {}
				article_dict.update({'history':coordinates})
				dataset.append(article_dict)
				count = count + 1


				
f = open('url_file.txt','w')
f.write(str(dataset))
#f.write("; \n var dataset2 = ")
#f.write(str(dataset2))
f.close()
