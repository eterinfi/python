# Let's demo a working application that showcases one of the 19 APIs available within the Watson Developer Cloud: the Personality Insights (PI) API.

# The name of this application is Celebrity Match.

# The application does the following:

# Accepts two Twitter usernames as variables
# Retrieves the last 200 Tweets from each Twitter username
# Sends the text of the 200 Tweets to the Personality Insights (PI) API (covered in more detail later in this course) to gain insights on the two users
# Compares the users to one another
# Displays the results of the comparison
# The final results displayed will be the top 5 traits shared between the two Twitter users (for example: you and a celebrity of your choice).

# The results are displayed in the following format:

# Matched Personality Trait -> Probability of your profile exhibiting given trait -> Probability of Celebrity's profile exhibiting given trait.

# Note: To successfully run this demo, a Twitter account and Twitter API credentials are required.

import sys
import requests
import json
import operator
import twitter
import script as pi
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights 

#This function is used to receive and analyze
#the last 200 tweets of a Twitter handle using
#the Watson PI API
def analyze(handle):

	#The Twitter API credentials
	twitter_consumer_key = 'ADD YOUR CONSUMER KEY HERE'
	twitter_consumer_secret = 'ADD YOUR CONSUMER SECRET HERE'
	twitter_access_token = 'ADD YOUR ACCESS TOKEN HERE'
	twitter_access_secret = 'ADD YOUR ACCESS SECRET HERE'

	#Invoking the Twitter API
	twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                  consumer_secret=twitter_consumer_secret,
                  access_token_key=twitter_access_token,
                  access_token_secret=twitter_access_secret)

	#Retrieving the last 200 tweets from a user
	statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

	#Putting all 200 tweets into one large string called "text"
	text = "" 
	for s in statuses:
	    if (s.lang =='en'):
    			text += s.text.encode('utf-8')

	#Analyzing the 200 tweets with the Watson PI API
	pi_result = PersonalityInsights(username=pi.u, password=pi.p).profile(text)

	#Returning the Watson PI API results
	return pi_result

#This function is used to flatten the result 
#from the Watson PI API
def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data


#This function is used to compare the results from
#the Watson PI API
def compare(dict1, dict2):
	compared_data = {}
	for keys in dict1:
    		if dict1[keys] != dict2[keys]:
			compared_data[keys] = abs(dict1[keys] - dict2[keys])
	return compared_data


#The two Twitter handles
user_handle = "@ADD YOUR TWITTER USERNAME HERE"
celebrity_handle = "@IBM" 

#Analyze the user's tweets using the Watson PI API
user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)

#Flatten the results received from the Watson PI API
user = flatten(user_result)
celebrity = flatten(celebrity_result)

#Compare the results of the Watson PI API by calculating
#the distance between traits
compared_results = compare(user,celebrity)

#Sort the results
sorted_results = sorted(compared_results.items(), key=operator.itemgetter(1))

#Print the results to the user
for keys, value in sorted_results[:5]:
	print keys ,
	print (user[keys]),
	print ('->'),
	print (celebrity[keys]),
	print ('->'),
	print (compared_results[keys])
