train_data = []

with  open('../aclImdb/movie_data/full_train.txt') as ifile:
    for i in ifile:
        train_data.append(i.strip())
        

test_data  = []

with open('../aclImdb/movie_data/full_test.txt') as ifile:
	for i in ifile:
		test_data.append(i.strip())