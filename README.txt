Easy way to web scrapping without API service
In this project I will scrape the data of Worldwide Box Office from mojo website for whay year I choose to  

1.Save url content to html file for future parsing
2.Parse html file with help of requests-html module like this:
    find('.class_name') by inspecting the website 
    find('tr') to looking for rows
    find('th') to looking for columns
3.Store the data to csv file by using pandas module 

 -> python -i .\scrape.py *YEAR* (not necessarily)