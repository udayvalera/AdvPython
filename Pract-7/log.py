import logging

# Configure logging
logging.basicConfig(filename='fibonacci.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fibonacci(n):
    logging.info("Starting Fibonacci computation.")

    try:
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        
        if n == 0:
            logging.debug("Fibonacci(0) = 0")
            return 0
        elif n == 1:
            logging.debug("Fibonacci(1) = 1")
            return 1
        
        a, b = 0, 1
        logging.debug(f"Initial values: a={a}, b={b}")

        for i in range(2, n + 1):
            a, b = b, a + b
            logging.debug(f"Fibonacci({i}) = {b}")

        logging.info("Fibonacci computation completed successfully.")
        return b

    except ValueError as e:
        logging.error(f"Error during Fibonacci computation: {e}")
        return str(e)

    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        return "An unexpected error occurred."

def main():
    while True:
        user_input = input("Enter a non-negative integer for Fibonacci computation (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            logging.info("User exited the program.")
            break
        
        try:
            n = int(user_input)
            result = fibonacci(n)
            print(f"Fibonacci({n}) = {result}")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

if __name__ == "__main__":
    main()
