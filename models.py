class User:
	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password

class Candidate:
	def __init__(self, name, email, summary, projects):
		self.name = name
		self.email = email
		self.summary = summary
		self.projects = projects

class Experience:
	def __init__(self, company, duration, description):
		self.company = company
		self.duration = duration
		self.description = description
