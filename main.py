# -*- coding: utf-8 -*-
"""
Test module for functions
"""

from query_and_extract import *
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Take price bracket information for Airbnb search')
    parser.add_argument('location', 
                         type = str, 
                         help = 'Location where to run the search (normally "Town--Country_code" e.g. "Aberdeen--UK"). Use HTML URL encoding for non-alphanumeric characters (see https://www.w3schools.com/TagS/ref_urlencode.asp)')
    parser.add_argument('min_price', 
                        type = int, 
                        help = 'Lower price bound for search request')
    parser.add_argument('max_price', 
                        type = int, 
                        help = 'Upper price bound for search request')
    parser.add_argument('price_bands', 
                        type = int, 
                        help = 'Size of price bands for search request. Reduce if hitting the 300 listings limit, or increase to speed up search.')
    parser.add_argument('num_tries',
                        type = int,
                        help = 'How many times to try a failing request.')
    args = parser.parse_args()
    listings, records = full_listing_search(location = args.location,
                                          #"Kotel%29%29Bulgaria", 
                                          #"Aberdeen%29%29UK",
                                          min_price = args.min_price,
                                          max_price = args.max_price,
                                          price_bands = args.price_bands,
                                          num_tries = args.num_tries)

    ids = [listing['listing']['id'] for listing in listings]
    #ids.sort()
    #
    idset = set(ids)
    names = [listing['listing']['name'] for listing in listings]
    namesset = set(names)
    
    print("\n")
    print("Number of elements: " + str(len(listings)) + "\n")
    print("Number of unique elements: " + str(len(idset)) + "\n")
    print("Diagnostics: {min_price: {offset: number_in_listing}}\n")
    print("If requests with offset 250 return 50 results, you're hitting")
    print("the 300 listings limit. Consider narrowing your price bands.\n")
    userids = extract_userids(listings)
    hosts_ratings = convert_to_dataframe(get_hosts_listings(userids))
    hosts_ratings.to_csv('hosts_ratings.csv')
