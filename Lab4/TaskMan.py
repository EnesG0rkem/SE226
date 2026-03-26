taskNumber = int(input("Please enter number of tasks: "))
taskDict = {}
for i in range(0,taskNumber):
    taskName = input("Please enter task name: ")
    print('Please enter number of dependencies for task "',taskName,'": ', end ="")
    numOfDependencies = int(input())
    dependencies = []
    for k in range(0, numOfDependencies):
        print("Please enter depenency ", k+1, " for task ",taskName, " :", end ="")
        dependencies.append(input())
    taskDict[taskName] = dependencies

print('TASK STRUCTURE')
for task in taskDict.keys():
    print(task, "-> ", taskDict.get(task))

print('INITIAL TASKS (no dependencies) :')
initialTask = False
initailTasks = []
for task in taskDict.keys():
    if not taskDict.get(task):
        initialTask = True
        print(task, "-> ",taskDict.get(task))
        initailTasks.append(task)
if not initialTask:
    print('None')

print('EXECUTION ORDER')
taskSet = {}

isCircular = False
for task in initailTasks:
    taskSet.add(task)

for a in taskDict.keys():
    for task in taskDict.keys():
        print(a)
    isCircular = True

if isCircular:
    print('Error: circularity!')