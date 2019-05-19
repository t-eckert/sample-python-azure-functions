import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("func: decrypt: request received")

    encrypted_name = req.params.get("encrypted_name")
    dummy_key = req.params.get("dummy_key")
    if not encrypted_name or not dummy_key:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            encrypted_name = req_body.get("encrypted_name")
            dummy_key = req_body.get("dummy_key")

    if encrypted_name and dummy_key:
        name = decrypt(int(encrypted_name), int(dummy_key))

        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400,
        )


def decrypt(encrypted_name: int, dummy_key: int) -> str:
    # returns XOR of encrypted_name and dummy_key converted to bytes and decoded
    name_key: int = encrypted_name ^ dummy_key
    return name_key.to_bytes((name_key.bit_length() + 7) // 8, "big").decode()
