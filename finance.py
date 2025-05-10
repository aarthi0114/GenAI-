import cohere

# ✅ Use your API key here
co = cohere.Client("iMA2tvcSRv3w7NMKzeUfKf3WZB8WgIA5cIXBIGmA")

# 📊 User request — simulated analyst summary
query = "Summarize the latest analyst recommendations for NVIDIA (NVDA)."

# 🧠 Prompt to guide the model
prompt = f"""
You are a financial assistant who helps users understand stock market insights.

Based on the user's request, provide a summarized analysis of analyst recommendations for NVIDIA (NVDA).
Since you do not have real-time data, respond as if you are simulating a report.

Include:
- Overall analyst sentiment (e.g., Strong Buy, Hold, Sell)
- Number of analysts in each category
- Target price range
- General market outlook on the stock

Format your answer using a neat table and bullet points.

User request: {query}

Your response:
"""

# 🧾 Get Cohere response
response = co.generate(
    model="command-r-plus",
    prompt=prompt,
    max_tokens=600,
    temperature=0.7,
)

# 📄 Print the output
print(response.generations[0].text.strip())
