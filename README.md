# Surfs Up

## Project Overview

### Purpose
The purpose of this project was to obtain and summarize temperature data for the months of June and December in Oahu, Hawaii. This information was needed to assess the viability of a surf and ice cream shop in the area. To accomplish this, SQLAlchemy was used to filter data from hawaii.sqlite to isolate the desired data into a pandas dataframe in Jupyter Notebook. Once the data was in Jupyter Notebook, the pandas library was used to calculate and display summary statistics for temperatures in Oahu in June and December.

### Resources
- Data Sources: hawaii.sqlite
- Tools: Python3.7, Pandas, SQLAlchemy, anaconda4.13, Jupyter Notebook, VSCode, SQLite

## Results
The following is a list of major points revealed by the analysis.

- Temperatures do not vary much in Oahu, as evidenced by a standard deviation of only 3.26 degrees in June and 3.75 in December.
- It never gets unbearably hot or cold in Oahu, with a maximum temperature of only 85°F in June and a minimum temperature of 56°F in December. 
- Both months have sample sizes large enough to generate reliable summary statistics. However, the summary statistics for June may be slightly more reliable than for December, given that there are 1,700 measurements for June and 1,517 for December

## Summary

### Surfing
The surfing aspect of the business is viable year round. According to manymoremaps.com, a wetsuit is only typically necessary if the water is below 65°F. With a mean temperature of 71°F in December and only 25% of temperatures below 69°F, the water should be plenty warm. We can carry wetsuits for rental as well on the off chance someone wants to have one on those colder days.

### Ice Cream
The ice cream aspect of the business is also viable year round. Ice cream sales will obviously do better in the Summer, as evidenced by a mean June temperature of 75°F and only 25% of temperatures below 73°F. However, the mean temperature in December (71°F) is only about 4 degrees cooler than June. Additionally, I mentioned the low standard deviations in the results section, meaning that there will not be many cold days where ice cream sales will suffer. All of this is to say that I do not believe there will be a drastic difference in ice cream sales between Summer and Winter.

### Additional Queries

#### Precipitation
Precipitation data would be very valuable given that people are more likely to both surf and buy ice cream on a sunny day versus a cloudy/rainy day.

#### Hottest Days
Another interesting query with possibly valuable results would be to examine what days are usually the hottest of the year. If we examined the top 10 temperatures for each year and compared the dates, we could try to identify a trend. If we found that the hottest days were consistently during a certain part of the summer, we could plan some type of promotion for those days since, as I mentioned in the summary section, hotter days should lead to more business. Something along the lines of buy one ice cream cone get one free, or rent two surfboards for an hour get a third one for free, etc. This promotion could drive more business to us and away from our competitors on those high volume days.