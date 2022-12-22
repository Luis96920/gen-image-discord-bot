import json
import requests

from tenacity import (
    retry,
    stop_after_attempt,
    stop_after_delay,
    wait_exponential
)

@retry(
    wait=wait_exponential(min=1, max=10), 
    stop=(stop_after_attempt(5) | stop_after_delay(30)),
def get_voucher(voucher_id):
    return requests.get(f"http://voucher-service:8080/voucher/{voucher_id}").json()


@retry(
    wait=wait_exponential(min=1, max=10), 
    stop=(stop_after_attempt(5) | stop_after_delay(30)),
def get_vouchers(person_id):
    return requests.get(f"http://voucher-service:8080/vouchers?person_id={person_id}").json()


@retry(
    wait=wait_exponential(min=1, max=10), 
    stop=(stop_after_attempt(5) | stop_after_delay(30)),
def redeem_voucher(person_id):
    pass


@retry(
    wait=wait_exponential(min=1, max=10), 
    stop=(stop_after_attempt(5) | stop_after_delay(30)),
def use_credit(voucher_id):
    pass

