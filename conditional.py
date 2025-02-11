a = list(map(int, input("Enter the elements separated by space: ").split()))  # Convert input into a list of integers
grt = a[0] if a else None  # Initialize 'grt' with the first element if the list is not empty

for i in a:
    if i > grt:
        grt = i  # Update the greatest element

if grt is not None:
    print("Greatest element:", grt)
else:
    print("No elements entered.")
