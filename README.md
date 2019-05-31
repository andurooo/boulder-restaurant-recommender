********************
# Exploring Boulder Restaurants
********************
What are the dining options available in Boulder? 
What are the categories and features to choose from in those dining options?

## Table of Contents
1. [Background](#Background)
2. [Objective](#Objective)
3. [Data](#Data)
4. [Challenges](#Challenges)
5. [Findings](#Findings)
6. [Next Steps](#Next-Steps)

# Background 
Choosie's mission is to take the stress out of dining out. They aspire to achieve that by providing personalized recommendations, both for you and your group. The first target market is Boulder, CO. 

<p align="center">
<img src='choosie_food.png'>
  
## Question: 
What are the dining options available in Boulder? What are the categories and features to selecting from when choosing a restaurant?

# Objective
  * Gather data on Boulder restaurants
  * Perform exploratory data analysis (EDA)
      * Identify categorical, numerical and textual data

# Data
Foursquare Places API: https://developer.foursquare.com/places-api

Foursquare API provides data centered around location. Their API is very developer-friendly; many corporations use the Foursquare API for their apps today. Also, the terms and conditions are less strict compared to alternative API's, especially for commercial use.

## 3 GET requests
  *categories (147 total)
  *explore (uses keyword to return recommendations)
  *details (single query using venue unique id)
  
Through the categories GET request, I gained insight about all of the categories used in the Foursquare app. It is divided up into main categories that serve as umbrella categories. And below those main categories, there are two levels of subcategories. For example, the main category I used for my GET request was 'Food'. And under 'Food' were subcategories, such as "Indian Restaurants", and "Mexican Restaurants", and under those subcategories were sub-level-2 categories, such as "Dosa", "South Indian", "North Indian", and "Taco Places" and "Burrito Places", respectively. In the dataset I used, under "Food", there were 90 subcategories and 56 sub-level-2 categories, for a total of 147 categories.

The explore GET request takes a keyword as an input and compares it against restaurants' associated categories and tips. The output is a specified number of venues, with a limit of 100. 

Lastly, the details GET request takes the unique id of a venue and runs a single query that returns all of the specific details for that single venue. Because it is a single query, I attained all of the categories from the categories GET request, ran a loop to get all of the restaurants associated with each category to get around the limit of 100 on explore. Then, I created a set of all of the unique id's from the explore recommendations list and created another loop to run single queries using all of the unique id's gathered from the first two GET requests. The resulting dataset was a dataframe with a shape of (622, 20). 







