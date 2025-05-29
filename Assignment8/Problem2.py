import threading

# Function to calculate the sum of even factors
def evenfactor(number):
    even_sum = sum(i for i in range(1, number + 1) if number % i == 0 and i % 2 == 0)
    print(f"Sum of even factors of {number}: {even_sum}")

# Function to calculate the sum of odd factors
def oddfactor(number):
    odd_sum = sum(i for i in range(1, number + 1) if number % i == 0 and i % 2 != 0)
    print(f"Sum of odd factors of {number}: {odd_sum}")

# Main function
def main():
    number = int(input("Enter an integer: "))

    # Creating threads
    even_thread = threading.Thread(target=evenfactor, args=(number,))
    odd_thread = threading.Thread(target=oddfactor, args=(number,))

    # Starting threads
    even_thread.start()
    odd_thread.start()

    # Waiting for threads to complete
    even_thread.join()
    odd_thread.join()

    # Main thread message
    print("Exit from main")

# Run the program
if __name__ == "__main__":
    main()
