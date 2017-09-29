# -*- coding: utf-8 -*-
"""
Author: Luc Frachon

"""

#import mechanize
#import cookielib
#from lxml import html
#import csv
#import re
#from lxml.etree import tostring
#import bs4
#from frange import *
import pandas as pd
import collections
from random import randint
from time import sleep
import urllib2
import json

hdr = {'User-Agent': 'Mozilla/5.0'}  # header for URL requests
MAX_LISTINGS_PER_SEARCH = 50  # max number of listings that the API can return per request
MAX_LISTINGS_PER_LOCATION = 300  # max number of listings that the API can return per location

def full_listing_search(location, min_price = 20, max_price = 1000, price_bands = 5, num_tries = 3):
    """
    Lists all properties in a specific locations up to the specified limit. If limit exceeds 1000 (max listing
    number for a single query), automatically applies an offset to get the next set of listings.
    Returns: A Python dictionary converted from a JSON file.
    """
    
    base_url = "https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&location=" + location
    listings = []
    # dict of dicts that keeps track of how many records were added for each price band and offset value
    records = collections.defaultdict(dict)  
    
    for price in range(min_price, max_price + 1, price_bands):
    # split search in price unit increments of 'price_bands' to avoid the 300 results limit.
        lower = price
        upper = price + price_bands - 1
        offset = 0
            
        while True:
            success = False

            for i in range(num_tries):
                if not success:
                    try:
                        # build query URL
                        full_url = base_url + '&_limit=' + str(MAX_LISTINGS_PER_SEARCH) + '&_offset=' + str(offset)
                        full_url += '&price_min=' + str(lower) + '&price_max=' + str(upper)

                        # send request and get results
                        req = urllib2.Request(full_url, headers = hdr)
                        print "\nRetrieving data from URL %s" %(full_url)

                        # introduce a random pause then execute request
                        sleep(randint(0., 1.))  
                        open_url = urllib2.urlopen(req)

                        # returned codes from HTTP request
                        #code = open_url.getcode()

                        # convert returned JSON into Python dictionary
                        json_search_results = json.loads(open_url.read())
                        num_added_items = len(json_search_results['search_results'])
                        print "Adding " + str(num_added_items) + " listings."
                
                        # store search results in a list (discard metadata)
                        listings.extend(json_search_results['search_results'])
                        print "length: " + str(num_added_items)
                
                        # request was executed successfully (which causes exit form the for loop)
                        success = True
                        
                    except:
                        print "This URL has not returned any results. Depending on settings, I may try again."

            
            # increment offset for next request
            offset += MAX_LISTINGS_PER_SEARCH

            # exit loop if we've encountered all listings for this offset value
            if num_added_items == 0:
                break
            else: # otherwise record the number of listings found
                records[price][offset - MAX_LISTINGS_PER_SEARCH] = num_added_items

            # exit loop when offset reaches its max possible value (currently 250 on the Abnb API)
            if offset > MAX_LISTINGS_PER_LOCATION - MAX_LISTINGS_PER_SEARCH:
                break

    return listings, records


def convert_to_dataframe(records_dict):

    return pd.DataFrame.from_dict(records_dict, orient = 'index', dtype = 'int')


def extract_userids(listings):  #TODO: write extract_userids function
    """
    Takes a dictionary containing Airbnb listings for a location and extracts a list of all user IDs that appear
    in those listings.
    Returns: A Python list.
    """
    return

def get_hosts_listings(userids):  #TODO: write get_hosts_listings function
    """
    Takes a list of user ids and collects all listings belonging to these hosts.
    Returns: A Python dictionary converted from a JSON file.
    """
    #for each userid in userids:
        #execute HTTP GET https://api.airbnb.com/v2/listings/?client_id=3092nxybyb0otqw18e8nh5nty&user_id=...
        #add returned data to dict, using userid as the key
    return

