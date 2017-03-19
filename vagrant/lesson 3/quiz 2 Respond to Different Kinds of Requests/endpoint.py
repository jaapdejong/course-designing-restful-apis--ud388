from flask import Flask, request
app = Flask(__name__)
# Create the appropriate app.route functions, test and see if they work, and paste your URIs in the boxes below.

#Make an app.route() decorator here
@app.route("/puppies", methods = ["GET", "POST"])
def puppiesFunction():
	if request.method == 'GET':
		#Call the method to Get all of the puppies
		print 'GET /puppies'
		return getAllPuppies()

	elif request.method == 'POST':
		#Call the method to make a new puppy
		print 'POST /puppies'
		return makeANewPuppy()  
  
 
#Make another app.route() decorator here that takes in an integer id in the 
@app.route("/puppies/<int:id>", methods = ["GET", "PUT", "DELETE"])
def puppiesFunctionId(id):
	if request.method == 'GET':
		#Call the method to get a specific puppy based on their id
		print 'GET /puppies/' + str(id)
		return getPuppy(id)
		
	elif request.method == 'PUT':
		#Call the method to update a puppy
		print 'PUT /puppies/' + str(id)
		return updatePuppy(id)
		
	elif request.method == 'DELETE':
		#Call the method to remove a puppy
		print 'DELETE /puppies/' + str(id)
		return deletePuppy(id)


def getAllPuppies():
	print 'getAllPuppies()'
	return "Getting All the puppies!"

def makeANewPuppy():
	print 'makeANewPuppy()'
	return "Creating A New Puppy!"

def getPuppy(id):
	print 'getPuppy(' + str(id) + ')'
	return "Getting Puppy with id %s" % id

def updatePuppy(id):
	print 'updatePuppy(' + str(id) + ')'
	return "Updating a Puppy with id %s" % id

def deletePuppy(id):
	print 'deletePuppy(' + str(id) + ')'
	return "Removing Puppy with id %s" % id

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)

