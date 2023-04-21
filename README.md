# Housing-Analytics

## Goal
To create a comprehensive back-end structure that aggregates house listing data and other relevant information, this will allow for dashboarding, analytics, and forecasting of the housing market to comprehend the nature of what impacts a housing price in a granular fashion.
<br>
<br>

## Data Sources
1. House Listing Data:
    - Redfin API -- [click here](https://github.com/reteps/redfin) for a look at the github explaining how to use this in python.
    - Seems to incorporate up-to-date listing information, housing details, and even local school info & reviews.
2. Crime Data 
    - NIBRS (but we need to ensure we can access a live connection).
    - How does crime and what types of crime are contributing to the impact on house listings?
3. Macroeconomic Indicators (interest rates are huge here)
    - Rather simply accessed through the [St. Louis Fed](https://fred.stlouisfed.org/docs/api/fred/)
    - Things like interest rates and the job market obviously have an effect on the housing market, but to how much of an extent? And are there certain industries that have differing effects?
4. News
    - Using the [GDELT Project](https://www.gdeltproject.org/data.html).
    - How does wordly instability impact peoples' decisions to make a financial decision? Does local news or politics have any impact on the local housing market?
5. Public/Commercial Buildings
    - Ideally incorporating something like Google maps to identify stores, schools, gyms, etc...
6. Climate
    - Would be interesting to gather statistics on temperatures and weather events overtime for each location.

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
    - What is the static look at the housing market?
    - Can we notice any trends geographically?
- Short/Medium-term: 
    - How have trends changed recently?
    - What are fair prices to pay for a given location?
- Long-term: 
    - When is the best time to buy an apartment?
    - What prices/availability can we expect down the line?

<br>
<br>

## What do we want our output to be?

Firstly, a fundamentals analysis: what is at play in the supply and demand of housing? 

Options ahead:
- Dashboard/search tool for house listings that fit someones needs
- Forecasting the housing market
- Research Paper (if we want to swing something new and interesting, i.e. "There are clearly some problems in the banking system because this prices should be *X* but they are *Y*...yada yada" -- watch *The Big Short*).

## Next Steps:

- Data Gathering (APIs)
- Data Cleansing
- ER Diagram of our database
  - Determine where we want to hold this database if it gets large (maybe Google Cloud? Would be interesting to see how to navigate files locally from the cloud).
- Data Processing
  - Organizing our tables to how we see fit, filtering out unimportant info, adjusting variables as we see fit.
- EDA
  - Visualize the data to understand basic insights of the housing market - heatmaps, correlation matrices, linear regressions, etc...

