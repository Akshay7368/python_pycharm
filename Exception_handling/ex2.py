accounts = {'Akshay': 2000,'Kumar': 1000,'Jack': 4000,'Peter' : 8000}
print(accounts)


class InsufficientFundError(Exception):
    pass


def Transfer(sender, receiver, amount):
    try:
        if sender not in accounts or receiver not in accounts:
            raise ValueError("Invalid Account because Sender/ Receiver not in accounts")
        if amount <=0:
            raise ValueError("Amount cannot be negative")
        if accounts[sender] < amount:
            raise InsufficientFundError("Sender doesn't have enough money")
        accounts[sender]-= amount
        accounts[receiver]+= amount
        print(f"{amount} has been successfully transferred from {sender} to {receiver}")

    except ValueError:
        print("Invalid Account because Sender/ Receiver not in accounts")

    except InsufficientFundError:
        print("Insufficient balance")

    except Exception:
        print("Transaction Failed")

    else:
        print(f"New balance of {sender} = {accounts[sender]} ")
        print(f"New balance of {receiver} = {accounts[receiver]} ")

    finally:
        print("All transactions are completed")


Transfer('Akshay','Peter', 1000)
# Transfer('Akshay','Peter', 6000)
Transfer('Mani','Peter',900)


