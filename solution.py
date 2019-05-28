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


    def get_user_service(self, user_id, service):
        '''
        Takes in user id and service name as strings and returns the routes appropriately.
        Even though it wasn't mentioned in the problem description, I've noticed that in the output pattern
        for user services follows this:
        
        > Append user_id before the stop name for strava
        > Append user_id after the stop name for rwgps
        > Append user_id before and after the stop name for komoot
        
        '''
        if service =="strava":
            output = []
            #Iterate over the checkpoints in the service and append the user id before the checkpoint
            for checkpoint in self.available_services[service]:
                output.append(user_id + checkpoint)
            return output
        elif service == "rwgps":
            output = []
            #Iterate over the checkpoints in the service and append the user id after the checkpoint
            for checkpoint in self.available_services[service]:
                output.append(checkpoint + user_id)
            return output
        elif service == "komoot":
            output = []
            #Iterate over the checkpoints in the service and append the user id before and after the checkpoint
            for checkpoint in self.available_services[service]:
                output.append(user_id+checkpoint + user_id)
            return output

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

    def get_user_routes_by_service(self, user_id, services_list):
        '''
        Return all the user routes by service
        '''
        user_routes = []
        #Iterate over the services list which is provided as input
        for service in services_list:
            #Use the helper functions to append to user routes
            user_routes.extend(self.services.get_user_service(user_id, service))
        return user_routes



def main():
    #Create an object of helper class. We use this object to print the required output.
    helper = Helper()

    #Output
    print("All routes:", helper.get_all_routes())
    print("Unique routes:")
    print("For user 42:")
    print("For user 42 services [\"komoot\",\"rwgps\"]:", helper.get_user_routes_by_service("42", ["komoot","rwgps"]))
    

#If this program is being run from command line directly, execute the main method.
#Also, the entry point of the program.
if __name__=="__main__":
    main()
