import cPickle
from glob import iglob
from os import path

def parseTestCaseTemplate(template):
	""" Each test case includes the following with the format key:<val>, see 
	README.txt for more information on the format.
	Args:
		template: the path of the template file
	Returns:
		Dict with required template keys mapped to values.
	"""
	keys = ['id', 'sourcefile', 'testdriver', 'requirement', 'component', 
			'method', 'inputs', 'outcome']
	template_dict = {}

	template_f = open(template, 'r')
	for line in template_f:
		line = line.replace('\n', '')
		lines = [line.strip() for line in line.split(':')]
		lines[0] = lines[0].lower()
		if lines[0] in keys:
			template_dict[lines[0]] = lines[1]
		else:
			print 'Error: Invalid test case template %s. Skipping...' % \
				template_f.name.split('/')[-1:][0]
			template_dict = None
			return None
	for k in keys:
		if k not in template_dict:
			print 'Error: Missing \'%s\' in template. Skipping...' % k
			template_dict = None
			return None
	template_f.close() 
	return template_dict

def parseCaseResults(results_dir):
	""" Generator to return each template dict with results from a test case
		run to avoid keeping all of them in memory.
	Args:
		results_dir: path to the template data directory
	Returns:
		(Iteratively) Each test case template dict in the file
	"""
	for template in iglob(path.join(results_dir, '*.pck')):
		f = open(template, 'r')
		yield cPickle.load(f)
		f.close()