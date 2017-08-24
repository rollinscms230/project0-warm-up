### Automated testing program, ver. 0.1
### DSM, 2017

from os import system
from os import listdir
from sys import exit

programs = ['hello']
tests = ['hello1', 'hello2']

test_file_list = listdir('./tests')

num_passed = 0

# Build the project
rc = system('make')
if rc != 0:
	print 'Build failed. Exiting.'
	exit()
	
num_passed += 1  # A working build is one of the tests

for program in programs:
	
	print '\n#####  Testing program %s  #####' % program

	for test in tests:
		print '\n###  Test %s  ###' % test
		out_file = test + '.out'
		in_file = test + '.in'
		cmp_file = './tests/' + test + '.cmp'
		
		if in_file in test_file_list:
			run_command = './%s < ./tests/%s > %s' % (program, in_file, out_file)
		else:
			run_command = './%s > %s' % (program, out_file)
			
		diff_cmd = 'diff -q %s %s' % (out_file, cmp_file)
		
		system(run_command)
		rc = system(diff_cmd)

		if rc != 0:
			print '\nYour program\'s output:'
			system('cat %s' % out_file)
			print '\nExpected output:'
			system('cat %s' % cmp_file)
		else:
			print 'Passed.'
			num_passed += 1

print '\n#####  Final Score  #####'
print 'You passed %d out of %d tests.' % (num_passed, len(tests) + 1)
print 'Percentage = %f' % (float(num_passed) / (len(tests) + 1))