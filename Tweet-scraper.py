import pandas as pd
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter



scraper = sntwitter .TwitterSearchScraper('write any keyword or sentence that you want to scrpe')
tweets = []
for i,tweet in enumerate(scraper.get_items()):
   
    data = [ tweet.content]
    tweets.append(data)
    if i>3000:
        break
        

tweet_df = pd.DataFrame(tweets, columns=['content'])

tweet_df.to_csv('data1.csv')