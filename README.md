# S&P Companies
Fetches the companies that comprises the s&p 500 based on the wiki page https://en.wikipedia.org/wiki/List_of_S%26P_500_companies including historical lists.

## Usage
```
from datetime import date
from snp_companies import SNPListing

listing = SNPListing()
print(listing[date.today()])
print(listing['2021-11-28'])
print(listing['2000-11-28'])
```