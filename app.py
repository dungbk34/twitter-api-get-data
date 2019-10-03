# -*- coding: utf-8 -*-

import os
import tweepy as tw
import pandas as pd
from datetime import datetime, timedelta
import json

consumer_key = 'Nfl9DbPnaWOyf3nsXFie2M9FL'
consumer_secret = 'LmApcnTPNU7BJ0DcYdcZg1xJA1UEiXQR9aEwNfdT4BHaKtu4So'
access_token = '1176888876473827328-sTZjVUREBJlWSNl9sGeNzJFJ46zCA4'
access_token_secret = 'Frw4J84Md9iiK7uUow7sORWYmRk7KlHikh62h6IG13APs'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

##############################################################
# Tweets
# Returns the 20 most recent statuses, including retweets, posted by the authenticating user and that user’s friends. This is the equivalent of /timeline/home on the Web.

# Parameters:
# since_id – Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
# max_id – Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
# count – The number of results to try and retrieve per page.
# page – Specifies the page of results to retrieve. Note: there are pagination limits.
# Return type:
# list of Status objects

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# f = open('home_timeline.txt', 'w+')

# for status in tw.Cursor(api.home_timeline).items(1):
#     # Process a single status
# 	json.dump(status._json, f)
# f.close()
#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
# API.user_timeline([id/user_id/screen_name][, since_id][, max_id][, count][, page])
# Returns the 20 most recent statuses posted from the authenticating user or the user specified. It’s also possible to request another user’s timeline via the id parameter.

# Parameters:
# id – Specifies the ID or screen name of the user.
# user_id – Specifies the ID of the user. Helpful for disambiguating when a valid user ID is also a valid screen name.
# screen_name – Specifies the screen name of the user. Helpful for disambiguating when a valid screen name is also a user ID.
# since_id – Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
# max_id – Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
# count – The number of results to try and retrieve per page.
# page – Specifies the page of results to retrieve. Note: there are pagination limits.
# Return type:
# list of Status object

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# f = open('user_timeline.txt', 'w+')

# for status in api.user_timeline('@Cristiano', count=1):
#     # Process a single status
# 	json.dump(status._json, f)

# f.close()


#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
# API.statuses_lookup(id_[, include_entities][, trim_user][, map_][, include_ext_alt_text][, include_card_uri])
# Returns full Tweet objects for up to 100 tweets per request, specified by the id_ parameter.

# Parameters:
# id_ – A list of Tweet IDs to lookup, up to 100
# include_entities – The entities node will not be included when set to false. Defaults to true.
# trim_user – A boolean indicating if user IDs should be provided, instead of complete user objects. Defaults to False.
# map_ – A boolean indicating whether or not to include tweets that cannot be shown. Defaults to False.
# include_ext_alt_text – If alt text has been added to any attached media entities, this parameter will return an ext_alt_text value in the top-level key for the media entity.
# include_card_uri – A boolean indicating if the retrieved Tweet should include a card_uri attribute when there is an ads card attached to the Tweet and when that card was attached using the card_uri value.
# Return type:
# list of Status objects
# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# tweet id =  1179142471542067201

# f = open('statuses_lookup.txt', 'w+')

# for status in api.statuses_lookup(id_ = [1179142471542067201]):
#     # Process a single status
# 	json.dump(status._json, f)

# f.close()


#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
# API.retweets_of_me([since_id][, max_id][, count][, page])
# Returns the 20 most recent tweets of the authenticated user that have been retweeted by others.

# Parameters:
# since_id – Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
# max_id – Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
# count – The number of results to try and retrieve per page.
# page – Specifies the page of results to retrieve. Note: there are pagination limits.
# Return type:
# list of Status objects

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# f = open('retweets_of_me.txt', 'w+')

# for status in api.retweets_of_me(count = 1):
#     # Process a single status
# 	json.dump(status._json, f)

# f.close()
#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
# API.mentions_timeline([since_id][, max_id][, count])
# Returns the 20 most recent mentions, including retweets.

# Parameters:
# since_id – Returns only statuses with an ID greater than (that is, more recent than) the specified ID.
# max_id – Returns only statuses with an ID less than (that is, older than) or equal to the specified ID.
# count – The number of results to try and retrieve per page.
# Return type:
# list of Status objects


# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# f = open('mentions_timeline.txt', 'w+')

# for status in api.mentions_timeline(count = 1):
#     # Process a single status
# 	json.dump(status._json, f)

# f.close()

#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>


### Tweets method
##############################################################
# Status methods
# API.get_status(id[, trim_user][, include_my_retweet][, include_entities][, include_ext_alt_text][, include_card_uri])
# Returns a single status specified by the ID parameter.

# Parameters:
# id – The numerical ID of the status.
# trim_user – A boolean indicating if user IDs should be provided, instead of complete user objects. Defaults to False.
# include_my_retweet – A boolean indicating if any Tweets returned that have been retweeted by the authenticating user should include an additional current_user_retweet node, containing the ID of the source status for the retweet.
# include_entities – The entities node will not be included when set to false. Defaults to true.
# include_ext_alt_text – If alt text has been added to any attached media entities, this parameter will return an ext_alt_text value in the top-level key for the media entity.
# include_card_uri – A boolean indicating if the retrieved Tweet should include a card_uri attribute when there is an ads card attached to the Tweet and when that card was attached using the card_uri value.
# Return type:
# Status object

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # tweet id = 1179332900715667457
# f = open('get_status.txt', 'w+')

# status = api.get_status(id = 1179332900715667457)
# # Process a single status
# json.dump(status._json, f)

# f.close()
#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
# API.retweeters(id[, cursor][, stringify_ids])
# Returns up to 100 user IDs belonging to users who have retweeted the Tweet specified by the id parameter.

# Parameters:
# id – The numerical ID of the status.
# cursor – Breaks the results into pages. Provide a value of -1 to begin paging. Provide values as returned to in the response body’s next_cursor and previous_cursor attributes to page back and forth in the list.
# stringify_ids – Have ids returned as strings instead.
# Return type:
# list of Integers

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # tweet id = 1179332900715667457

# f = open('retweeters.txt', 'w+')

# retweeters = api.retweeters(id = 1179332900715667457)
# # Process a single status
# json.dump(retweeters, f)

# f.close()
#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
    # API.retweets(id[, count])
    # Returns up to 100 of the first retweets of the given tweet.

    # Parameters:
    # id – The numerical ID of the status.
    # count – Specifies the number of retweets to retrieve.
    # Return type:
    # list of Status objects

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # tweet id = 1179332900715667457

# f = open('retweets.txt', 'w+')

# for status in api.retweets(id = 1179332900715667457,count = 1):
#     # Process a single status
# 	json.dump(status._json, f)

# f.close()


#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

###   User method


##############################################################
    #  API.get_user(id/user_id/screen_name)
    # Returns information about the specified user.

    # Parameters:
    # id – Specifies the ID or screen name of the user.
    # user_id – Specifies the ID of the user. Helpful for disambiguating when a valid user ID is also a valid screen name.
    # screen_name – Specifies the screen name of the user. Helpful for disambiguating when a valid screen name is also a user ID.
    # Return type:
    # User object

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## user screen name = '@Cristiano'

# f = open('get_user.txt', 'w+')

# user = api.get_user('@Cristiano')
# json.dump(user._json,f)

# f.close()

#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
    #  API.friends(id/user_id/screen_name)
    # Returns information about the specified user.

    # Parameters:
    # id – Specifies the ID or screen name of the user.
    # user_id – Specifies the ID of the user. Helpful for disambiguating when a valid user ID is also a valid screen name.
    # screen_name – Specifies the screen name of the user. Helpful for disambiguating when a valid screen name is also a user ID.
    # Return type:
    # User object

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## user screen name = '@Cristiano'

# f = open('friends.txt', 'w+')

# for user in api.friends('@Cristiano', count = 5):
#   json.dump(user._json,f)

# f.close()
#
# #  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
    #  API.followers(id/user_id/screen_name)
    # Returns information about the specified user.

    # Parameters:
    # id – Specifies the ID or screen name of the user.
    # user_id – Specifies the ID of the user. Helpful for disambiguating when a valid user ID is also a valid screen name.
    # screen_name – Specifies the screen name of the user. Helpful for disambiguating when a valid screen name is also a user ID.
    # Return type:
    # User object

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## user screen name = '@Cristiano'

# f = open('followers.txt', 'w+')

# for user in api.followers('@Cristiano', count = 5):
#   json.dump(user._json,f)

# f.close()

#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
    #   API.lookup_users([user_ids][, screen_names][, include_entities][, tweet_mode])
    # Returns fully-hydrated user objects for up to 100 users per request.

    # There are a few things to note when using this method.

    # You must be following a protected user to be able to see their most recent status update. If you don’t follow a protected user their status will be removed.
    # The order of user IDs or screen names may not match the order of users in the returned array.
    # If a requested user is unknown, suspended, or deleted, then that user will not be returned in the results list.
    # If none of your lookup criteria can be satisfied by returning a user object, a HTTP 404 will be thrown.
    # Parameters:
    # user_ids – A list of user IDs, up to 100 are allowed in a single request.
    # screen_names – A list of screen names, up to 100 are allowed in a single request.
    # include_entities – The entities node will not be included when set to false. Defaults to true.
    # tweet_mode – Valid request values are compat and extended, which give compatibility mode and extended mode, respectively for Tweets that contain over 140 characters.
    # Return type:
    # list of User object

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## user screen name = '@Cristiano'

# f = open('lookup_users.txt', 'w+')

# for user in api.lookup_users(['@BarackObama', '@realDonaldTrump']):
#       json.dump(user._json,f)

# f.close()

#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##############################################################
    # API.search_users(q[, count][, page])
    # Run a search for users similar to Find People button on Twitter.com; the same results returned by people search on Twitter.com will be returned by using this API (about being listed in the People Search). It is only possible to retrieve the first 1000 matches from this API.

    # Parameters:
    # q – The query to run against people search.
    # count – Specifies the number of statuses to retrieve. May not be greater than 20.
    # page – Specifies the page of results to retrieve. Note: there are pagination limits.
    # Return type:
    # list of User objects



# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## search name = 'cristiano'

# f = open('search_users.txt', 'w+')

# for user in api.search_users(q = 'cristiano', count  = 1):
#       json.dump(user._json,f)

# f.close()

#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# #Friendship Methods
### skip this method
#############################################################
    # API.show_friendship(source_id/source_screen_name, target_id/target_screen_name)
    # Returns detailed information about the relationship between two users.

    # Parameters:
    # source_id – The user_id of the subject user.
    # source_screen_name – The screen_name of the subject user.
    # target_id – The user_id of the target user.
    # target_screen_name – The screen_name of the target user.
    # Return type:
    # Friendship object

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## friend name = '@Snon28281023'

# f = open('show_friendship.txt', 'w+')

# friendship = api.show_friendship(source_screen_name = '@dungbk6', target_screen_name = '@Snon28281023')
# print(friendship)

# f.close()

#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#############################################################
    #     API.friends_ids(id/screen_name/user_id[, cursor])
    # Returns an array containing the IDs of users being followed by the specified user.

    # Parameters:	
    # id – Specifies the ID or screen name of the user.
    # screen_name – Specifies the screen name of the user. Helpful for disambiguating when a valid screen name is also a user ID.
    # user_id – Specifies the ID of the user. Helpful for disambiguating when a valid user ID is also a valid screen name.
    # cursor – Breaks the results into pages. Provide a value of -1 to begin paging. Provide values as returned to in the response body’s next_cursor and previous_cursor attributes to page back and forth in the list.
    # Return type:	
    # list of Integers

# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## friend name = '@Cristiano'

# f = open('friends_ids.txt', 'w+')

# friends_ids = api.friends_ids(screen_name = '@Cristiano')
# json.dump(friends_ids, f)

# f.close()

#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#############################################################
#     API.followers_ids(id/screen_name/user_id)
# Returns an array containing the IDs of users following the specified user.

# Parameters:	
# id – Specifies the ID or screen name of the user.
# screen_name – Specifies the screen name of the user. Helpful for disambiguating when a valid screen name is also a user ID.
# user_id – Specifies the ID of the user. Helpful for disambiguating when a valid user ID is also a valid screen name.
# cursor – Breaks the results into pages. Provide a value of -1 to begin paging. Provide values as returned to in the response body’s next_cursor and previous_cursor attributes to page back and forth in the list.
# Return type:	
# list of Integers
# >>>>>>>>>>>>>>>>>>>>>>>> code begin >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

## friend name = '@Cristiano'

# f = open('followers_ids.txt', 'w+')

# followers_ids = api.followers_ids(screen_name = '@Cristiano')
# json.dump(followers_ids, f)

# f.close()

#  >>>>>>>>>>>>>>>>>>>>>>>>>> end >>>>>>>>>>>>>>>>>>>>>>>>>>>>>