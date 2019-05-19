# Encryption and Decryption

This pair of functions implements a [One-Time Pad](https://en.wikipedia.org/wiki/One-time_pad) to encrypt your name. Calling the `encrypt` HTTP function with a `name` paramter will give you back an `encrypted_name` and `dummy_key` to decrypt it. Calling the `decrypt` function with `encrypted_name` and `dummy_key` parameters will give you back a decrypted name.

## Prerequisites

- [Python 3.6](https://www.python.org/downloads/)
- [Azure Functions Core Tools](https://docs.microsoft.com/bs-latn-ba/azure/azure-functions/functions-run-local#v2)

## Quickstart

Clone the Repository

``` bash
git clone https://github.com/t-eckert/sample-python-azure-functions.git
```

Change directory to `encryption_and_decryption`

``` bash
cd sample-python-azure-functions/encryption_and_decryption/
```

Set the runtime to `python`

``` bash
func settings add FUNCTIONS_WORKER_RUNTIME python
```

Create a virtual environment to run the code in.

Bash

``` bash
python3.6 -m venv .env  
source .env/bin/activate
```

Powershell

``` powershell
py -3.6 -m venv .env
.env\scripts\activate
```

Start the Azure Functions App

``` bash
func host start
```

## Using the App

Once the app is running encrypt the name "Sophia", by going to `http://localhost:7071/api/encrypt?name=Sophia` in a browser. You will get an output resembling:

``` json
{
    "encrypted_name": 133673440856088,
    "dummy_key": 47262719615353
}
```

Decrypt the name by going to `http://localhost:7071/api/decrypt?encrypted_name=133673440856088&dummy_key=47262719615353`. You should get the response:

``` text
Hello Sophia!
```

Try it with your name!