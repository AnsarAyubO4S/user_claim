import requests
import concurrent.futures

#{"schemeCode":"1953113d","rewardId":"92E63744"}

data = {
       "claimCode":"80518360"
       }

d = [0] * 100

def get_wiki_page_existence(payload, timeout=10):
    headers = {
        "Content-Type": "application/json", 
	"authToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiUEhBTlRPTSIsImNvbnRleHQiOiJEQVNIQk9BUkQiLCJjb21wYW55Q29kZSI6InRlc3QtZGVtby1jbyJ9.iXKDj3a_I2ul5i7g8iolp5dWa6jYxfa99rWwAUQFSxo" 
   }
    url = "https://dev.o4s.io/evato/refund-claim"    
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.json())
    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"	
    return response.status_code


with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    success = 0
    failures= 0
    for url in d:
        futures.append(executor.submit(get_wiki_page_existence, data))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
        if(future.result()==200):
            success+=1
        else:
            failures+=1   
    print(success,failures)  

