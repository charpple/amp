# coding=utf-8

from twitter import *

import sys
import unicodecsv as csv

#moscow
latitude = 55.704751
longitude = 37.558465

#New York
#latitude = 40.759131
#longitude = -73.985356

#Eaketerininburg
#latitude = 56.832604
#longitude = -60.573237

#56.832604, 60.573237
max_range = 2
num_results = 1000
outfile = "tweets.csv"


config = {}
execfile("config.py", config)


twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


csvfile = file(outfile, "w")
csvwriter = csv.writer(csvfile)


row = [ "user", "text"]
csvwriter.writerow(row)



result_count = 0
last_id = None
while result_count <  num_results:

	query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)

	for result in query["statuses"]:

		if result["geo"]:
			user = result["user"]["screen_name"]
			text = result["text"]


			row = [ "@"+user.encode("utf-8"), text.encode("utf-8")]
			csvwriter.writerow(row)

			result_count += 1
		last_id = result["id"]


	print "got %d results" % result_count


csvfile.close()
