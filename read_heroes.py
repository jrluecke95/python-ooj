import pickle

message = "marvel is better than Dc"

with open('heroes.txt', 'wb') as file_handle:
    pickle.dump(message, file_handle)