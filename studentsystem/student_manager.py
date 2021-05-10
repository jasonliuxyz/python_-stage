'''
面向对象版本
author：jason.liu
date: 2021/05/10
'''

class Student:
	def __init__(self, id, name, python):
		self.id = id
		self.name = name
		self.python = python

	def __str__(self):
		return "{'id': '%s', 'name': '%s', 'python': '%s'}" %(self.id,self.name,self.python)

class StudentManager:
	def __init__(self):
		self.student_dict = {}

	def startup(self):
		self.load_from_file('/Users/liucheng/Code/python/studentsystem/student.txt')
		while True:
			self.menu()
			choice_list = [0, 1, 2, 3, 4, 5, 6, 7]
			choice = int(input('请选择：'))
			if choice not in choice_list:
				print('输入无效，请重新输入')
				continue
			if choice == 0:
				print('感谢使用，886！！！')
				self.save_to_file('/Users/liucheng/Code/python/studentsystem/student.txt')
				break
			elif choice == 1:
				self.insert()
			elif choice == 2:
				self.search()
			elif choice == 3:
				self.delete()
			elif choice == 4:
				self.modify()
			elif choice == 5:
				self.total()
			elif choice == 6:
				self.showall()

	def menu(self):
		print('======================学生信息管理系统===========================')
		print('-------------------------功能菜单-------------------------------')
		print('					1. 录入学生信息')
		print('					2. 查找学生信息')
		print('					3. 删除学生信息')
		print('					4. 修改学生信息')
		print('					5. 统计学生总人数')
		print('					6. 显示所有学生信息')
		print('					0. 退出系统')
		print('-------------------------------------------------------------')

	def insert(self):
		while True:
			name = input('请输入学生姓名：')
			id = input("请输入学生ID：")
			if name and id:
				try:
					python = int(input("请输入python成绩："))
				except:
					print('输入无效，不是整数类型，请重新输入')
					continue
			
				if id in self.student_dict.keys():
					print("学生已存在！！！")
					continue
				else:
					student = Student(id, name, python)
					self.student_dict[id] = student
					print(f'添加学生{id}成功' + '\n')
					print(student)	
			choice = input('是否继续录入? Y|N')
			if choice == 'Y' or choice == 'y':
				continue
			else:
				break
	def search(self):
		while True:
			choice = int(input('请输入查询方式 1.ID查询，2.姓名查询：'))
			if choice == 1:
				#print(self.student_dict.keys())
				id = input('请输入ID：')
				if id in self.student_dict.keys():
					print(self.student_dict[id])
				else:
					print('没有这个学生信息！！！')

			if choice == 2:
				name = input('请输入学生姓名：')
				#print(self.student_dict.items())
				for student in self.student_dict.values():
					if name == student.name:
						print(student)
					else:
						print('没有这个学生信息！！！')

			choice = input('是否继续查找？ Y|N')
			if choice == 'Y' or choice == 'y':
				continue
			else:
				break

	def delete(self):
		while True:
			id = input('请输入要删除的ID：')
			if id in self.student_dict.keys():
				print(self.student_dict[id])
				self.student_dict.pop(id)

			else:
				print('没有这个学生信息！！！')

			choice = input('是否继续删除？ Y|N')
			if choice == 'Y' or choice == 'y':
				continue
			else:
				break

	def modify(self):
		while True:
			id = input('请输入要修改的id：')
			if id in self.student_dict.keys():
				name = input('请输入姓名：')
				python = input('请输入python：')
				student = Student(id, name, python)
				student_dict[id] = student
				print(f'修改学生{id}成功' + '\n')
			else:
				print('没有这个学生信息！！！')

			choice = input('是否继续删除？ Y|N')
			if choice == 'Y' or choice == 'y':
				continue
			else:
				break

	def sort(self):
		while True:
			choice = int(input('请选择排序方式，升序0，降序1：'))
			if choice == 0:
				choice = int(input('请选择排序方式，python为0：'))
				if choice == 0:
					pass

			if choice == 1:
				pass

	def total(self):
		print(len(self.student_dict))

	def showall(self):
		for i in self.student_dict.values():
			print(i)

	def load_from_file(self, file):
		with open(file, 'r', encoding='utf-8') as rf:
			for item in rf.readlines():
				print(item)
				tmp_student_dict = dict(eval(item))
				id = tmp_student_dict['id']
				name = tmp_student_dict['name']
				python = tmp_student_dict['python']
				student = Student(id, name, python)
				self.student_dict[id] = student		
		 
	def save_to_file(self, file):
		with open(file, 'w') as wf:
			student_list = self.student_dict.values()
			for student in student_list:
				wf.write(str(student) + '\n')		
	

if __name__ == '__main__':
	sm = StudentManager()
	sm.startup()	
