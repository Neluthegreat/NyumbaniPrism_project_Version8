import random

def simulate_bank_transaction(employee_name, account_number, amount):
    """
    Simulates a transaction with a mock bank API.
    In a real-world scenario, this would involve making an API call to a payment gateway or bank.
    """
    print(f"Initiating payment for {employee_name} to account {account_number} for the amount of {amount}.")

    # Simulate network latency
    import time
    time.sleep(random.uniform(0.5, 2.0))

    # Simulate transaction success/failure
    if random.random() < 0.95:  # 95% success rate
        transaction_id = f"TXN{random.randint(10000000, 99999999)}"
        print(f"Transaction successful. Transaction ID: {transaction_id}")
        return {"status": "success", "transaction_id": transaction_id, "message": "Payment processed successfully."}
    else:
        error_code = random.choice(["INSUFFICIENT_FUNDS", "INVALID_ACCOUNT", "BANK_SERVER_DOWN"])
        print(f"Transaction failed. Error: {error_code}")
        return {"status": "failure", "error_code": error_code, "message": "Payment failed."}
