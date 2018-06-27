# filter_map_reduce

## Description

This project implelemntation was made basd on Python, Clojure, and Swift.

Python served as the link to Twitter's API.  The Python Script called "getTweets.py" basically creates a file with tweets made based on a location given.

This implementation was based on :

https://github.com/ideoforms/python-twitter-examples

After building the Tweet Database, Clojure serves as the filtering mechanism. "findTrend.clj" counts each ocurrance of all of the words that exist on the database (CSV file). Based on this, it returns the most repeated word in another TXT file (trend.txt).

Finally, to demonstrate in a GUI the output, Swift was used. To demo the trend displayed on an iPhone, Swift's script reads the (trend.txt) file and Shows it on screen.


## Usage

To run the elemental scripts:

    . getTrends.sh
    
    

