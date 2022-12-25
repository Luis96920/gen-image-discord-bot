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
    stop=(stop_after_attempt(5) | stop_after_delay(30)))
def get_voucher(voucher_id):
    response = requests.get(f"http://localhost:8080/voucher/{voucher_id}")
    return response.json()


@retry(
    wait=wait_exponential(min=1, max=10), 
    stop=(stop_after_attempt(5) | stop_after_delay(30)))
def get_vouchers(person_id):
    response = requests.get(f"http://localhost:8080/vouchers?person_id={person_id}")
    return response.json()

def get_credits(person_id):
    vouchers = get_vouchers(person_id)

    if not vouchers:
        return 0
    else:
        return sum(voucher["credits"] for voucher in vouchers)


@retry(
    wait=wait_exponential(min=1, max=10), 
    stop=(stop_after_attempt(5) | stop_after_delay(30)))
def redeem_voucher(voucher_id, person_id):
    payload = {"request_type": "REDEEM_VOUCHER", "person_id": person_id}
    requests.patch(f"http://localhost:8080/vouchers/{voucher_id}", json=payload)


@retry(
    wait=wait_exponential(min=1, max=10), 
    stop=(stop_after_attempt(5) | stop_after_delay(30)))
def subtract_credits(voucher_id, credits=1):
    payload = {"request_type": "SUBTRACT_CREDITS", "credits": credits}
    requests.patch(f"http://localhost:8080/vouchers/{voucher_id}", json=payload)

