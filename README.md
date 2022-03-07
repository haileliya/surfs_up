# surfs_up Analysis
Overview of the analysis: Explain the purpose of this analysis.

The purpose of this analysis was to use SQLalchemy to provide more weather related information trends before the opening of a surf shop. The customer wanted temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

Results: Provide a bulleted list with three major points from the two analysis deliverables. Use images as support where needed.

1. The first result extracted temperature data from the month of June by creating a session query for the engine we used. This extraction brought the data into a list which was then converted to a dataframe. Summary statistics were easily found once the dataframe contained the temperature data from June. In the month of June, the average temperature is 74.9 degrees F, while the lowest is 64. 

![image](https://user-images.githubusercontent.com/96396696/156978962-6b43b015-9166-4145-94c7-82c3ed060681.png)


2. The second results is similar in process to the first, except I extracted data for the month of December by refractoring the code to have the filter == 12. I ran summary statistics and found the average temperature during December in Oahu to be 71 degrees F, whiile the min was 56 and the max 83.

![image](https://user-images.githubusercontent.com/96396696/156978984-248da3fa-e95a-4f1e-8e97-f61e522f1764.png)

3. By conducting these two summary analysis, one interesting thing I found was that or the data, the temperature in the quintiles were very close. For instance the 75th quintile, the temperature was 77 and 74 for June and December, respectively. 

Summary: Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.

Overall, from this analysis we can gather that opening a ice cream and surf shop in Oahu would be adventageous even in an unconventional month like December. The temperature data shows that the average temperature for these two months were not too different.

Additionally, I think that it would be good to do an analysis of the precepitation in these two months to understand the wether better. It would also be smart to know the description of the weather to see iif it is mostly cloudy or windy during these two months, which I believe would highly affect sales of the shop.
