# tau
This project relatives to courses from Test Automation Academy, Python branch.

* Course 1 (intro to pytest)
    - Chapter 1 (The first test case. 
    Run test in commands line from the project root directory by "python -m pytest" or just "pytest")
    - Chapter 2 (A failing test case)
    - Chapter 3 (A test case with an Exception)
    - Chapter 4 (Parametriezed test Cases) so usefull!!! 
	- Chapter 5 (Testing Classes)
	- Chapter 6 (@fixtures)
	- Chapter 7 (peremetrs to lounch:
					--verbose  -  pytest prints more data
					--quiet  -  show omnly failed test
					--exitfirst  -  stop after first test failed
					--maxfail=1 the same as previous but can run any failed tests
					--junit-xml report.xm;  -  save roport of run
					
					
				configuration:
					create a new file - pytest.ini with content: 
						[pytest]
						junit_family = xunit2  -  skip xml worning msg)
	- Chapter 8 (Filtering tests:
					run from folder: python -m pytest tests/test_accum.py
					run one test: python -m pytest tests/test_math.py::test_one_plus_one
					run test which contein part of word: python -m pytest -k one
					run test with any conditions: python -m pytest -k "one and not accum"
				MARKERS:
					@pytest.mark.math
					add to configuration file
					markers = 
					  math
					  accumulator)
					Run: python -m pytets -m math
					
				testpaths = tests  -  The command will kooking test only tests folder
				)
	
	- Chapter 9 ( Feature tests: rest API tests:
					pip install requests
					import requests
					
	- Chapter 10 ( Plugins:
					html reports  pip install pytest-html
					ti use it: python -m pytest --html=report.html
					
					cov plugin to show coverege of unittests
					
					*RUN* parralel 
					pip install pytest-xdist
					run in console: python -m pytest -n 3
					
