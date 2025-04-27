import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from SukhPB.startup import *  # Make sure this module exists and is accessible


def run_keep_alive():
    """Minimal HTTP server to prevent Replit sleep."""

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is alive!")

    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()


# Start the keep-alive server in a background thread
Thread(target=run_keep_alive, daemon=True).start()

# Your existing .env setup code
vars = """
APP_ID=
API_HASH=
SUDO_USERS=
START_PIC=
START_MESSAGE=
HELP_PIC=
PING_PIC=
LOG_CHANNEL=
HANDLER=
BOT_TOKEN=
BOT_TOKEN2=
BOT_TOKEN3=
BOT_TOKEN4=
BOT_TOKEN5=
BOT_TOKEN6=
BOT_TOKEN7=
BOT_TOKEN8=
BOT_TOKEN9=
BOT_TOKEN10=
BOT_TOKEN11=
BOT_TOKEN12=
BOT_TOKEN13=
BOT_TOKEN14=
BOT_TOKEN15=
BOT_TOKEN16=
BOT_TOKEN17=
BOT_TOKEN18=
BOT_TOKEN19=
BOT_TOKEN20=
BOT_TOKEN21=
BOT_TOKEN22=
BOT_TOKEN23=
BOT_TOKEN24=
BOT_TOKEN25=
"""

botspam = input("Want to fill vars? If yes type Y/yes else press enter: ")
if botspam.lower() in ["y", "yes"]:
    if not os.path.exists(".env"):
        with open(".env", "w") as y:
            y.write(vars)
        os.system("clear")
        BadmundaStartUP()
    else:
        with open(".env") as f:
            check = f.read()
        print(check)

        def check_again():
            global lines
            with open(".env") as f:
                lines = f.readlines()  # Read the lines properly

        check_again()  # Call the function before using `lines`

        if len(lines) == 35:
            os.remove(".env")  # Proper way to delete the file
            with open(".env", "w") as y:
                y.write(vars)
            os.system("clear")
            BadmundaStartUP()
        else:
            os.system("clear")
            BadmundaStartUP()
else:
    os.system("clear")
    os.system("python3 -m BADMUNDA")
