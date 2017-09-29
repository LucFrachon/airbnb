# -*- coding: utf-8 -*-
"""
Author: Luc Frachon

"""

import mechanize
import cookielib
from lxml import html
import csv
import re
from random import randint
from time import sleep
from lxml.etree import tostring
import bs4
import pandas
import json


def full_listing_search(location = "Aberdeen%29%29UK", limit = None):  #TODO: write full_listing_search function
    """
    Lists all properties in a specific locations up to the specified limit. If limit exceeds 1000 (max listing
    number for a single query), automatically applies an offset to get the next set of listings.
    Returns: A Python dictionary converted from a JSON file.
    """
    #execute HTTP GET  https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&location=...
    return


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

