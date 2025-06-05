#rihito

import requests
import time, os

os.system('clear')
token = input("Enter your Access Token: ").strip()
link = input("Enter the link to share: ").strip()
shares = int(input("How many times to share? "))
delay = float(input("Delay between shares (in seconds): "))

for i in range(1, shares + 1):
    response = requests.post(
        "https://graph.facebook.com/v13.0/me/feed",
        data={
            "link": link,
            "published": "0",
            "privacy": '{"value":"SELF"}',
            "access_token": token
        }
    ).json()

    if "id" in response:
        print(f"[{i}] Shared successfully. Post ID: {response['id']}")
    else:
        print(f"[{i}] Failed to share: {response}")
        break

    time.sleep(delay)

print("Done.")
