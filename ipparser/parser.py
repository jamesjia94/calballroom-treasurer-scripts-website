from __future__ import division
import sys
from collections import OrderedDict
import pprint

# Returns the last name of a person.
def getLastName(line):
	l = line.split()
	return l[-1]

# Returns true if the lesson is an IP based on a list of "non-IP" strings.
def isIP(line):
	for non_IP_name in non_IPs:
		if non_IP_name in line.lower():
			return False
	return True 

# List of strings that are considered "non-IP" lessons.
non_IPs = ["rounds", "latin conditioning", "intermediate gt", "advanced gt", "beginner gt", "newcomer group", "bronze group", "silver group", "group technique", "ds group"]

def outputLessons(data):
	linebreak = True
	teacherName = ""

	nameToLessons = {}
	counts = {}
	GTs = {}

	# Process the file
	for line in iter(data.readline, ''):
		line = line.rstrip()
		# If the previous line was a newline, this line must be a teacher's name.
		if linebreak:
			teacherName = line
			linebreak = False
		else:
			# If this line is a newline, set linebreak to True.
			if line == "":
				linebreak = True
				continue
			# Otherwise, we are processing a class 
			else:
				# Get all the people in the class
				names = line.split(",")
				for name in names:
					val = 1/len(names)
					# If the name is already in the dictionary of people who are taking classes
					if name in nameToLessons:
						# If the teacher is already dictionary of classes that this person is taking
						if teacherName in nameToLessons[name]:
							nameToLessons[name][teacherName] = nameToLessons[name][teacherName] + val
						# Otherwise, add teacher to classes taken by this person
						else:
							nameToLessons[name][teacherName] = val
					# Since name isn't in the dictionary of people who are taking classes, store (name, dictionary of classes taken).
					else:
						nameToLessons[name] = OrderedDict()
						nameToLessons[name][teacherName] = val
			# If this is an IP, add this class to the count of IPs taught by this teacher.
			if isIP(line):
				if teacherName in counts:
					counts[teacherName] = counts[teacherName] + 1
				else:
					counts[teacherName] = 1
			# Otherwise, add this class to the count of GTs taught by this teacher.
			else:
				if teacherName in GTs:
					GTs[teacherName] = GTs[teacherName] + 1
				else:
					GTs[teacherName] = 1
	return (nameToLessons, counts, GTs)


if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "Please specify file to parse."
		sys.exit(0)
	fname = sys.argv[1]
	data = open(fname,"r")
	pp = pprint.PrettyPrinter()

	(nameToLessons, counts, GTs) = outputLessons(data)

	keys = nameToLessons.keys()
	keys.sort(key=getLastName)
	for key in keys:
		print key
		pp.pprint(dict(nameToLessons[key]))
		print

	print "IP Lessons"
	print counts
	print "GTs and Rounds"
	print GTs