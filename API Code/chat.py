import cohere

# Your Cohere API Key (replace with the actual key you got)
cohere_api_key = "oLjo2wBNZ0Fno0yfoGr6wyPiEGhlZxeL8OKes2Ak"

# Initialize the Cohere client
co = cohere.Client(cohere_api_key)

# Function to generate text based on a prompt
def generate_text(prompt):
    response = co.generate(
        model='command-xlarge',  # Use 'command-xlarge' model
        prompt=prompt,
        max_tokens=150  # Adjust the number of tokens (words) for the response
    )
    
    # Access the generated text from the 'choices' list
    generated_text = response.generations[0].text.strip()  # Correct way to access generated text
    return generated_text

# Prompt input from user
prompt = input("Enter the prompt (e.g., 'crime scene report generation'): ")

# Generate and print the response
print("Generated Text: ")
print(generate_text(prompt))