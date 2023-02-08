FILEPATH = "tasks.txt"


def get_tasks(filepath=FILEPATH):
    """ Read a text file and return the tasks
    """

    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FILEPATH):
    """Writes a list of tasks to a text file"""

    with open(filepath, 'w') as file_local:
        file_local.writelines(tasks_arg)

def enumPrint(tasks_arg):
    for index_local, item_local in enumerate(tasks_arg):
        item_local = item_local.strip('\n')
        print(f"{index_local + 1}. {item_local}")


