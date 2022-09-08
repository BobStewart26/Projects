from datetime import *
from importlib import resources

class project:
    def __init__(self,name,startdate,enddate):
        self.name = name
        self.startdate = startdate
        self.enddate = enddate
        self.tasks = []

    def addtask(self,task):
        self.tasks.append(task)

class task:
    def __init__(self,name,duration):
        self.name = name
        self.duration = duration
        self.resources = []

    def addresource(self,resource):
        self.resources.append(resource)

class resource:
    def __init__(self,name,skill):
        self.name = name
        self.skill = skill


project = project("AI",date(2022,9,8),date(2023,9,8))
task1 = task("software",100)
resource1 = resource("Bob",'Python')
task1.addresource(resource1)
project.addtask(task1)

task2 = task("Testing",100)
resource2 = resource("Qasim",'Dev-ops')
task1.addresource(resource2)
project.addtask(task2)

task3 = task("Release",50)
resource3 = resource("Nisha",'HR')
task1.addresource(resource3)
project.addtask(task3)


for eachtask in project.tasks:
    print(eachtask.name)
    print(eachtask.duration)
    for eachresource in eachtask.resources:
        print(eachresource.name)
        print(eachresource.skill)