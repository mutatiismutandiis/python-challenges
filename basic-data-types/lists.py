def perform_print():
    print(list_to_print)

def perform_insert(command):
    position = int(command[1])
    value_to_insert = int(command[2])
    list_to_print.insert(position, value_to_insert)

def perform_remove(command):
    value_to_delete = int(command[1])
    list_to_print.remove(value_to_delete)

def perform_append(command):
    value_to_add = int(command[1])
    list_to_print.append(value_to_add)

def perform_sort():
    list_to_print.sort()

def perform_reverse():
    list_to_print.reverse()

def perform_pop():
    list_to_print.pop()

commands_dict = {
    "print": perform_print,
    "insert": perform_insert,
    "remove": perform_remove,
    "append": perform_append,
    "sort": perform_sort,
    "reverse": perform_reverse,
    "pop": perform_pop
} 

if __name__ == '__main__':
    N = int(input())
    list_to_print = []

    for _ in range(N):
        command = input().split()
        command_name = command[0]
        if command_name in commands_dict:
            if len(command) > 1:
                commands_dict[command_name](command)
            else:
                commands_dict[command_name]()
        else:
            print("Invalid command:", command_name)
    
            