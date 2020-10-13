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

    
    resultcnt = 0
    for r in (json_data["results"]):
        #filters out entries with a vote average of 0 
        if r["vote_average"] > 0:
            print("=============================================")
            print ("title: \"" + r["title"] + "\"")
            print ("release date: " + r["release_date"])
            print ("average rating: " + str(r["vote_average"]) )
            resultcnt += 1
    print("=============================================")
    print("---------------------------------------------")        
    print (str(resultcnt) + " results shown.")
    print("---------------------------------------------")
