import cohere

# Initialize Cohere client
co = cohere.Client('iMA2tvcSRv3w7NMKzeUfKf3WZB8WgIA5cIXBIGmA')  # Replace with your actual API key

# Ingredients to use
ingredients = "chicken, garlic, and tomatoes"

# Use the chat endpoint instead of generate
response = co.chat(
    model="command-r-plus",  # or "command-r" if you don't have access to plus
    message=f"Give me a detailed recipe using the following ingredients: {ingredients}"
)

# Print the AI's response
print("Recipe:\n")
print(response.text.strip())
