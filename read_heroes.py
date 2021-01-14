import pickle

with open('heroes.txt', 'rb') as file_handle:
    old_message = pickle.load(file_handle)
    print(f"Old message is: '{old_message}'")

yser_input = input("What to save? ")

with open('heroes.txt', 'wb') as file_handle:
    pickle.dump(message, file_handle)
    print("message saved. ")

