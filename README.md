
# Custom Metadata Scraper

This repository contains the "Custom Metadata Scraper" add-on for DocumentCloud. The user can check which data types they would like to scrape and the add-on will fetch that specific data and compile the results into a csv that can then be downloaded  

## Files

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

### main.py

This is the file to edit to implement your Add-On specific functionality.  You
should define a class which inherits from `AddOn` from `addon.py`.  Then you
can instantiate a new instance and call the main method, which is the entry
point for your Add-On logic.  You may access the data parsed by `AddOn` as well
as using the helper methods defined there.  The `HelloWorld` example Add-On
demonstrates using many of these features.

If you need to add more files, remember to instantiate the main Add-On class
from a file called `main.py` - that is what the GitHub action will call with
the Add-On parameters upon being dispatched.

### config.yaml

This is a YAML file which defines the data for the add-on It uses the [JSON Schema](https://json-schema.org/) format, but allows you to
use YAML for convenience.  

### requirements.txt

This is a standard `pip` `requirements.txt` file. 

### .github/workflows/run-addon.yml

This is the GitHub Actions configuration file for running the add-on.  It
references a reusable workflow from the
`MuckRock/documentcloud-addon-workflows` repository.  

### .github/workflows/update-config.yml

This is the GitHub Actions configuration file for updating the configuration
file.  It references a reusable workflow from the
`MuckRock/documentcloud-addon-workflows` repository.  This workflow sends a
`POST` request to DocumentCloud whenever a new `config.yaml` file is pushed to
the repository. 

### LICENSE

The license this code is provided under, the 3-Clause BSD License

