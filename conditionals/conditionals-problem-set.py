# Conditionals Recap
# Assume we have the following variable declarations -- select all options that will evaluate to true:

# var1 = None
# var2 = 1
# var3 = {}
# var4 = [0, 0]
# var5 = "None"

# var1 or var2
# var5 and var2
# var4 or var3
# var5 or var3
# var2 or not var5
# not (var3 or var1)

# Conditionals Problem Set - id: 246422d2-e06a-4ed9-83e1-602e4acfaca8
# A grocery store's point of sale system generates notifications when a product reaches low inventory levels. For this example, the low inventory threshold is 10 units or lower. Select the option that best describes the logic for this notification.

# def check_inventory_level():
#     if product_details["inventory"] <= 10:
#         print(product_details["name"] + " is low in stock.")

# Conditionals Problem Set - id: b6ed651c-a170-47c6-a57f-d3e22e7e7f0d
# Netflix allows basic plan subscribers to stream on one device at a time. Which option would notify basic plan subscribers when they go over this limit?

# def check_streaming_limit():
#     if len(streaming_devices) > 1:
#         print("Your Netflix account is in use on too many devices. Please stop playing on other devices to continue. Visit netflix.com/help for more information.")
#     else:
#         open_browse_page()

# Conditionals Problem Set - id: 4dd59372-ea02-4809-94fe-4fd42a4cb172
# Select the option that best describes how a smart car would behave when detecting a traffic light.

# if traffic_light_color == "green":
#     print("continue driving at current speed")
# elif traffic_light_color == "red":
#     print("reduce speed to stop")
# elif traffic_light_color == "yellow":
#     print("reduce speed by half and check traffic_light_color again")
# else:
#     print("prepare to reduce speed")

# Conditionals Problem Set - id: 41ac7ae8-8b94-4305-8b05-40e0855fc00f
# Online-retailers often provide free shipping to members if their cart total reaches at least $100. Select the option that describes the logic to determine if a customer will receive free shipping or not.

# if is_account_member and cart >= 100:
#     print("You are qualified for free shipping. Proceed to checkout.")
# elif is_account_member is False and cart >= 100:
#     print("Sign up today for free shipping on your next order.")
# else:
#     print("Save on shipping by becoming a member and spending $100 on your order. Offer ends soon!")

# Conditionals Problem Set - id: 744730ac-4364-42c7-84db-5d2951d08af2
# Imagine you are a game developer for a new Mario Kart game. You are developing the game mechanic to unlock stages. In order for the player to unlock Peach's Castle, Mario needs to reach a skill level of at least 10 and earn at least 8 stars from previous stages. Which option best describes the conditional to build this feature?

# if skill_level >= 10 and total_stars_count >= 8:
#     print("Peach's Castle is unlocked!")
# else:
#     print("Must reach level 10 and achieved 8 stars")

# Conditionals Problem Set - id: 00216143-06ad-457e-b2aa-1d1dfd1e1a07
# The Cinnamon Cinema always prices movie tickets based on age. There is a new promotion for additional discounts to reward individuals for pursuing an education. The discounted ticket prices per age are listed below.

# if customer_age < 0:
#     print("please enter a valid age.")
# elif customer_age <= 10:
#     ticket_price = 10.00
# elif customer_age <= 17:
#     ticket_price = 13.00
# elif customer_age < 60:
#     ticket_price = 15.00
# else:
#     ticket_price = 11.00

# Conditionals Problem Set - id: a61f06a0-94aa-4617-89a2-86f1217c8ef4
# Voice assistants like Alexa will turn on when any of its "wake words" is announced nearby. Which option best describes this behavior?

# if "alexa" in users_speech or "echo" in users_speech:
#   print("processing your request...")