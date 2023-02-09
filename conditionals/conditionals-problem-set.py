# Conditionals Recap
# Assume we have the following variable declarations -- select all options that will evaluate to true:
var1 = None
var2 = 1
var3 = {}
var4 = [0, 0]
var5 = "None"

# var1 or var2
# var5 and var2
# var4 or var3
# var5 or var3
# var2 or not var5
# not (var3 or var1)

# Conditionals Problem Set - id: 246422d2-e06a-4ed9-83e1-602e4acfaca8
# A grocery store's point of sale system generates notifications when a product reaches low inventory levels. For this example, the low inventory threshold is 10 units or lower. Select the option that best describes the logic for this notification.
def check_inventory_level():
    if product_details["inventory"] <= 10:
        print(product_details["name"] + " is low in stock.")

# Conditionals Problem Set - id: b6ed651c-a170-47c6-a57f-d3e22e7e7f0d
# Netflix allows basic plan subscribers to stream on one device at a time. Which option would notify basic plan subscribers when they go over this limit?
def check_streaming_limit():
    if len(streaming_devices) > 1:
        print("Your Netflix account is in use on too many devices. Please stop playing on other devices to continue. Visit netflix.com/help for more information.")
    else:
        open_browse_page()

# Conditionals Problem Set - id: 4dd59372-ea02-4809-94fe-4fd42a4cb172
# Select the option that best describes how a smart car would behave when detecting a traffic light.
if traffic_light_color == "green":
    print("continue driving at current speed")
elif traffic_light_color == "red":
    print("reduce speed to stop")
elif traffic_light_color == "yellow":
    print("reduce speed by half and check traffic_light_color again")
else:
    print("prepare to reduce speed")
