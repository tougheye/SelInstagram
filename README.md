# SelInstagram
I created an Instagram bot on Selenium that would go to a target IG page and automatically follow the followers of the page. 
It is a great way to build your own business followers from a similar business's public IG page.
I used the official page of the great Bass angler Roland Martin's official page to follow his fans. You can choose your own targets

The main program is in InstaFollower class which has 3 main functions after the launch of the webdriver -
1. login - launches IG website and logs you in
2. find_followers - goes to the target IG page and clicks on the follower link. The code could scroll down the webpage 300 times in one session.
3. follow - clicks on the follow button. Takes 1 second pause in between each click.

The roland_martin_html.py page has the code for requests module to get the data from the target IG page and write them in a text file that it creates. 
