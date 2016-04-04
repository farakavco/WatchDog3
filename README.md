# Author: Amin Etesamian
# Title: Document
# Date: 16/01/1395



Introuction:
A watchdog designed to extract all urls from a website and request them concurrently to check their health status. There is configuration file included in the project
which enables you to set the sites and the number of threads used for doing the request operation.

Usage:
Adjust the configuration.py to meet your needs and simply run the __init__.py file. A list of messages is created containing the urls which didn't response with 200
request and also any occured exception in the operation of requesting the url.
 There is a messenger.py file which by default may be used to inform the person in charge of server monitoring about the server using the list of messages created by
the crawler module.


