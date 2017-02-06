#short-jokes-dataset

This repository contains all the python scripts used to build Short Jokes Dataset. The dataset contains 231,657 short jokes scraped from various websites. 

All the web scraper scripts are present in the `/scripts/scrapers/` folder. These scripts are written for specific websites (website link mentioned in the header of each file) and they generate csv files of jokes in `/data/` folder with the fixed format: `ID, Joke`.  

Jokes from subreddits `/r/jokes` and `/r/cleanjokes` are extracted using `scripts/scrapers/subredditarchive.py`. This `subredditarchive.py` generates a json file for each post in a separate folder. Json dumps for both the subreddits can be accessed from [here](https://www.mediafire.com/folder/7jj7iemb69shh/Reddit_Dumps)  (Uncompressed 2.3GB). Jokes from all the json files are extracted and written to a csv file using `scripts/json_to_csv.py`. 

`scripts/merge_csvs.py` removes the duplicates from all the csv files and merges the jokes into a single csv to get the final dataset `shortjokes.csv`. 

## Contributions
* If you are aware of any resource (preferably large) of good clean jokes, feel free to suggest or send a pull request with scraper script and csv file in the above format.
* Any other positive suggestions for the dataset are welcome. 
