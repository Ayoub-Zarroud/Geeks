def box_printer(*words):
    # Find the longest word to size the box
    max_length = max(len(word) for word in words)
    border = "*" * (max_length + 4)
    
    print(border)
    for word in words:
        print(f"* {word.ljust(max_length)} *")
    print(border)


# Example usage
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
