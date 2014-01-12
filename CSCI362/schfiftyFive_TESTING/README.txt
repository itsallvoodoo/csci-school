DIOTeam 5 (Schfifty-Five) Testing Framework for the OpenRemote Controller platform.
Developers:
Drew Rodman
Chadd Hobbs
Jason Daniel
Jake Wisse
Brett Ostwalt

Test Execution:
To execute all test cases, perform the following actions:
1. Ensure that you have at least Python 2.5 installed
2. Run Terminal or the command-line equivalent
3. cd (change directory) to this directory
4. Run 'chmod +x scripts/runAllTests.py' without the quotes
5. Run 'scripts/runAllTests.py', again without the quotes
6. The report should launch automatically in a browser window. If not, 
	the output can be found in the reports folder.
NOTE: All of the directories below must be present for the script to run.

Directory Layout:
/docs
	Any documentation for tests or project code
/oracles
	Text files containing expected output of test executables. 
	NOTE: these files must have the same filename as their corresponding
	executable, but with .oracle instead of .java
/reports
	Generated HTML files containing the results of a test run
/scripts
	Helper scripts for executing the tests
/src
	Contains the relevant OpenRemoteController project files
/temp
	Stores temporary files from test execution
/testCases
	Templates following the format below for defining test cases.
/testCasesExecutables
	Java files that will perform the expected tests and provide output to stdout.

Test Case Template Format (key-value pairs):
	1. Id: Test id
	2. SourceFile: project file being tested (with .java)
	3. Driver: test case executable (with .java)
	4. Requirement: Requirement being tested
	5. Component: Component being tested
	6. Method: Method being tested
	7. Inputs: Test inputs or command line arguments (if any)
	8. Outputs: Expected outcome(s)