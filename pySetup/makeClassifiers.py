from sklearn.ensemble import RandomForestClassifier

'''
determine which parameters we want to mess with
    https://www.kaggle.com/forums/f/15/kaggle-forum/t/4092/how-to-tune-rf-parameters-in-practice
    A. M-Try (number of features it tries at each decision point in a tree). Starts at square root of features available, but tweak it up and down by a few (probably no more than 3 in each direction; it seems even 1 or 2 is enough)
    B. Number of folds for cross-validation: 10 is what most people use, but more gives you better accuracy (likely at the cost of compute time). again, returns are pretty rapidly diminishing. 
    C. platt scaling of the results to increase overall accuracy at the cost of outliers (which sounds perfect for an ensemble)
    D. preprocessing the data might help- FUTURE
    E. Principle Component Analysis to decrease dependence between features
    F. Number of trees
    G. Possibly ensemble different random forests together. this is where the creative ensembling comes into play!
    H. Splitting criteria
    I. AdaBoost
    J. Can bump up nodesize as much as possible to decrease training time (split)
        consider doing this first, finding what node size we finally start decreasing accuracy on, then use that node size for the rest of the testing we do, then possibly bumping it down a bit again at the end. 
            https://www.kaggle.com/c/the-analytics-edge-mit-15-071x/forums/t/7890/node-size-in-random-forest
    K. min_samples_leaf- smaller leaf makes you more prone to capturing noise from the training data. Try for at least 50??
        http://www.analyticsvidhya.com/blog/2015/06/tuning-random-forest-model/
    L. random_state: adds reliability. Would be a good one to split on if ensembling different RFs together. 
    M. oob_score: something about intelligent cross-validation. 
    N. allusions to regularization, or what I think they mean- feature selection. 

'''


def makeClassifiers(globalArgs):
    return {
    'clRandomForest': RandomForestClassifier(n_estimators=15, n_jobs=globalArgs['numCPUs'])
    }