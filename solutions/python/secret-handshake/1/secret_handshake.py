def commands(binary_str):
    task_list = ["wink","double blink","close your eyes","jump","Reverse"]
    output_task = []
    for binary, task in zip(reversed(binary_str),task_list):
        if task == "Reverse":
            if int(binary):
                output_task.reverse()
            return output_task
        if int(binary):
            output_task.append(task)

