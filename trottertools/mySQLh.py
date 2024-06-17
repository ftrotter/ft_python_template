"""
mySQLh.py 
A set of SQL helper functions, that is compatible with querpy
This one is for mysql
"""

from querpy import Query


class SQLh(object):

    @staticmethod
    def runDictOfQuerys(query_dict,is_just_print = False,is_ignore_exception = False):
        #This is just a wrapper for runQuerys
        SQLh.runQuerys(query_dict,is_just_print,is_ignore_exception)

    @staticmethod
    def runListOfQuerys(query_list,is_just_print = False, is_ignore_exception = False):
        #This is just a wrapper for runQuerys
        SQLh.runQuerys(query_list,is_just_print,is_ignore_exception)

    @staticmethod
    def runQuerys(these_queries,is_just_print = False, is_ignore_exception = False):
        """
        Runs a dictoriary or list of queries against the spark SQL engine
        
        Arguments:
        these_queries -- a dictionary or a list of queries to run
        is_just_print -- will print the SQL instead of running it if True
        is_ignore_exception -- will prevent crashing due to SQL error if True
        
        """
        #this simple helper loops over a list of queries, prints them and shows the results
        #if you just want the loop to run the queries, then set is_just_print to true
        #This same function works on dictionaries too!! Should rename!!!
        #

        is_first_run = True

        #We want to have only one code.. so we are going to convert all the list into a dict. 
        if isinstance(these_queries, list):
            new_dict = {}
            i = 0
            for this_sql in these_queries:
                i = i+1
                new_dict[i] = this_sql
            #finally reset these_queries to the new dictionary
            these_queries = new_dict

        
        #run this code against a series of dictionaries. First, make sure they are dictionaries.
        if isinstance(these_queries, dict):
            for this_label, this_sql in these_queries.items():
                print(this_label)
                print(this_sql)
                print("\n")
                if is_just_print:
                    #we do nothing, we have already printed
                    print('#not running sql')
                else:
                    if(is_first_run): 
                        # perhaps we connect to database here?

                    print('running SQL command')
                    try:
                        #Todo mysql connection
                        pass
                    except Exception as error:
                        #no matter what, we print the error!!
                        print(f"SQLh.runQuerys: Error in the SQL loop: \n", error)
                        if not is_ignore_exception:
                            #The user wants this error to stop the script execution
                            #So we just raise the error again
                            raise
                        else:
                            print("SQLh.runQuerys: is_ignore_exception is True. So we are continuing despite this error.")

    
        else:
            #We have been passed something other than a list!! 
            #That is fatal! 
            print(these_queries)
            raise Exception("The above was passed to SQLh.runListOfQueries but it is not a list or dict of queries!!!")



