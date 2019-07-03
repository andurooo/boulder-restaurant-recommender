********************
# NMF Clustering for Restaurant
********************

## Table of Contents
1. [Background](#Background)
2. [Question](#Question)
3. [Data](#Data)
4. [Approach](#Approach)
5. [Findings](#Findings)
6. [Next Steps](#Next-Steps)

# Background 
Choosie's mission is to take the stress out of dining out. They aspire to achieve that by providing personalized recommendations, both for you and your group. The first target market is Boulder, CO. 

For Capstone 2, the focus was on identifying clusters of restaurant venues using unsupervising learning, specifically non-negative matrix factorization (NMF).

<p align="center">
<img src='img/choosie.png'>
  
# Question: 
Using NMF, what unexpected clusters can we find amongst Boulder restaurants that we can use to make recommendations?

# Data
Foursquare Places API: 
[ source](https://developer.foursquare.com/places-api)
</p>

There are 615 Boulder restaurants in the dataset. While there are 147 possible categories a restaurant on Foursquare can be labeled as, only 73 of those categories are represented in Boulder restaurants. Also, each restaurant can be described by the attributes it has. In Boulder restaurants, 23 attributes are represented. 

Summary:
  * **96 total features** 
  * 73 categories (i.e. Mediterranean Restaurants, Cafes, etc)
  * 23 attributes (i.e. Outdoor seating, Happy Hour, Live Music, Wheelchair accessible, Price Tier 1-4, etc)
  * did not use numerical: likes, rating, photos, tips, listed

# Approach
  * Why did I choose NMF?
  * How did I choose the number of k's?
  
**Why NMF?**

Soft clustering. Because each of my restaurants can have multiple categories or features associated with them. 

**How did I choose my k?**

After running my algorithm, I calculated the **reconstruction error** at various points in k to find where there is the greatest dropoff. The goal is to have the reconstruction error minimized to a desired value. To help visualize this, here is an elbow plot:

<p align="center">
<img src="img/k_rec_error.png">

While there isn't a clear drop-off point in the error at point k, there is a noticeable change shift of the slop at **k = 10**. So I decided to use 10 as my number of k. 

# Findings

By features:

latent topic 1: cocktails, full bar, happy hour, beer, wine, reservations, american_restaurant, dinner, dessert, table_service

latent topic 2: 'price_tier_1', 'sandwich_place', 'food_truck', 'pizza_place',
       'fast_food_restaurant', 'café', 'coffee_shop', 'mexican_restaurant',
       'ice_cream_shop', 'deli_/_bodega'





# Next-Steps
1. Build on topic modelling concepts towards a collaborative recommender system
2. Create user-facing tool for recommender (i.e. Flash)
