import os
filename = 'student.txt'
def main():
	while True:
		menu()
		choice_list = [0, 1, 2, 3, 4, 5, 6, 7]			
		choice = int(input('请选择：'))
		if choice not in choice_list:
			print('输入无效，请重新输入')
			continue
		if choice == 0:
			print('感谢使用，886！！！')
			break
		elif choice == 1:
			insert()
		elif choice == 2:
			search()
		elif choice == 3:
			delete()
		elif choice == 4:
			modify()
		elif choice == 5:
			sort()
		elif choice == 6:
			total()
		elif choice == 7:
			showall()

def insert():
	student_list = []
	while True:
		name = input('请输入学生姓名：')
		id = input("请输入学生ID：")
		if name and id:
			try:
				python_score = int(input("请输入python成绩："))
			except:
				print('输入无效，不是整数类型，请重新输入')
				continue
		else:
			print('name or id 为空，请重新输入')
			continue
		student = {'id': id, 'name': name, 'python': python_score}
		student_list.append(student)
	
		choice = input('是否继续录入? Y|N')
		if choice == 'Y' or choice == 'y':
			continue
		else:
			break
	save(student_list)
	print('录入学生信息完成！')

def save(list):
	if os.path.exists(filename):
		with open(filename, 'a') as af:
			for item in list:
				af.write(str(item) + '\n')
	else:
		with open(filename, 'w') as wf:
			for item in list:
				wf.write(str(itme) + '\n')
	
def search():
	student_list = []
	with open(filename, 'r', encoding='utf-8') as rf:
		students = rf.readlines()

	while True:
		id = ''
		name = ''
		choice = int(input('请输入查询方式 1.ID查询，2.姓名查询：'))
		if choice == 1:
			id = input('请输入ID：')
								
		elif choice == 0:
			name = input('请输入学生姓名：')

		else:
			print('输入不对，请重新输入')
			continue
		
		for student in students:
			student_dict = dict(eval(student))
			if student_dict['id'] == id or student_dict['name'] == name:
				student_list.append(student)
		show(student_list)
		student_list.clear()
		choice = input('是否继续Y|N：')
		if choice == 'Y' or choice == 'y':
			continue
		else:
			break
	
def show(lst):
	if len(lst) == 0:
		print('没有查询到学生信息, 无数据显示')
		return

	format_title = '{:^6}\t{:^12}\t{:^8}'
	print(format_title.format('ID', '姓名', 'python成绩'))
	format_data = '{:^6}\t{:^12}\t{:^8}'
	for item in lst:
		if not isinstance(item, dict):
			item = dict(eval(item))
			print(format_data.format(item.get('id'),
						item.get('name'),
						item.get('python'),
						))
		else:
                        print(format_data.format(item.get('id'),
                                                item.get('name'),
                                                item.get('python'),
                                                ))		
def delete():
	student_new = []
	while True:
		id = input('请输入要删除的ID：')
		if not id:
			continue
		else:
			with open(filename, 'r') as rf:
				student_old = rf.readlines()

			flag = False
			if student_old:
				for student in student_old:
					student_dict = dict(eval(student))
					if student_dict['id'] != id:
						student_new.append(student)

					else:
						flag = True
				if flag:
					print(f'id为{id}的学生信息已删除')
				else:
					print(f'没有找到ID为{id}的学生信息')
						
				with open(filename, 'w') as wf:
					for student in student_new:
						wf.write(str(student)+'\n')
				
			else:
				print('无学生信息')
				break						

		show(student_new)

		student_new.clear()

		choice = input('是否继续删除Y|N：')
		if choice == 'y' or choice == 'Y':
			continue
		elif choice == 'n' or choice == 'N':
			break	
def modify():
	student_new = []
	while True:
		with open(filename, 'r') as rf:
			student_old = rf.readlines()

		id = input('请输入要修改的id：')
		if not id:
			continue
		else:
			flag = False
			for student in student_old:
				student_dict = dict(eval(student))
				if student_dict['id'] != id:
					student_new.append(student_dict)
				else:
					flag = True
					name = input('请输入姓名：')
					python = input('请输入python：')
					student_dict['name'] = name
					student_dict['python'] = python
					student_new.append(student_dict)
			
			if flag:
				print('修改成功！！！')

		with open(filename, 'w') as wf:
			for student in student_new:
				wf.write(str(student)+'\n')
		student_new.clear()
		
		choice = input('是否继续删除Y|N：')
		if choice == 'y' or choice == 'Y':
			continue
		elif choice == 'n' or choice == 'N':
			break
def sort():
	student_new=[]
	with open(filename, 'r') as rf:
		student = rf.readlines()
		for item in student:
			student_new.append(dict(eval(item)))

	choice = int(input('请选择排序方式，升序0，降序1：'))
	if choice == 0:
		choice = int(input('请选择排序方式，python为0：'))
		if choice == 0:
			student_new.sort(key=lambda x : int(x['python']), reverse=True)
	
	elif choice == 1:
		choice = int(input('请选择排序方式，python为0：'))
		if choice == 0:
			student_new.sort(key=lambda x : int(x['python']), reverse=False)

	show(student_new)

def total():
	with open(filename, 'r') as rf:
		student = rf.readlines()
	print(f'学生总人数: {len(student)}')	

def showall():
	with open(filename, 'r') as rf:
		student = rf.readlines()
	show(student)
		
def menu():
	print('======================学生信息管理系统===========================')
	print('-------------------------功能菜单-------------------------------')
	print('					1. 录入学生信息')
	print('					2. 查找学生信息')
	print('					3. 删除学生信息')
	print('					4. 修改学生信息')
	print('					5. 排序')
	print('					6. 统计学生总人数')
	print('					7. 显示所有学生信息')
	print('					0. 退出系统')
	print('-------------------------------------------------------------')


if __name__ == '__main__':
	main()


