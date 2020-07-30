# trackage

A command line application written in Python for tracking your packages.


## How to Use

You will need Python installed to run this application.

There are 4 available functions in this application:  
1. add - requires tracking number and shipping service  
ex: python trackage.py add -tn 12312312312312312312 -s usps  
2. delete - requires tracking number  
ex: python trackage.py delete -tn 12312312312312312312
3. track_all - no arguments  
ex: python trackage.py track_all  
4. track_one - requires tracking number and shipping service  
ex: python trackage.py track_one -tn 12312312312312312312 -s usps
