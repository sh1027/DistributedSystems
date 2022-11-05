import argparse
import logging
import random
import threading
import time


class Account:
    def __init__(self, balance: int) -> None:
        self.balance = balance
        logging.info(f"Account created. Initial balance: {balance:>6,}")

    def get_balance(self) -> int:
        return self.balance

    def set_balance(self, balance: int) -> None:
        self.balance = balance


def transaction(account: Account, amount: int) -> None:
    logging.debug("Transaction Started.")
    before_balance = account.get_balance()
    time.sleep(random.randint(1, 5))
    after_balance = before_balance + amount
    account.set_balance(after_balance)
    logging.info(
        f"Transaction Completed. | before: {before_balance:>6,} | amount: {amount:>6,} | after: {after_balance:>6,} |"
    )


def transaction_with_lock(account: Account, amount: int, lock: threading.Lock) -> None:
    logging.debug("Transaction Started.")
    with lock:
        before_balance = account.get_balance()
        time.sleep(random.randint(1, 5))
        after_balance = before_balance + amount
        account.set_balance(after_balance)
    logging.info(
        f"Transaction Completed. | before: {before_balance:>6,} | amount: {amount:>6,} | after: {after_balance:>6,} |"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lock", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=logging_level, format="%(threadName)s: %(message)s")

    if args.lock:
        lock = threading.Lock()

    account = Account(1000)
    for i in range(10):
        time.sleep(1)
        amount = random.randint(-100, 100)
        if args.lock:
            t = threading.Thread(
                target=transaction_with_lock,
                name=f"Thread-{i}",
                args=(account, amount, lock),
            )
        else:
            t = threading.Thread(
                target=transaction,
                name=f"Thread-{i}",
                args=(account, amount),
            )
        t.start()
