import cohere

# ✅ Paste your Cohere API key here
co = cohere.Client("iMA2tvcSRv3w7NMKzeUfKf3WZB8WgIA5cIXBIGmA")

# 🗓️ User request — customize the location/date as needed
query = "Plan my weekend with fun and Christmas-themed activities in Bangalore for 21 and 22 Dec 2024."

# 🧠 Prompt to guide Cohere
prompt = f"""
You are a weekend planning assistant that helps users create a personalized weekend itinerary.

Based on the request below, provide a detailed yet clear response organized into 3 sections:

1. **Events**: Include event name, date, time, location, a short description, and a mock booking link (like BookMyShow or Insider.in).
2. **Activities**: Suggest engaging things to do with estimated time required, location, and tips (like best time to visit).
3. **Dining Options**: Recommend 2–3 restaurants or cafés in the area, mentioning cuisine, vibe, and links (like Google Maps or Zomato).

Make sure all suggestions are relevant to the dates: 21 and 22 December 2024 in Bangalore. If real events aren't known, suggest popular or evergreen Christmas activities that people can enjoy.

User Request: {query}

Your response:
"""

# 🧾 Get response from Cohere
response = co.generate(
    model="command-r-plus",
    prompt=prompt,
    max_tokens=600,
    temperature=0.8,
)

# 📌 Print the final plan
print(response.generations[0].text.strip())
