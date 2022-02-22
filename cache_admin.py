import json
import os 

class cache_admin:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value  = value

    def cache_utilization(self):
        with open('cache.json') as cj:
            data = json.load(cj)
            cj.close()
        return data

    def cache_add(self):  
        with open('cache.json','r+') as cj:     
            data = json.load(cj)
            cj.close()
        data[self.key]= self.value
        with open('cache.json','w') as cj:
            json.dump(data, cj)
            cj.close()                 

    def cache_write(self):
        with open("cache.json", "w") as cj:
            json.dump({self.key:self.value}, cj)  

    def del_cache(self):
        os.remove('cache.json')

    def cache_workflow(self):
        try:
            data = self.cache_utilization()
            if self.key in data:
                print(data[self.key])
            else:
                pass
            self.cache_add()
        except:
            self.cache_write()

    

            
