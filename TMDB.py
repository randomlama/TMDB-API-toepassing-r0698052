import urllib.parse
import requests 

# enter your API-Key here
auth = "INSET-API-KEY-HERE"
# the base URL for api requests
urlbase = "https://api.themoviedb.org/3/search/movie?"


# while loop to allow for user input and handeling of request
while  True:
    query = input("Enter your query: ")
    #allows user to exit the program
    if query == "q" or query == "quit":
        break
    #auth v3
    url = urlbase +urllib.parse.urlencode({"api_key": "%s" %auth, "query": query})
    #auth v4
    #url = urlbase +urllib.parse.urlencode({"Authentication ": "Bearer %s" %auth, "query": query})
    json_data = requests.get(url).json()
    print("URL: " + (url))
    #checks if there is an error code
    if "status_code" not in json_data:
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
    else:
        #prints error message when applicable 
        json_status = json_data["status_message"]
        print ("error: " + json_status)