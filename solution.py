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

class Helper:
    '''
    A helper class which can host all the business logic a.k.a required methods to get the output.
    '''
    #Create an object of Services class and get all the service name which might come in handy later
    services = Services()
    service_names = services.get_all_service_names()

    def get_all_routes(self):
        '''
        Return all the possible routes as a list.
        '''
        all_routes = []

        #Iterate over each service
        for service in self.service_names:
            #Add each element to routes list
            all_routes.extend(self.services.get_service(service))

        return all_routes


def main():
    #Create an object of helper class. We use this object to print the required output.
    helper = Helper()

    #Output
    print("All routes:", helper.get_all_routes())
    print("Unique routes:")
    print("For user 42:")
    print("For user 42 services [\"komoot\",\"rwgps\"]:")
    

#If this program is being run from command line directly, execute the main method.
#Also, the entry point of the program.
if __name__=="__main__":
    main()
