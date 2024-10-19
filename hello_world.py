def greet():
    name = input("Please enter your name: ").strip()
    
    if not name:
        print("Error: Name cannot be empty. Please provide a valid name.")
    else:
        print(f"Hello, {name}! Welcome to Hacktoberfest!")

if __name__ == "__main__":
    greet()
