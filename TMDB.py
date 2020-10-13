import urllib.parse
import requests 

# enter your API-Key here
auth = "INSERT API-KEY HERE"
# the base URL for api requests
urlbase = "https://api.themoviedb.org/3/search/movie?"

# while loop to allow for user input and handeling of request
while  True:
    query = input("Enter your query: ")
    #allows user to exit the program
    if query == "q" or query == "quit":
        break
    url = urlbase +urllib.parse.urlencode({"api_key":auth, "query": query})
    json_data = requests.get(url).json()
    print("URL: " + (url))
    print("=============================================")
    print ("Results: ")
    resultcnt = 0
    rating = 0.0
    for r in (json_data["results"]):
        if r["vote_average"] > 0:
            print (r["title"])
            rating = r["vote_average"]
            print ("average rating: " + str(rating) )
            resultcnt += 1
            print("=============================================")
    print (resultcnt)
    print("=============================================")
