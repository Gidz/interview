class Services:
    #The standard set of services
    available_services = {'strava': ["SRT", "CVT", "Perkiomen"], 'rwgps' :["CVT", "Perkiomen", "Welsh Mountain"], 'komoot' : ["SRT", "Welsh Mountain", "Oaks to Philly"]}

    def get_service(self, service_name):
	'''
    Given a service name as a string, returns the routes associated with this service.
    '''
        return self.available_services[service_name]

    def get_all_service_names(self):
    '''
    A helper function to just return the names of all the available services.
    '''
        return self.available_services.keys()



def main():
    print("All routes:")
    print("Unique routes:")
    print("For user 42:")
    print("For user 42 services [\"komoot\",\"rwgps\"]:")
    

if __name__=="__main__":
    main()
