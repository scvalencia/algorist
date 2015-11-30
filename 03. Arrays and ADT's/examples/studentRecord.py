class StudentRecord(object):

	def __init__(self, student_id, first_name, last_name, year, gpa):
		self._year_dct = {1 : 'Freshman', 2 : 'Sophomore', 3 : 'Junior', 4 : 'Senior'}
		self.id = student_id
		self.first_name = first_name
		self.last_name = last_name
		self.year = self._year_dct[year]
		self.gpa = gpa

class StudentFileReader(object):

	def __init__(self, file_name):
		self._file_name = file_name
		self._file_object = None

	def open(self):
		self._file_object = open(self._file_name, 'r')

	def close(self):
		self._file_object.close()
		self._file_object = None

	def _fetch_one(self):
		line = self._file_object.readline()
		if line == "":
			return None

		student_id = int(line.strip())
		first_name = self._file_object.readline().strip()
		last_name = self._file_object.readline().strip()
		year = int(self._file_object.readline().strip())
		gpa = float(self._file_object.readline().strip())

		student = StudentRecord(student_id, first_name, last_name, year, gpa)
		return student

	def fetch_all(self):
		records = []

		student = self._fetch_one()

		while student != None:
			records.append(student)
			student = self._fetch_one()

		return records

def main():

	sfr = StudentFileReader('students.txt')
	sfr.open()
	students = sfr.fetch_all()
	sfr.close()

	students.sort(key = lambda s : s.id)

	print 'LIST OF STUDENTS'.center(50)
	print 
	print "%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA')
	print "%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4)

	for student in students:
		print '%5d %-25s %-10s %4.2f' % (student.id, student.last_name + ', ' + student.first_name,
			student.year, student.gpa)

	print '-' * 47
	print 'Number of students: ', len(students)

if __name__ == '__main__':
	main()