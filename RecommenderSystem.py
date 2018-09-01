# 

import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data and format it

data = fetch_movielens(min_rating=4.0)

#print training and test dat

print(repr(data['train']))
print(repr(data['test']))

#create model

model = LightFM(loss='warp') #weighted approximate-rank pairwise
#It uses gradient descent algorithm
#Content + Collaborative = Hybrid system

#train model
model.fit(data['train'], epochs=30, num_threads=2) #num_threads : parallel computations

def sample_recommendation(model, data, user_ids):
	
	#numberof users and movies in training data
	n_users, n_items = data['train'].shape

	#generate recommendations for each user we input
	for each_user_id in user_ids:

		#movies they already like
		known_positives = data['item_labels'][data['train'].tocsr()[each_user_id].indices]

		#predicted movies that they will like
		scores = model.predict(each_user_id, np.arange(n_items))

		#rank them in descending order
		top_items = data['item_labels'][np.argsort(-scores)]

		#print out the results
		print("User %s" % each_user_id)
		print("Known positives  :" )

		for x in known_positives[:3]:
			print("    %s" % x)

		print("Recommened :")

		for x in top_items[:3]:
			print("    %s" % x)

sample_recommendation(model,data, [2,5,100])