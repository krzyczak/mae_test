from multiprocessing import Process, Pipe
from config import *

def run_train(data, name, child_conn):
    print(f"{name} is processing data: {data}")
    processed_data = list(map(lambda x: x * 2, data))
    child_conn.send(processed_data)
    child_conn.close()

def start():
    text = f"Module {__name__}: your_path: {your_path} IR RAW is {DIR_RAW}"
    print(text)

    data = [[1,2,3], ["A", "B", "C"]]

    result = []
    index = 0
    processes = []
    parent_connections = []

    for package in data:
        index += 1
        # create a pipe for communication
        parent_conn, child_conn = Pipe()
        parent_connections.append(parent_conn)

        # create the process, pass sentence and connection
        process = Process(target=run_train, args=(package, f"package-{index}", child_conn,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    for parent_connection in parent_connections:
        result.append(parent_connection.recv())

    print("Printing result before returning from mae");
    print(result)
    return result
