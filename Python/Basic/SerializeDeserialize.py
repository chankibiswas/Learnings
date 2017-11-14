import pickle

# Serialize
example_dictionary = {1:'a', 2:'b', 3:'c'}

pickle_out = open("dict.pickle", "wb")
pickle.dump(example_dictionary, pickle_out)
pickle_out.close()


# Deserialize
##pickle_in = open("dict.pickle", "rb")
##example_dictionary = pickle.load(pickle_in)
##
##print(example_dictionary)
