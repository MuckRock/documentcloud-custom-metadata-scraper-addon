
# DocumentCloud Add-On - Custom Metadata Scraper

This repository contains a custom metadata scraper add-on for DocumentCloud. The user can check which data types they would like to scrape,and the addon will fetch that specific data and compile the result/s into a csv  

### testing

The data passed into the add-on is a dictionary of variable length (depends on the data selected) with the keys being the different document data types and their values being booleans. Currently, the following document data types are supported:

ID  <br />
Title <br />
Privacy Level <br />
Asset URL <br />
Contributor <br />
Created At Date <br />
Description <br />
Full Text URL <br />
PDF URL  <br />
Page Count <br />
Tags <br />
Key Value Pairs <br />

Example invocations:
```
python3 main.py --documents 123 --username "..." --password "..." --data '{"ID": true, "TITLE": true, "PRIVACYLEVEL": true, "ASSETURL": true, "CONTRIBUTOR": true, "CREATEDATDATE": true,  "DESCRIPTION": false, "FULLTEXTURL": true, "PDFURL": false, "PAGECOUNT": true, "TAGS": true, "KEYVALUEPAIRS": false}' 
```
```
python3 main.py --documents 123 --username "..." --password "..." --data '{"ID": true, "TITLE": true, "PRIVACYLEVEL": true}' 
```
```
python3 main.py --documents 123 --username "..." --password "..." --data '{"CREATEDATDATE": true,  "DESCRIPTION": false, "FULLTEXTURL": true' 
```