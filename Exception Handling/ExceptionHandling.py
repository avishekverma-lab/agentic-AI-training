class InsufficientFundsError(Exception):
    """Custom exception for bank account withdrawals."""
    pass

def bank_withdrawal(balance, amount):
    try:
        print(f"--- Transaction Started ---")
        
        # 1. Potential ValueError if input isn't a number
        amount = float(amount)
        
        # 2. Logic check: Custom Exception
        if amount > balance:
            raise InsufficientFundsError(f"Attempted to withdraw ${amount}, but balance is only ${balance}.")
        
        # 3. Potential ZeroDivisionError (demonstration purposes)
        if amount == 0:
            result = 10 / 0 

        balance -= amount
        
    except ValueError:
        print("Error: Please enter a valid numerical amount.")
    except InsufficientFundsError as e:
        print(f"Transaction Denied: {e}")
    except ZeroDivisionError:
        print("Error: You cannot perform operations with zero here.")
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")
    else:
        # This block runs only if no exception was raised in the 'try' block
        print(f"Success! New balance: ${balance}")
    finally:
        # This block runs no matter what (even if the program crashes or returns)
        print("--- Transaction Logged & Connection Closed ---")
        print("\n")

# Testing various scenarios
bank_withdrawal(500, 100)      # Scenario: Success
bank_withdrawal(500, "abc")    # Scenario: Invalid Input (ValueError)
bank_withdrawal(500, 1000)     # Scenario: Custom Error (InsufficientFundsError)
bank_withdrawal(500, 0)        # Scenario: Built-in Error (ZeroDivisionError)