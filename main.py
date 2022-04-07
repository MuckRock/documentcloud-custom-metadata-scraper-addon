"""
This is a metadata scraping plugin for DocumentCloud.

It demonstrates how to write a add-on which can be activated from the
DocumentCloud add-on system and run using Github Actions.  It receives data
from DocumentCloud via the request dispatch and writes data back to
DocumentCloud using the standard API
"""
import sys
from documentcloud.addon import AddOn
import csv


class CustomMetaData(AddOn):
    """An metadata scraping Add-On for DocumentCloud."""

    def main(self):
        """The main add-on functionality goes here."""
        #fetch your add-on specific data

        #get boolean array
        values = self.data.get("choices")

        #make sure the array is of the right size 
        if (len(values) < 12):
            sys.exit('ERROR: Not enough arguments, every document data type should have an argument')
        elif (len(values) > 12):
            sys.exit('ERROR: Too many arguments')

        #make sure only 1s and 0s are being inputeted
        for value in values:
            if value == '0' or value == '1':
                continue
            else:
                sys.exit('ERROR: Please only enter zeros and ones into the list')

        #print(values)
  
        self.set_message("Beginning custom metadata scraping!")

        # preset header + metadata list
        header = ['id', 'title', 'privacy level', 'asset-url', 
        'contributor', 'created at date', 'description' ,'full text url', 'pdf url',
        'page count', 'Tags', 'Key Value Pairs']

        #delete values of 0 from the header because the user does not want them 
        Newheader = []
        for head in header:
            if values[header.index(head)] == '1':
                Newheader.append(head)

        #print(Newheader)


        metadata_list = [] # list of lists containing metadata for each document

        #takes the document object and an empty array as input, and places the document metadata into the array
        def setData(doc, doc_metadata):

            #document description break fix
            try:
                description = doc.description
            except AttributeError:
                 description = ""
            
            doc_metadata = [doc.id, doc.title, doc.access, doc.asset_url,
            doc.contributor, doc.created_at, description, doc.full_text_url,
            doc.pdf_url, doc.page_count]

            #separate key values and tags into two separate arrays
            keyvalues = doc.data
            tags = ""

            #are there any tags?
            try:
                tags = keyvalues['_tag']
                del keyvalues['_tag']
            except KeyError:
                tags = ""
            
            doc_metadata.append(tags)
            doc_metadata.append(keyvalues)

            return doc_metadata

        # retrieve information from each document.
        description = "NO DESCRIPTION PRESENT" #for the edge case with the description not existing
        if self.documents:
            length = len(self.documents)
            for i, doc_id in enumerate(self.documents):
                self.set_progress(100 * i // length)
                doc = self.client.documents.get(doc_id)

                #set the metadata
                metadata_list.append(setData(doc,[]))
        elif self.query:
            documents = self.client.documents.search(self.query)
            length = len(documents)
            for i, doc in enumerate(documents):
                self.set_progress(100 * i // length)
                
                #set the metadata
                metadata_list.append(setData(doc,[]))

        #go through the accumulated data and delete the data you do not want 
        Newdatalist = [[]]
        for data in metadata_list[0]:
            if values[metadata_list[0].index(data)] == '1':
                Newdatalist[0].append(data)

        #print(Newdatalist)

        # the id of the first document + how many more documents will be the name of the file
        try:
            firstTitle = metadata_list[0][1]
        except IndexError:
            firstTitle = ""
            length = 1

        with open("metadata_for-"+str(firstTitle)+"-_+"+str(length-1)+".csv", "w+") as file_:
            writer = csv.writer(file_)

            #FORMAT HEADER
            writer.writerow(Newheader)

            for row in Newdatalist:
                #FORMAT THE DATA 
                writer.writerow(row)
            
            self.upload_file(file_)

        self.set_message("Custom metadata scraping end!")


if __name__ == "__main__":
    CustomMetaData().main()
