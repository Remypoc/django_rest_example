# Django rest example
Example of file upload using django rest

## Install
pip install django

pip install djangorestframework

pip install coreapi

## Few examples

You can use django api or admin panel for testing. Here are some
request to POST and GET snippet with files like videos or images.

#### Get list of possible actions
- coreapi get http://127.0.0.1:8000/schema/
 
#### List snippets
- coreapi action snippets list

#### Delete a snippet
- coreapi action snippets delete --param id=1

#### Add snippet
- coreapi action snippets create --param title="Example5" --file file="path/to/file.*"