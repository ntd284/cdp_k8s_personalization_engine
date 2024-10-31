from personalization_router import api_personalization

# Run the FastAPI api_personalization
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(api_personalization, host="0.0.0.0", port=8000)



# import requests
# import time

# def main():
#     api_url = "http://zenquotes.io/api/quotes"
#     while True:
#         try:
#             response = requests.get(api_url)
#             if response.status_code == 200:
#                 data = response.json()
#                 print(data[0])
#             else:
#                 print(f"Failed to fetch data. Status code: {response.status_code}")
#         except requests.exceptions.RequestException as e:
#             print(f"Error: {e}")
#         time.sleep(2)

# if __name__ == "__main__":
#     main()

