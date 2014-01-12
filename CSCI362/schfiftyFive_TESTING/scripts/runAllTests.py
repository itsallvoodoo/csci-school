#!/usr/bin/env python
import datetime
from glob import iglob
import os
import re
import subprocess
from subprocess import CalledProcessError
import shutil
import sys
import webbrowser
import cPickle

from parse import *

# Directory containing project source files.
PROJECT_DIR = 'project'
# Directory containing test case templates.
TEST_CASE_DIR = 'testCases'
# Directory containing test case executables.
TEST_EXECUTABLE_DIR = 'testCasesExecutables'
# Directory containing test case oracles.
TEST_ORACLE_DIR = 'oracles'
# Directory for compiled java files and test output.
TEST_TEMP_DIR = 'temp'

def compileTarget(target_path):
	""" Compile a source file to the ./temp directory if target_path 
		is java file (see decorator).
	"""
	try:
		print "Compiling %s..." % target_path
		subprocess.check_call(['javac',
			'-classpath', PROJECT_DIR, '-d', 
			TEST_TEMP_DIR, target_path])
	except subprocess.CalledProcessError:
		print 'Error: Test driver %s failed to compile.\n' % target_path
		return False
	return True

def executeTest(test_case):
	""" Execute a test file containing a test case, which should
		be defined in the test case's template (and subsequently located
		in ./testCasesExecutables)
		Args:
			test_case: filename of java test case for the project
		Returns:
			False if run or compliation failed, else output of test file.
	"""
	test_case = test_case.replace('.java', '')
	test_output = None
	try:
		print 'Running %s...' % test_case
		test_output = subprocess.check_output(['java', 
			'-classpath', TEST_TEMP_DIR, 
			TEST_EXECUTABLE_DIR + '/' + test_case])
	except subprocess.CalledProcessError:
		print 'Error: Test driver %s failed to run.\n' % test_case
		return False
	return test_output

def compareOracle(output_file, oracle):
	""" Compare the result of a test case to the expected output, which
		is contained within an oracle file in the /oracles directory.
		Args:
			output_file: filename of the output 
			oracle: filename of the associated oracle containing expected output
		Returns:
			True if the oracle matches the output, otherwise False.
	"""
	output_file = '%s/%s' % (TEST_TEMP_DIR, output_file)
	oracle = '%s/%s' % (TEST_ORACLE_DIR, oracle)
	try:
		diff = subprocess.check_output(['diff', output_file, oracle])
		return 'Pass'
	except CalledProcessError:
		return 'Fail'

def buildHTMLReport(results_dir):
	""" Read all compiled test reports and generate an html file.
		Args:
			results_dir: path to directory containing all the pickled template
				data for each test run
		Returns:
			path to generated html report
	"""
	timestamp = str(datetime.datetime.today()).replace(' ', '-')
	filename = 'testReport%s.html' % timestamp
	html = open('./reports/' + filename,'w+')
		
	html.write(
        "<!DOCTYPE html>\n"\
        "<html>\n"\
        "<head> <link rel='stylesheet' href='resources/table.css' type='text/css'/>\n"\
        "<title>\n"\
        "Test Case Report\n"\
        "</title>\n"\
        "<script src ='resources/js.js' type='text/javascript'></script></head>\n"\
        "<body>\n"\
        "<h1 align ='center'>Test Report Summary for Openremote Software Platform</h1>\n"\
        "<div class='CSS_Table_Example'>\n"\
        "<h3>General Information:</h3>\n"\
        "<ul><li>Team Name: Schfifty-Five</li><li>Group Members: Chad Hobbs, Jake Wisse, Brett Oswald, Andrew Rodman, and Jason Daniel</li><li>Class: CSCI-362</li></ul>\n"\
        "</div>\n"\
        "<div >\n"\
        "<table align='right'>\n"\
        "<tr><th>Number of Test Cases:</th><td><img src ='resources/numTests.png' alt ='number of tests'></td></tr>\n"\
        "<tr><th>Passed:</th><td><img src ='resources/pass.png' alt ='passed'></td></tr>\n"\
        "<tr><th>Failed:</th><td><img src ='resources/fail.png' alt ='failed'></td></tr>\n"\
        "<tr><th>Error:</th><td><img src ='resources/error.png' alt ='error'></td></tr>\n"\
        "<tr><th>Expected to Fail:</th><td><img src ='resources/expected.png' alt ='expected number of failures'></td></tr>\n"\
        "<tr><th>Time Elapsed:</th><td><img src ='resources/time.png' alt ='total time'></td></tr>\n"\
        "<div>\n"\
        "<p><input type ='submit' name ='Show/Hide Table' value = 'Show/Hide Table'  onClick=\"setTable('table1');return false\"></p>\n"\
        "<p><input type ='submit' name ='Show missing Row Data' value = 'Show missing Row Data'  onClick=\"display_rows('table1');\"></p>\n"\
        "</div>\n"\
        "</div>\n"\
        "<table id ='table1' style=\"display:block;\" class='CSS_Table_Example'>\n"
        )
	html.write("<tr>\n")

	keys = ['id', 'sourcefile', 'testdriver', 'requirement', 'component', 
		'method', 'inputs', 'outcome', 'result']
	for k in keys:
		html.write("<th>\n"+k+"\n</th>\n")
	html.write("</tr>\n")
	        
        numPassed = 0;
        numFailed = 0;
        numErrors = 0
	for template in parseCaseResults(results_dir):
		html.write("<tr id ="+template['id']+" onclick=\"toggle('"+template['id']+"')\">\n")

		for k in keys:                                        
                    if k == 'result':
                        if template[k] == 'Pass':
                            numPassed = numPassed + 1
                            html.write("<td><img src ='resources/pass.png' alt ='Passed'></td>")
                        elif template[k] == 'Error':
                            numFailed = numFailed + 1
                            html.write("<td><img src ='resources/error.png' alt ='Error'></td>")
                        elif template[k] == 'Fail':
                            numErrors = numErrors + 1
                            html.write("<td><img src ='resources/fail.png' alt ='Failed'></td>")                    
                    else:
                        html.write("<td>\n"+ template[k] +"</td>\n")
	html.write("</tr>\n</table>\n")
        html.write("<div class ='CSS_tab;e_example'>\n"\
                    "<h2>Summary Statistics</h2>"
                    "<p>Total Number of tests ran: " +str(numPassed + numFailed +numErrors)+".<br/>\n"\
                    "Total Number of tests failed: " +str(numFailed)+".<br/>\n"\
                    "Total Number of tests passed: " +str(numPassed)+".<br/>\n"\
                    "Total Number of tests with errors: " +str(numErrors)+".<br/>\n"\
                    "</p>\n</div>")
			
	html.write("</div></body>\n</html>")
	filename = html.name
	html.close()
	return filename

def cleanTemp(temp_dir, results_dir):
	clearDirectory(temp_dir)
	try:
		os.rmdir(os.path.join(temp_dir, 'testCasesExecutables'))
		shutil.rmtree(os.path.join(temp_dir, 'com'))
		shutil.rmtree(os.path.join(temp_dir, 'org'))
	except:
		pass
	try:
		shutil.rmtree(results_dir)
	except:
		pass

def clearDirectory(path):
	""" Remove everything recursively from path
	"""
	files = os.listdir(path)
	for item in files:
		if '.svn' not in item:
			f = os.path.join(path, item)
			if os.path.isdir(f):
				clearDirectory(f)
			else:
				os.remove(f)

def main():
	cwd = os.getcwd()
	temp_dir = os.path.join(cwd, TEST_TEMP_DIR)
	cases_dir = os.path.join(cwd, TEST_CASE_DIR)
	temp_res_dir = os.path.join(temp_dir, 'templates')

	cleanTemp(temp_dir, temp_res_dir)

	print '\nGathering templates from %s...' % TEST_CASE_DIR
	os.mkdir(temp_res_dir)
	# glob.iglob uses a generator instead of a list, so filenames will be
	# returned lazily instead of keeping all of them in memory.
	for case in iglob(os.path.join(cases_dir, '*.txt')):
		if '~' in case:
			# The file is a temporary one created by Linux - skip it.
			continue
		# Build a dictionary with the parsed template values we need.
		case_properties = parseTestCaseTemplate(case)
		if not case_properties:
			continue

		driver = case_properties['testdriver']
		compileTarget(os.path.join(TEST_EXECUTABLE_DIR, driver))
		output = executeTest(driver)
		if output:
			# Write the output to a temporary file to be diff'd against the 
			# associated oracle.
			out_name = driver.replace('.java', '.tmp')
			out_file = open(os.path.join(temp_dir, out_name), 'w+')
			# Newline is required since Java std outputs automatically append
			# append it for most functions.
			out_file.write(output + '\n')
			out_file.close()

			oracle = driver.replace('.java', '.oracle').lower()
			case_properties['result'] = compareOracle(out_name, oracle)
		else:
			case_properties['result'] = 'Error'
		# Pickle the results dict and dump it into a file to keep as little
		# in memory as possible.
		p_fname = os.path.join(temp_res_dir, driver.replace('.java', '.pck'))
		p_file = open(p_fname, 'w+')
		cPickle.dump(case_properties, p_file)
		p_file.close()

	report_filename = buildHTMLReport(temp_res_dir)
	print '\nTesting Complete, Opening Report in Browser Window.'
	if report_filename:
		url = 'file:///%s' % os.path.abspath(report_filename)
		webbrowser.open_new_tab(url)
	
	cleanTemp(temp_dir, temp_res_dir)

if __name__ == '__main__':
	main()
