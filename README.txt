This project is about web scapping with and without an API service.
The idea behind it is to store into a csv file the Worldwide BoxOffice of an year you choose to,
by scrapping from two different sources like this:
- from https://www.boxofficemojo.com/ I scraped the entire BoxOffice they give us and save all the data to html file
- from https://www.themoviedb.org/ I searched by the name and year of each BoxOffice movie,
to add some extra details(release date, original language, etc)

WebScrapping without API:
1.Save url content to html file for future parsing
2.Scrape html file with help of requests-html module like this:
    find('.class_name') by inspecting the website 
    find('tr') to looking for rows
    find('th') to looking for columns
3.Store the data to future works

WebScrapping with API:
1. Use api_token/api_key and a specific format of headers to connect to API service
2. Search for movie by name
3. Verify the results and select from a list of movies which is from the year of our BoxOffice
4. Select new data to add to BoxOffice

Finally, save all the data to csv file using pandas module

 -> python -i .\boxoffice.py *YEAR* 