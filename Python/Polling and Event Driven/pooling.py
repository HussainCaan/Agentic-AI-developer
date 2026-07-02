import time

Hungry = True

while (Hungry):
    with open('test.txt', 'r') as f:
        for line in f:
            if line == 'available':
                print("Food is available, eating now...")
                Hungry = False
                break
    if Hungry:
        print("Food is not available, waiting for 5 seconds...")
        time.sleep(1)