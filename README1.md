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
Using NMF, what unexpected clusters can we find amongst restaurants that we can use to make recommendations to the user? 

# Data
Foursquare Places API: 
[ source](https://developer.foursquare.com/places-api)
</p>

615 restaurants

96 total features 
73 categories (i.e. Mediterranean Restaurants, Cafes, etc)
23 attributes (i.e. Outdoor seating, Happy Hour, Live Music, Wheelchair accessible, Price Tier 1-4, etc)

did not use: likes, rating, photos, tips, listed

# Approach
  * Why did I choose NMF?
  * How did I choose the number of k's?
  
# Findings

### Overview:
147 categories, 483 restaurants, 20 features

### Categorical Data:
  * *Price Tier*
  * *Verified*
  * *Categories*
  * *Attributes*

<p align="center">
<img src="img/comparer.png">

### Numerical Data:
  * *Ratings*
  * *Likes*
  * *Tips Count*
  * *Listed*
  * *Photos Count*

<p align="center">
<img src="img/scattermatrix.png">

### Textual Data: 
  * *Descriptions*
  * *Tips*
  * *Categories*
  * *Attributes*
  

<p align="center" font='12'>
"Grab a seat on the patio if you've got kids--there's a park just beyond the fence!
happy hour: 3-7
Everything! Love carnitas!
The best tacos west of the Mississippi and Norte del Mexico"
</p>

### Image Data:
  * *Photos*

# Future Steps
1. Gather user data and perform EDA
2. Expand analysis on dataframe in preparation for feature selection & modeling (i.e. NLP, Sentiment Analysis, Computer Vision, Multiple Regression)
3. Create database/data pipeline before scaling (i.e. MongoDB, Spark, AWS)
4. Webscrape Boulder Dining website, if needed
