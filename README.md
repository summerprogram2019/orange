![Orange banner](https://raw.githubusercontent.com/summerprogram2019/orange/master/img/banner.png)

# Orange
> 橙功之道. The road to nutrition and health.

This application was made during the Start-Up China Program at the Dalian Neusoft University of Information in the summer of 2019.

Orange is all about making healthy eating even easier. These days everyone can see how much sugar and fat they're eating, but what about all of the important vitamins and minerals that your body needs?

Orange provides all users with the ability to track important nutritional information that often gets overlooked. After tracking your food intake, you can view your daily levels of every nutritional element, ensuring you can have a healthy balanced lifestyle.

Orange makes tracking food even easier with the added food scanning feature. Using our advanced machine learning algorithm, you can take a picture of your food and it will instantly be added to your daily intakes. What makes Orange even more special is it gives users the ability to customise their daily intakes to suit their own special requirements. If your lifestyle or medical background requires any dietary changes, you can easily configure your profile allowing you to see your new nutritional goals.

# Getting started

1. Clone and change directory into the repository
2. Run ` python -m pip install -r requirements.txt`
3. Export required environment variables `IP_ADDR` (ip address to host on, either 127.0.0.1 or the ip address of your computer in your local network) and `WOLFRAM_API_KEY`.
4. Change directory into `orange`
5. Create database using ` python manage.py migrate --run-syncdb `
6. Run server at given IP ADDRESS `python manage.py runserver $IP_ADDR:8000`
