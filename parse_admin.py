import argparse
from api_interaction import *
from cache_admin import *
import datetime


class parse_admin:
    
    def create_parse(self):
        # Initiate the parser
        parser = argparse.ArgumentParser()

        # Add long and short argument
        parser.add_argument("action", nargs='?', const='', help="set action", type= str)
        parser.add_argument("query", nargs='?', const='', help="set query", type= str )
        parser.add_argument('--world', nargs='?', const='')
        parser.add_argument('--clean', nargs='?', const='')
        
        # Read arguments from the command line
        args = parser.parse_args()
        return args

    def parse_impacts(self, args, conc_dict):
        name_list = conc_dict['name']
        name_list = list(map(lambda x: x.lower(), name_list))

        if args.action == 'search':            
            if args.query!='':
                found = False

                #venv problem check
                if args.query[-1]=="'" and args.query[0]=="'":
                    args.query = args.query[1:-1]
                print(args.query)
                for i in range(len(name_list)):    
                    if str(args.query.lower()) in name_list[i]:
                        found = True
                        properties= api_interaction(conc_dict['url'][i]).api_connect()['result']['properties']
                        print('Name: {}\nHeight: {}\nMass: {}\nBirth Year: {}\n'.format(properties['name'], properties['height'], properties['mass'], properties['birth_year'])) 
                        if args.world=='':
                            world_properties = api_interaction(properties['homeworld']).api_connect()['result']['properties']
                            print('Homeworld\n---------\nName: {0}\nPopulation: {1}\n'.format(world_properties['name'], world_properties['population']))
                            days = round(int(world_properties['rotation_period'])/24, 2)
                            years = round(int(world_properties['orbital_period'])/365, 2)
                            world = 'On {0} 1 year on earth is {1} years and 1 day {2} days'.format(world_properties['name'], years, days)
                            print(world)
                            # cached
                            key= '{}/{}'.format(properties['name'], world_properties['name'])
                            value= f'catched: {datetime.datetime.now()}'
                            ca= cache_admin(key, value)
                            ca.cache_workflow()
                        else:
                            key= '{}'.format(properties['name'])
                            value= f'catched: {datetime.datetime.now()}'
                            ca= cache_admin(key, value)
                            ca.cache_workflow()                                                     
                        break
                if not found:
                    print('The force is not strong within you')
                else:
                    pass
            else:
                pass
        elif args.action == 'cache' and args.clean=='':
            ca= cache_admin()
            try:
                ca.del_cache()
                print('removed cache')
            except:
                pass
        else:
            pass
                


    