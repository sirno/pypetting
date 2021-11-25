"""Send a message."""

import argparse
import requests


def send_message(msg: str, url: str):
    """Send message from worklist."""
    return (f'B;Execute("pypetting-message-service {url} {msg}",0,"",2);').encode()


def message_service():
    """Message helper tool."""
    parser = argparse.ArgumentParser(description="Send messages to slack webhook.")
    parser.add_argument("url", type=str)
    parser.add_argument("msg", type=str, nargs="+")
    args = parser.parse_args()

    msg = " ".join(args.msg)
    requests.post(args.url, json={"text": msg})
