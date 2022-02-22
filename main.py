from api_interaction import *
from parse_admin import *


def main():
    
    api = api_interaction('https://www.swapi.tech/api/people')
    api_json = api.api_connect()
    conc_dict = api.create_result_dict(api_json)

    pa = parse_admin()
    args = pa.create_parse()    
    pa.parse_impacts(args, conc_dict)


if __name__ == "__main__":
    main()