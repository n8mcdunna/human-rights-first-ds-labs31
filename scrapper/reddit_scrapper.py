import praw
from prawcore import PrawcoreException
import dotenv


class RedditScrapper(praw.Reddit):
    
    def __init__(self, subreddit_name, dotenv_path):
        """ 
            RedditScrapper instance constructor. 
             
            Instance of the Reddit App can be created at 'https://www.reddit.com/prefs/apps' to obtain 
            client_id, client_secret, user_agent credentials. In order for RedditScrapper to utilize 
			Reddit API credentials fot Reddit App need to be added to .env file as a variables of format:
			   praw_user_agent = user agent description
			   praw_client_secret = client secret key
			   praw_client_id = client app id 
        """
        #Load Reddit app credentials as environment variables
        dotenv.load_dotenv(dotenv_path, override=True)
        
        #Instanciate superclass
        super().__init__(check_for_async = False)
        
        #Assign subreddit name to an instance variable
        self.subreddit_name = subreddit_name
        
        
    def connection_test(self):
        """Checks for valid connection to the Reddit API. Returns `True` or `False` according to connection success.
           Although calling connection_test is optinal, it is recommended to use this method before making queries 
           in order to prevent Runtime errors."""
        
        try:
            for post in self.subreddit('all').search('the'):
                return True
        
        except PrawcoreException as error:
            print(error)
            return False
        
    
    def fetch(self, limit=None, body = True, time_filter='all'):
        
		"""Fetches posts from `subreddit` that are dated within a range of `time_filter`. By default fetch returns `array` 
		   of all posts from indicated subreddit. 

			`body` - Boolean indicating whether to include (if exists) the body of the Reddit post in the output.
			If body=False, then only post title will be included in the output. (default: True).

			`time_filter` – Can be one of: all, day, hour, month, week, year (default: all).

			`limit` - integer number of search results to return. If limit=None, all posts within a range of `time_filter`
			are returned. (default: None).
        """
        output = []
        subr = self.subreddit(self.subreddit_name)
        posts = subr.top(time_filter=time_filter)
        posts.limit = limit
        
        try:
            for post in posts:
                if (body):
                    if (post.selftext):
                        output.append(f'{post.title} {post.selftext}')
                    else:
                        output.append(post.title)
                else:
                    output.append(post.title)
            return output
        
        except PrawcoreException as error:
            print(error)
            return []           

