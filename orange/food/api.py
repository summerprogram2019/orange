import urllib.request
import json
import xml.etree.ElementTree as ET
import os
import pint

# get wolfram api key from environment variable
WOLFRAM_API_KEY = os.environ['WOLFRAM_API_KEY']

ureg = pint.UnitRegistry()

# lookup table from database name to wolfram alpha api
lookup = {
    'calcium': ('calcium', ureg.mg),
    'calories': ('total calories', ),
    'fat': ('total fat', ),
    'sat_fat': ('saturated fat', ),
    'sodium': ('sodium', ),
    'carbs': ('total carbohydrates', ),
    'fibre': ('dietary fiber', ),
    'protein': ('protein', ),
    'vitamin_a': ('vitamin A', ),
    'vitamin_b12': ('vitamin B12', ),
    'vitamin_b6': ('vitamin B6', ),
    'vitamin_c': ('vitamin C', ),
    'vitamin_d': ('vitamin D', ),
    'vitamin_e': ('vitamin E', ),
    'niacin': ('niacin', ),
    'thiamin': ('thiamin', ),
    'phosphorus': ('phosphorus', ),
    'zinc': ('zinc', ),
    'magnesium': ('magnesium', ),
    'folate': ('folate', ),
    'riboflavin': ('riboflavin', ),
    'vitamin_b5': ('panto acid', ),
    'potassium': ('potassium', ),
    'iron': ('iron', ),
    'copper': ('copper', ),
}


# returns nutrients dictionary from a given food name (string) OR null if the search failed
# i.e. get_nutrients('tofu') returns {'vitamin D': '133 IU', 'calcium': '165 mg', 'protein': '8.1 g', 'vitamin E': '2.5 mg', 'phosphorus': '124 mg', 'copper': '197 µg', 'iron': '1.6 mg', 'magnesium': '33 mg', 'total fat': '5.1 g', 'folate': '22 µg', 'zinc': '814 µg', 'thiamin': '69 µg', 'saturated fat': '750 mg', 'total calories': '86 Cal', 'vitamin B12': '0.17 µg', 'vitamin A': '140 IU', 'potassium': '115 mg', 'dietary fiber': '856 mg', 'vitamin B6': '35 µg', 'riboflavin': '37 µg', 'sodium': '22 mg', 'panto acid': '132 µg', 'niacin': '214 µg', 'total carbohydrates': '2.9 g', 'vitamin C': '93 µg'}
def get_nutrients(food_name):
    # request URL. Gets all nutrition information (only from the cell DailyValuesRanking)
    request_url = f'https://api.wolframalpha.com/v2/query?input={food_name}+nutrients&format=plaintext&output=xml&appid={WOLFRAM_API_KEY}&podstate=DailyValuesRanking:ExpandedFoodData__More&podstate=DailyValuesRanking:ExpandedFoodData__More&includepodid=DailyValuesRanking:ExpandedFoodData'

    try:
        page = urllib.request.urlopen(request_url)
        result = page.read()

        # parse xml
        root = ET.fromstring(result)

        # find the plaintext of the pod of interest
        text = root.find('pod').find('subpod').find('plaintext').text

        # convert wolfram alpha table into a dict with keys of nutrients and values of quantity 
        return dict([tuple(x.split(' | ')[:2]) for x in text.split('\n')[1:-1]])

    except Exception as e:
        return None

# sample response from server
pizza = {'sodium': '788 mg', 'saturated fat': '6.3 g', 'protein': '16 g', 'phosphorus': '284 mg', 'total fat': '17 g', 'calcium': '228 mg', 'thiamin': '320 µg', 'riboflavin': '328 µg', 'total calories': '384 Cal', 'vitamin B12': '0.97 µg', 'folate': '63 µg', 'niacin': '3.1 mg', 'zinc': '2.2 mg', 'iron': '2.6 mg', 'copper': '271 µg', 'dietary fiber': '3.2 g', 'total carbohydrates': '40 g', 'magnesium': '35 mg', 'vitamin B6': '158 µg', 'vitamin A': '327 IU', 'potassium': '258 mg', 'cholesterol': '22 mg', 'vitamin E': '1.2 mg', 'vitamin C': '3.5 mg', 'panto acid': '424 µg'}
