import sys
import argparse
from pytrends.request import TrendReq


def get_inputs():
    parser = argparse.ArgumentParser(description='Google Trends Scraper')
    parser.add_argument('-l', '--language', help='Set trends language search default is es_ES', required=False,
                        default='es_ES')
    parser.add_argument('-f', '--file', help='Path to file, if it\'s not set uses local folder keywords.csv',
                        required=False, default='keywords.csv')
    parser.add_argument('-o', '--output', help='Path to output file, if it\'s not set uses local folder output.csv',
                        required=False, default='output.csv')
    parser.add_argument('-t', '--timeframe', help='Timeframe to search, default is today 5-y', required=False,
                        default='today 5-y')
    parser.add_argument('-tz', '--timezone', help='Set timezone sefault is 360', required=False,
                        default='360')
    parser.add_argument('-g', '--geo', help='Geo to search, default is empty', required=False, default='')
    parser.add_argument('-p', '--gprop', help='Gprop to search, default is empty', required=False, default='')
    parser.add_argument('-d', '--debug', help='Enable request debug', required=False, default=False)

    return parser.parse_args()



def load_keywords(file):
    with open(file, "r") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    inputs = get_inputs()
    print(inputs)
    pytrends = TrendReq(hl=inputs.language, tz=inputs.timezone)
    kw_list = load_keywords(inputs.file)
    pytrends.build_payload(kw_list, cat=0, timeframe=inputs.timeframe, geo=inputs.geo, gprop=inputs.gprop)
    interest_over_time_df = pytrends.interest_over_time()

    print(pytrends.related_topics())
    print(pytrends.related_queries())
    print(interest_over_time_df)


