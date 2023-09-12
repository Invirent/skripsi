# import multiprocessing

# def worker_function(num):
#     print(f"Worker {num} is running.")

# if __name__ == "__main__":
#     num_processes = 4  # Number of processes to create

#     # Create a list to hold process objects
#     processes = []

#     for i in range(num_processes):
#         process = multiprocessing.Process(target=worker_function, args=(i,))
#         processes.append(process)
#         process.start()

#     # Wait for all processes to finish
#     for process in processes:
#         process.join()

#     print("All processes have finished.")


# import multiprocessing
# import time

# def worker_function(num, start_event):
#     print(f"Worker {num} is waiting for the start signal.")
#     start_event.wait()  # Wait for the start signal

#     print(f"Worker {num} is running.")

# if __name__ == "__main__":
#     num_processes = 4
#     start_event = multiprocessing.Event()  # Create an event to signal the start

#     processes = []

#     for i in range(num_processes):
#         process = multiprocessing.Process(target=worker_function, args=(i, start_event))
#         processes.append(process)
#         process.start()

#     print("Press Enter to start the workers...")
#     input()  # Wait for user to press Enter

#     start_event.set()  # Signal the start to worker processes

#     # Wait for all processes to finish
#     for process in processes:
#         process.join()

#     print("All processes have finished.")

import multiprocessing
import time

def worker_function(num):
    print(f"Worker {num} is running.")

if __name__ == "__main__":
    num_processes = 4
    process_interval = 2  # Interval between starting processes in seconds

    processes = []

    for i in range(num_processes):
        process = multiprocessing.Process(target=worker_function, args=(i,))
        processes.append(process)

        # Start the process
        process.start()

        # Wait for the specified interval before starting the next process
        time.sleep(process_interval)

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes have finished.")
