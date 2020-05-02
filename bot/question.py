class Question(object):
	#Question constructor
	#parameters:
# question_text - text of your question
	#internal_name - name of your question in English is used to add questions to results
	#answer_type - type of an answer can be bool or text
	def __init__(self, question_text, internal_name, answer_type):
		self.question_text = question_text
		self.internal_name = internal_name
		self.answer_type = answer_type
