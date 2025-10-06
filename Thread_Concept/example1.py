# thread--parallel execution

# without thread
'''sq = []
cu = []


def square(thread_name,endpoint,delay):
    print(f"thread_name={thread_name}")
    for a in range(1,endpoint+1):
        sq.append(a**2)
        time.sleep(delay)
        print(f"sq list={sq}")


def cube(thread_name,endpoint,delay):
    print(f"thread_name={thread_name}")
    for a in range(1,endpoint+1):
        cu.append(a**3)
        time.sleep(delay)
        print(f"cu list={cu}")


square('thread1',20,5)
print("-----------------------")
cube('thread2',20,5)


import _thread
import time

sq = []
cu = []


def square(thread_name,endpoint,delay):
    print(f"thread_name={thread_name}")
    for a in range(1,endpoint+1):
        sq.append(a**2)
        time.sleep(delay)
        print(f"sq list={sq}")


def cube(thread_name,endpoint,delay):
    print(f"thread_name={thread_name}")
    for a in range(1,endpoint+1):
        cu.append(a**3)
        time.sleep(delay)
        print(f"cu list={cu}")
        
try:
    _thread.start_new_thread(square,('thread1',20,1))
    _thread.start_new_thread(cube,('thread2',20,2))
    # _thread.start_new_thread(square,('thread3',50,1))
    
    
except:
    print("unable to start")


while(1):
    pass


import threading
import time


def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)


def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(1)

# Create threads


number_thread = threading.Thread(target=print_numbers)
letter_thread = threading.Thread(target=print_letters)

# Start threads
number_thread.start()
letter_thread.start()

# Wait for both threads to complete
number_thread.join()
letter_thread.join()
print("Done with both tasks")

'''

import threading
import time


class BankAccount:
    def _init_(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount, name):
        with self.lock:
            print(f"{name} depositing {amount}...")
            local_balance = self.balance
            time.sleep(0.5)  # Simulate processing time
            local_balance += amount
            self.balance = local_balance
            print(f"{name} deposit complete. New balance: {self.balance}")

    def withdraw(self, amount, name):
        with self.lock:
            print(f"{name} withdrawing {amount}...")
            if self.balance >= amount:
                local_balance = self.balance
                time.sleep(0.5)  # Simulate processing time
                local_balance -= amount
                self.balance = local_balance
                print(f"{name} withdrawal complete. New balance: {self.balance}")
            else:
                print(f"{name} withdrawal failed. Insufficient funds.")


def customer_actions(account, name):
    account.deposit(100, name)
    account.withdraw(50, name)


if __name__ == "__main__":
    account = BankAccount(200)

# Create threads (customers)
t1 = threading.Thread(target=customer_actions, args=(account, "Alice"))
t2 = threading.Thread(target=customer_actions, args=(account, "Bob"))

# Start threads
t1.start()
t2.start()

# Wait for both to finish
t1.join()
t2.join()

print(f"Final account balance: {account.balance}")





