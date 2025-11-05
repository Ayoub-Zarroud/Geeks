def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# Call the function with default values
make_shirt()
# Call the function with custom size but default text
make_shirt("medium")
# Call the function with custom size and custom text
make_shirt("small", "Custom message")
# Bonus: Using keyword arguments
make_shirt(size="small", text="Hello!")
