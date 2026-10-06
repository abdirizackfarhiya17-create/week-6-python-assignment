# unbreakable.py
print("This program is unbreakable! Type 'exit' to quit.")

while True:
    try:
        data = input("Enter a whole number: ")
        
        if data.lower() == 'exit':
            print("Goodbye!")
            break
            
        number = int(data)
        print(f"Success! Your number doubled is: {number * 2}\n")
        
    except ValueError:
        print("Error: That wasn't a valid whole number. Try again!\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}\n")
