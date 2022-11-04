from jinja2 import Template

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name    


person = Person('Peter', 34)

tm = Template("My name is {{ per.getName() }} and I am {{ per.getAge() }}")
msg = tm.render(per=person)

print(msg)

person = { 'name': 'Person', 'age': 34 }

tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
# tm = Template("My name is {{ per['name'] }} and I am {{ per['age'] }}")
msg = tm.render(per=person)

print(msg)

tm = Template("My name is {{ per.name }} and I am {{ per.age }}")
# tm = Template("My name is {{ per['name'] }} and I am {{ per['age'] }}")


data = '''
{% raw %}
His name is {{ name }}
{% endraw %}
'''

tm = Template(data)
msg = tm.render(name='Peter')

print(msg)

data = '<a>Today is a sunny day</a>'

tm = Template("{{ data | e}}")
msg = tm.render(data=data)

print(msg)
print(escape(data))

persons = [
    {'name': 'Andrej', 'age': 34}, 
    {'name': 'Mark', 'age': 17}, 
    {'name': 'Thomas', 'age': 44}, 
    {'name': 'Lucy', 'age': 14}, 
    {'name': 'Robert', 'age': 23}, 
    {'name': 'Dragomir', 'age': 54}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('showpersons.txt')

output = template.render(persons=persons)
print(output)

persons = [
    {'name': 'Andrej', 'age': 34}, 
    {'name': 'Mark', 'age': 17}, 
    {'name': 'Thomas', 'age': 44}, 
    {'name': 'Lucy', 'age': 14}, 
    {'name': 'Robert', 'age': 23}, 
    {'name': 'Dragomir', 'age': 54}
]

persons = [
    {'name': 'Andrej', 'age': 34}, 
    {'name': 'Mark', 'age': 17}, 
    {'name': 'Thomas', 'age': 44}, 
    {'name': 'Lucy', 'age': 14}, 
    {'name': 'Robert', 'age': 23}, 
    {'name': 'Dragomir', 'age': 54}, 
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True

template = env.get_template('showminors.txt')

output = template.render(persons=persons)
print(output)