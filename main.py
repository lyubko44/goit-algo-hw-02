from queue import Queue
import random

##Створити чергу заявок
queue = Queue()

def generate_request():
    #Створити нову заявку
    new_request = random.randint(1, 1000)
    #Додати заявку до черги
    queue.put(new_request)

def process_request():
    if not queue.empty():
        cur_request = queue.get()
        print("Оброблюємо заявку: " + str(cur_request))
    else:
        print("Черга пуста")       

def main():
    print("Service start to process request. Exit to stop processing")
    while True:
        user_input = input("Enter 'exit' to quit: ")
        if user_input.strip().lower() == 'exit':
            break
        generate_request()
        process_request()

if __name__ == "__main__":
    main()       