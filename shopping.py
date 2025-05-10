import cohere

# ✅ Paste your Cohere API key here
co = cohere.Client("iMA2tvcSRv3w7NMKzeUfKf3WZB8WgIA5cIXBIGmA")

# 🛍️ User query — change as needed
query = "I am looking for black running shoes under ₹10,000 suitable for long-distance running."

# 🧠 Prompt to guide Cohere
prompt = f"""
You are a product recommender assistant who helps users find the best products online.

Based on the user's request, suggest 2–3 product options from trusted e-commerce websites (like Amazon, Flipkart, Myntra, etc.).
For each product, provide:
- Product Name
- Brand
- Price (Approx.)
- Key Features
- Why it suits the user's preferences

Only suggest products that are in stock and popular.

User request: {query}

Your response:
"""

# 🧾 Get the response from Cohere
response = co.generate(
    model="command-r-plus",
    prompt=prompt,
    max_tokens=500,
    temperature=0.8,
)

# 📦 Print the suggestions
print(response.generations[0].text.strip())
