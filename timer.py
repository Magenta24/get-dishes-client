import requests
import datetime
import statistics as stat

SERVICE_1_ENDPOINT = "http://localhost:5000"
SERVICE_2_ENDPOINT = "http://localhost:8080/api"
SERVICE_3_ENDPOINT = "https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/a02d1a2d-2e39-42af-871e-3e8007f2e5e3"

NUM_TRIALS = 50
API_KEY = "zYAH4XzJ_X6U-RetmZw-Y0-1L2a8uG_qrE5MTKzM7-SM"


time_tracker = {
    "SERVICE_1_ENDPOINT": [],
    "SERVICE_2_ENDPOINT": [],
    "SERVICE_3_ENDPOINT": []
}


for i in range(NUM_TRIALS):
    time_start = datetime.datetime.now()
    recipes = requests.get(SERVICE_2_ENDPOINT + f'/all_dishes')
    time_end = datetime.datetime.now()
    time_tracker["SERVICE_2_ENDPOINT"].append(time_end - time_start)

for i in range(NUM_TRIALS):
    time_start = datetime.datetime.now()
    recipes = requests.get(SERVICE_1_ENDPOINT + f'/all_dishes')
    time_end = datetime.datetime.now()
    time_tracker["SERVICE_1_ENDPOINT"].append(time_end - time_start)

for i in range(NUM_TRIALS):
    time_start = datetime.datetime.now()

    recipes = requests.get(SERVICE_3_ENDPOINT + "/v1/synthesize",
        auth = ('apikey', API_KEY), params = {
            "accept": "audio/mp3",
            "text": "Hello World",
            "voice": "en-US_AllisonV3Voice"
        })
    time_end = datetime.datetime.now()
    time_tracker["SERVICE_3_ENDPOINT"].append(time_end - time_start)

print("####################################################################")
print("#                        SERVICE_1_ENDPOINT                        #")
print("####################################################################")
print("Mean(s): ", stat.mean([x.total_seconds() for x in time_tracker["SERVICE_1_ENDPOINT"]]))
print("Standard Deviation:", stat.stdev([x.total_seconds() for x in time_tracker["SERVICE_1_ENDPOINT"]]))
print("\n\n")

print("####################################################################")
print("#                        SERVICE_2_ENDPOINT                        #")
print("####################################################################")
print("Mean(s): ", stat.mean([x.total_seconds() for x in time_tracker["SERVICE_2_ENDPOINT"]]))
print("Standard Deviation:", stat.stdev([x.total_seconds() for x in time_tracker["SERVICE_2_ENDPOINT"]]))
print("\n\n")


print("####################################################################")
print("#                        SERVICE_3_ENDPOINT                        #")
print("####################################################################")
print("Mean(s): ", stat.mean([x.total_seconds() for x in time_tracker["SERVICE_3_ENDPOINT"]]))
print("Standard Deviation:", stat.stdev([x.total_seconds() for x in time_tracker["SERVICE_3_ENDPOINT"]]))
print("\n\n")

# print("SERVICE_2_ENDPOINT:", stat.mean([x.total_seconds() for x in time_tracker["SERVICE_2_ENDPOINT"]]))
# print("SERVICE_3_ENDPOINT:", stat.mean([x.total_seconds() for x in time_tracker["SERVICE_3_ENDPOINT"]]))