# Assessing host quality with the Airbnb API 

This small project uses the no-longer maintained Airbnb API v2.0 to extract listings in the location and
price range specified by the user, then extract a list of the corresponding hosts. Next, it extracts 
all listings for each of these hosts along with these listing's ratings and number of reviews, then
computes the average rating of each host.

The idea is to allow the user to get an idea of who they are dealing with.

## To run:

- Required library: pandas
- Runs in Python 2.7
- On the command line, type:
`python main.py <location> <min_price> <max_price> <price_bands> <num_tries>`

where:

- location: Location you are interested in. Typical format is "Town%29%29Coutry"
    or "Town%29%29Region%29%29Country", using HTML URL encoding for non-alphanumeric characters (see https://www.w3schools.com/TagS/ref_urlencode.asp)
- min_price: Lower end of the price bracket you are interested in
- max_price: Upper end of the price bracket
- price_bands: The Airbnb API has a limit of 50 listings per request and a maximum offset of 250,
which means that it will not return more than 300 listings per location per price range. The work-around
is to specify a narrower price band in the request. This is what price_bands does: It divides the request
into smaller ones, each covering `price_bands` units of the local currency.
- num_tries: How many times should a request be attempted when not successful?
    
 Host-related results are saved in a .csv file named hosts_ratings.csv.
