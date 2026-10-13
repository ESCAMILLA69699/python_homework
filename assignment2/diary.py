# ALEXANDER ESCAMILLA
# HW 2

# TASK 1 -- DIARY.PY


import traceback

done = "done for now"
prompt = "What happened today? "

try:
    with open("diary.txt", "a") as file:
        while True:
            userInput = input(prompt)
            file.write(userInput + "\n")

            if userInput == done:
                break
            else:
                prompt = "What else? "

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
