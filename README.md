# Surfs Up

<details><summary>Table of Contents</summary>
<p>

1. [Overview](https://github.com/catsdata/surfs_up#overview)
2. [Resources](https://github.com/catsdata/surfs_up#resources)
3. [Results](https://github.com/catsdata/surfs_up#results)
4. [Summary](https://github.com/catsdata/surfs_up#summary)

</p>
</details>

## Overview

A surf and ice cream shop has been planned for Oahu, Hawaii.  However, this concept didn't work out in the past due to weather patterns at its location.  To determine if Oahu is the right place to open the business and convince investors to help the start up, we need to analyze the weather.  We have all the weather data needed from 9 different stations, for several years, however to make sure this would be a year 'round venture, we are going to solely look at June and December data.  All of the weather data is already in a [SQLite Database](https://github.com/catsdata/surfs_up/blob/main/hawaii.sqlite) and we just need to access and analyze to present to the investors.  

## Resources

- Data Sources: 
    - [SQLite Database](https://github.com/catsdata/surfs_up/blob/main/hawaii.sqlite)
- Software:  
    - Jupyter Notebook 6.4.6
    - SQLAlchemy 1.4.27
    - Python 3.7.11 with dependencies: 
        - pandas 1.3.5
        - numpy 1.20.3
    
## Results

Code:  [Surfs Up Challenge](https://github.com/catsdata/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

We started by reflecting the SQLite database using SQLalchemy and Python and inspecting our table names.  We had station specific and measurement specific tables.  For this analysis, all the data we needed was contained in "measurement", which included the station ID, the date of the observation, the precipitation total of the day and the observed average temperature.  

Using SQLalchemy to extract the measurement tablem, we first pulled all June temperature observations.  Taking the temps, we added them to a new list to create a June Temp dataframe, and then ran statistics to summarize the years worth of data.  We repeated these steps for December.  Below are our Temp stats.

![June Temps](https://github.com/catsdata/surfs_up/blob/main/images/junestats.PNG)  ![December Temps](https://github.com/catsdata/surfs_up/blob/main/images/decstats.PNG)

- An immediate observation would be the data points for June being higher than December.  But from a previous research we know that several weather stations can be inconsistent in their data output.  Since we're looking at averages over several years, this shouldn't skew the data too much.
- June tends to be warmer than December with a minimum temp of 64, maximum of 85 and low standard deviation of 3.25 versus 56 min, 83 max and a higher stndardard deviation of 3.74.   
- June temps have an overall more pleasant range, however December is still somewhat ideal with an average of 71 degrees which is only 4 degrees less than June's average.  
- We can see additional detail in a previous observation of monthly averages on temps; a large majority of data sits in between 67 and 81 degrees - perfect t-shirt weather.

![Freq](https://github.com/catsdata/surfs_up/blob/main/images/freq.PNG)

Overall, Sales may be slower in December, but they wouldn't be non-existant based on the temps alone.  So we should also look at the precipitation as less customers will be surfing and eating ice cream if it's pouring rain.

Using the same process as we did for temps, we reran the data for average precipitation.  

![June Precip](https://github.com/catsdata/surfs_up/blob/main/images/juneprecip.PNG)    ![December Precip](https://github.com/catsdata/surfs_up/blob/main/images/decprecip.PNG)

- We see again a higher data count result for June than December which aligns with our station observations.
- June is still a winning month with lower average rain of 0.14 inches versus 0.22 inches in December.
- December again has a higher standard deviation on the averages as they did with the temps.  The precipitation is a little less predictable than June, but still within acceptable levels for a business.  


## Summary

June being a popular vacation time for families with school being out for the summer, we can expect to have greater sales.  Weather and temps do not appear to be a major factor for either month.  However, we may want to look further into the averages for other months and graph overall for the year to ensure it's a consistent increase/decrease based on the seasons.   

