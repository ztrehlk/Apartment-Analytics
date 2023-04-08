# Apartment-Analytics

## Goal
To create a comprehensive back-end structure that aggregates apartment listing data and other relevant information, in order to provide an easy-to-use platform for individuals to find and choose apartments based on their specific criteria.
<br>
<br>

## Data Sources
1. Apartment Listing Data: 
    - [Apartments.com API](https://api.apartments.com/v1/)
    - [Hotpads](https://filenet.hotpads.com/+guides/Rental+Listings+Real-Time+Feed+Guide.pdf)
2. Crime Data 
    - NIBRS (but we need to ensure we can access a live connection).
3. Reviews
    - Yelp/Google Reviews API
4. Miscellaneous 
    - [Google Maps API](https://developers.google.com/maps/documentation/places/web-service/overview) – need to check if we can easily access lists of, say, schools. Does have a free tier but may have costs after abundant usage.

<br>
<br>

## Methods
Structuring our database:
- Ensure APIs are working and sustainable.
- Pipeline to a live database – best if using a cloud server for this multi-person project; look into options.
- Cleaning & Organizing the data – dealing with a likely complicated set of json datafiles.
- Combining Tables – finding and/or establishing primary and foreign keys in our dataset to be able to create an ER diagram for documentation and replicability.

Drawing Insights:
- Immediate: 
    - What apartments available now match my criteria?
    - What are the reviews of the landlord/leasing company?
      - Highlighting topics of concern with word bucket techniques (maybe NLP down the line).
- Short/Medium-term: 
    - How have trends changed recently?
    - What are fair prices to pay for a given location?
- Long-term: 
    - When is the best time to buy an apartment?
    - What prices/availability can we expect down the line?


Pulling in all the info of apartments hopefully from an API
I think it will be a best practice to structure our addresses as 5 different columns based on my experience with google maps
There is the possibility of using the .png files of images to quantify stuff. I think this is really tough to do, but would also be quite fun. That way we could find factores like, plenty of counter space, new looking apartment, tons of windows
Recommendation systems aren’t even so much ML but we can always add ML projects with the data if we want later (forecasting pricing or availability)

Alex Python Web Scrape Apartments Data\
Cyrus Tidy data up in R\
I think I’ll explore using a google maps API and reticulate for now

<br>
<br>

## What do we want our output to be?

Maybe an app or website?\
I am pro making a [shiny app](https://shiny.rstudio.com/)\
Including the following features
- Walk Score
- Bike Score
- Bars score
- Other scores
- Crime of area
- Distance to work--we can factore bike/walking/driving duration with gmaps api
- Top features next to a location like The Davis, your mom, central park etc. 

Next Steps:

Come up with a Git repo name\
Decide if we should have the Git repo public or private. We can change this as the project progresses but they make you put in your PASSWORD for this also🥵\
Sketch idea for what we want our output to be\
Discuss how our workflow for this will go--what will be done in R and Python
