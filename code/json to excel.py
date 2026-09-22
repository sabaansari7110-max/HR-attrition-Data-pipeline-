import pandas as pd
import json



with open("daikibo-telemetry-data.json", "r", encoding= 'utf-8') as f:
    data = json.load(f)

rows= []
for r in data:
    rows.append({
        'deviceID' : r["deviceID"],
        'deviceType' : r["deviceType"],
        'timestamp' : r["timestamp"],
        'country': r["location"] ["country"],
        "city" :r["location"] ["city"],
        "area" : r["location"] ["area"],
        "factory" :r["location"] ["factory"],
        "section" : r["location"] ["section"],
        "status" :r["data"] ["status"],
        "temperature" : r["data"] ["temperature"],

    })

df = pd.DataFrame(rows)
df.to_excel("Daikibo telemetry data.xlsx", index= False)


# # Load the JSON file
# df = pd.read_json(C

# # Convert and save to XLSX
# df.to_excel('Daikibo telemtry.xlsx', index=False)
