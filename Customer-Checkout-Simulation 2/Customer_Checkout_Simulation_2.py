class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty queue
    
    # Enqueue: Add an element to the rear of the queue
    def enqueue(self, item):
        self.queue.append(item)
    
    # Dequeue: Remove and return the front element of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"
    
    # Is empty: Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

# Simulate the customer checkout process
def checkout_simulation():
    customers = ["Alice", "Bob", "Charlie", "Diana"]
    
    # Create a Queue for customers
    queue = Queue()
    
    # Enqueue all customers
    for customer in customers:
        queue.enqueue(customer)
    
    # Initialize total wait time
    total_wait_time = 0
    time_per_customer = 5  # Each customer is served for 5 minutes
    
    # Serve each customer
    while not queue.is_empty():
        customer = queue.dequeue()
        print(f"Serving {customer}")
        total_wait_time += time_per_customer
    
    # Display the total wait time
    print(f"Total wait time: {total_wait_time} minutes")

# Run the checkout simulation
checkout_simulation()
