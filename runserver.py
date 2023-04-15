"""Code for running server."""
import argparse
import sys
from luxapp import app

if __name__ == '__main__':

    # parse the port argument
    parser = argparse.ArgumentParser(
        prog='runserver.py', allow_abbrev=False, description='The YUAG search application')

    parser.add_argument(
        "port", help="the port at which the server should listen",)

    args = parser.parse_args()
    port = args.port

    # make sure that port is valid
    try:
        port = int(port)
    except Exception as err_mess:
        print("error: port must be an integer 0-65535", file=sys.stderr)
        sys.exit(1)

    # starts the server with the port
    try:
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as err_message:
        print("The server has crashed, error: ", err_message, file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nProcess: Killing Server")
