### Getting started

1. Clone and change directory into the repository

2. Run ` python -m pip install -r requirements.txt`

3. Export required environment variables `IP_ADDR` (ip address to host on, either 127.0.0.1 or the ip address of your computer in your local network) and `WOLFRAM_API_KEY`.

4. Change directory into `orange`

5. Create database using ` python manage.py migrate --run-syncdb `

6. Run server at given IP ADDRESS `python manage.py runserver $IP_ADDR:8000`
