class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, samples, new_monster):
        #Add your code here!
        #
        #The first parameter to this method will be a labeled list of samples in the form of
        #a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        #the parameters of a particular monster. The second item in each 2-tuple will be a
        #boolean indicating whether this is an example of this species or not.
        #
        #The second parameter will be a dictionary representing a newly observed monster.
        #
        #Your function should return True or False as a guess as to whether or not this new
        #monster is an instance of the same species as that represented by the list.
        
        model = dict()
        flag = 1

        # building the model
        for sample, tf in samples:
            # for positive example
            if tf == True:
                # set model to be the same as the first positive sample
                if flag == 1:
                    model = sample
                    flag = 0

                # generalize the specific model
                for attribute, val in sample.items():
                    if model[attribute] != val:
                        model[attribute] = 'any'

        # check how the new monster fits the model
        for attribute, val in new_monster.items():
            if model[attribute] != val and model[attribute] != 'any':
                return False
        
        return True