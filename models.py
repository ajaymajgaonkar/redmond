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
