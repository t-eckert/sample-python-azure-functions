import logging
from secrets import token_bytes
from typing import Tuple


import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("func: encrypt: request received")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        # encrypt name
        encrypted_name, dummy_key = encrypt(name)

        response = str({"encrypted_name": encrypted_name, "dummy_key": dummy_key})
        return func.HttpResponse(response)
    else:
        # ask for input if none provided
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400,
        )


def random_key(length: int) -> int:
    # returns length random bytes
    key: bytes = token_bytes(length)
    # convert key to bit string
    return int.from_bytes(key, "big")


def encrypt(name: str) -> Tuple[int, int]:
    # return (encrypted_name, dummy_key); encrypted by one-time pad
    # encode the name to bytes, then to a bit string
    name_as_bytes: bytes = name.encode()
    name_key: int = int.from_bytes(name_as_bytes, "big")

    # generate a dummy key for encryption
    dummy_key: int = random_key(len(name_as_bytes))

    # encrypt by XOR operation
    encrypted_name: int = name_key ^ dummy_key

    return encrypted_name, dummy_key
