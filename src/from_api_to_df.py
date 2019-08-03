# Import all of the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json, requests
import os

# List our necessary url's
categories_url = 'https://api.foursquare.com/v2/venues/categories'
explore_url = 'https://api.foursquare.com/v2/venues/explore'
details_url_first_part = 'https://api.foursquare.com/v2/venues/'

# Identify all of the categories under 'Food'

# Set parameters for categories. v is version. ll is longitude and latitude
# cat_params = dict(client_id=os.environ['FOURSQUARE_API_CLIENT_ID'],
#       client_secret=os.environ['FOURSAURE_API_CLIENT_SECRET'],
#       v='20190510',
#       ll='40.0150,-105.2705')

cat_params = dict(client_id=FOURSQUARE_API_CLIENT_ID,
      client_secret=FOURSQUARE_API_CLIENT_SECRET,
      v='20190510',
      ll='33.7490,-84.3880')

# Requests GET and load JSON into a text format
cat_response = requests.get(url=categories_url, params=cat_params)
categories_data = json.loads(cat_response.text)

# Define get_categories function that lists out all of the 'Food' categories/sub-categories and get their counts.
def get_categories(data):
    
    cat_count = 0 
    sub_count = 0
    sub2_count = 0
    cats = []
    
    
    for category in data['response']['categories']:
        if category['name'] == 'Food':
            cat_count += 1
            # print(category['name'])
            cats.append(category['name'])
            for sub_category in category['categories']:
                sub_count += 1
                # print('----',sub_category['name'])
                cats.append(sub_category['name'])
                for sub_cat_2 in sub_category['categories']:
                    sub2_count += 1
                    # print('    ','----',sub_cat_2['name'])
                    cats.append(sub_cat_2['name'])

    total_count = cat_count + sub_count + sub2_count                
# To see how many of each types of categories there are, uncomment the print statements below
    # print("categories: ", cat_count)
    # print("subcategories: ", sub_count)
    # print("sub2 categories: ", sub2_count)
    # print("total: ", total_count)

    return cats

cats = get_categories(categories_data)

# Return all categories and subcategories
# cats = get_categories(categories_data)

# Identify all of the unique id's for the categories under 'Food'

# Parse through to get just id's 
def parse_category_for_id(response_data):
    lst = [] 
#     count = 0
    for item in response_data['response']['groups']:
        for restaurant in item['items']:
            lst.append((restaurant['venue']['id']))
    return lst

# Explore GET requets to get all of the restaurants under 'Food'
# def explore_restaurants_by_category(category):
#     explore_params = dict(client_id=os.environ['FOURSQUARE_API_CLIENT_ID'],
#       client_secret=os.environ['FOURSQUARE_API_CLIENT_SECRET'],
#       v='20190510',
#       ll='40.0150,-105.2705',  
#       query=category,
#       limit=120)
    
def explore_restaurants_by_category(category):
    explore_params = dict(client_id=FOURSQUARE_API_CLIENT_ID,
      client_secret=FOURSQUARE_API_CLIENT_SECRET,,
      v='20190510',
      ll='33.7490,-84.3880',  
      query=category,
      limit=120)

    explore_response = requests.get(url=explore_url, params=explore_params)
    explore_data = json.loads(explore_response.text)
    
    return parse_category_for_id(explore_data)

# Get all of the unique id's of the restaurants
def get_unique_ids(categories):
    main_id = []
    for category in categories:
        main_id.append(explore_restaurants_by_category(category))
    flat_list = []
    for sublist in main_id:
        for item in sublist:
            flat_list.append(item)
    return set(flat_list)

unique_ids = get_unique_ids(cats)


# Get restaurant details for all restaurants using unique id's from above

def get_all_restaurant_details(unique_ids):

    details_lst = []

    details_params = dict(client_id=FOURSQUARE_API_CLIENT_ID,
      client_secret=FOURSQUARE_API_CLIENT_SECRET,,
          v='20190510',
          ll='33.7490,-84.3880',  
          section='food',
          limit=120)

    for uid in unique_ids:
        details_url_by_venue = details_url_first_part + uid
        details_response = requests.get(url=details_url_by_venue, params=details_params)
        details_data = json.loads(details_response.text)
        details_lst.append(details_data)
    return details_lst

details_lst = get_all_restaurant_details(unique_ids)

# Transform details list to final, usable pandas dataframe

def create_df(details_lst):

    # Parse through JSON object (i.e. dictionaries and lists) to get to usable format
    dtf = pd.DataFrame(details_lst)
    dtf2 = pd.DataFrame(dtf['response'])
    dtf3 = dtf2['response']
    dtf4 = pd.DataFrame(dtf3)

    # Create empty lists to be used as columns for the final dataframe. 
    # Some empty lists have been taken out in the final DF but left initiatied in case users would want to include them in future cases.
    unique_id = []
    name = [ ]
    phone = []
    twitter = []
    city = []
    state = []
    canonicalUrl = []
    categories = []
    verified = []
    stats = []
    url = []
    price = []
    hasMenu = []
    likes = []
    dislike = []
    ok = []
    rating = []
    menu = []
    allowMenuUrlEdit = []
    beenHere = []
    specials = []
    photos = []
    reasons = []
    page = []
    hereNow = []
    tips = []
    shortUrl = []
    timeZone = []
    listed = []
    hours = []
    popular = []
    attributes = []
    price = []

    # Continue parsing through JSON object. Append JSON data into created lists above.
    for a in dtf4['response']:
        for k, v in a.items():
            unique_id.append(v['id'])
            name.append(v['name'])
            phone.append(v['contact'].get('phone', 'NaN'))
            twitter.append(v['contact'].get('twitter', 'NaN'))
            city.append(v['location'].get('city', 'NaN'))
            state.append(v['location'].get('state', 'NaN'))
            canonicalUrl.append(v['canonicalUrl'])
            categories.append(v['categories'][0])
            verified.append(v['verified'])
            stats.append(v['stats']['tipCount'])
            likes.append(v['likes']['count'])
            rating.append(v.get('rating', 'NaN'))
            photos.append(v['photos']['count'])
            tips.append(v['tips']['count'])
            shortUrl.append(v['shortUrl'])
            timeZone.append(v['timeZone'])
            listed.append(v['listed']['count'])
            attributes.append(v['attributes']['groups'])

    # Create final DataFrame
    dtdf = pd.DataFrame(data=[unique_id, 
                            name, 
                            phone,
                            twitter, 
                            city,
                            state, 
                            canonicalUrl,
                            categories, 
                            verified,
                            stats, 
                            likes,  
                            rating,
                            photos, 
                            tips, 
                            shortUrl,
                            timeZone,  
                            listed, 
                            attributes])

    # Transpose dataframe to usable format (i.e. flip row and columns)
    final_dt_df = dtdf.T
    
    # Name columns in final dataframe
    final_dt_df.columns = ['unique_id',
                        'name', 
                        'phone',
                        'twitter',
                        'city',
                        'state',
                        'url',
                        'categories',
                        'verified',
                        'stats',
                        'likes',
                        'rating',
                        'photos',
                        'tips',
                        'short_url',
                        'time_zone',
                        'listed',
                        'attributes']
    
    return final_dt_df

final_dt_df = create_df(details_lst)

# Filter for just the restaurants in Boulder. 

# final_df = final_dt_df[final_dt_df['city']=='Boulder']
final_df = final_dt_df[final_dt_df['city']=='Atlanta']


# Get remaining restaurants. On the "Personal Tier" on Foursquare, it will not let you run more than 500 Premium calls per day, 
# which is what is required to get detailed information per restaurant. For Boulder, where there are 615 restaurants, this limitation will only 
# allow access for 500 restaurants. To get around this issue, the long-term solution is to upgrade to a "Startup Account", which requires 
# a monthly subcription fee of about $600 per month. The short-term solution is to delete the app and access a new Client ID and Secret key to run the function 
# "get_remaining_restaurants". The new Client ID and Secret key resets the limit of premium calls, and this allows access to the remaining 115 restaurants in Boulder.  

# Get remaining restaurants taking the original unique ids and checking which ones didn't show up in the dataframe. Use the new list of remaining id's to 
# run the "get_all_restaurants_details()" and "create_df()" functions. 

def get_remaining_restaurants(first_ids):
    remaining_ids = []
    
    for i in first_ids:
        if i not in list(df['unique_id']):
            remaining_ids.append(i)
    
    return remaining_ids

# Check restaurant counts in dataframes.

def get_restaurant_counts(df1, df2):
    print("There are {} restaurants in df.".format(len(df), df))
    print("There are {} restaurants in df2.".format(len(df2), df2))
    print("There are a total of {} restaurants.".format(len(df)+len(df2)))

# Concatenate the two created dataframes to produce one final dataframe.

def concatenate_to_final_df(df1, df2): 
    final_df = pd.concat([df,df2])
    return final_df

# Save final dataframe as csv. Ensure your name_csv is in quotes and saved as csv (i.e. "choosie.csv").

def save_df_as_csv(final_df, name_csv):
    final_df.to_csv(name_csv, encoding='utf-8', index=False)


# Next steps
# py scrpt on DF to NMF DF aka clean up categories and attributes. (also look at how to transform numerical to categorical data)
# from NMF df to latent topics and EDA and topic modelling

