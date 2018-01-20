import unittest
from MultipleAthletes import multipleathletes
from AthleteAnalysis import rankathletes, ridgeregression, linearregression, lassoregression, lassolarsregression, bayesianregression
from AthletePerformances import fetchresults



class AthleticsTestCase (unittest.TestCase):
    Athletes = ['276947', '611749', '642991', '596477', '521484', '537630', '377028', '404176', '119822']

    def test_ridge(self):
        #Set an events
        #AthletePageID = 'profile.aspx?athleteid=537630'
        AthletePageID = 'profile.aspx?athleteid=377028'
        Event = '400'
        #Fetch results for an athlete
        Results = fetchresults(Event, AthletePageID)
        #print(Results)
        #Predict next result using ridge
        Prediction = ridgeregression(Results)
        #Check the prediction
        print('Ridge:', Prediction)
        #self.assertEqual(Prediction, '50.0')



    def test_linear(self):
        #Set an events
        #AthletePageID = 'profile.aspx?athleteid=537630'
        AthletePageID = 'profile.aspx?athleteid=377028'
        Event = '400'
        #Fetch results for an athlete
        Results = fetchresults(Event, AthletePageID)
        #Predict next result using ridge
        Prediction = linearregression(Results)
        #Check the prediction
        print('Linear:' , Prediction)
        #self.assertEqual(Prediction, '50.0')

    def test_lasso(self):
        #Set an events
        #AthletePageID = 'profile.aspx?athleteid=537630'
        AthletePageID = 'profile.aspx?athleteid=377028'
        Event = '400'
        #Fetch results for an athlete
        Results = fetchresults(Event, AthletePageID)
        #Predict next result using ridge
        Prediction = lassoregression(Results)
        #Check the prediction
        print('Lasso:' , Prediction)
        #self.assertEqual(Prediction, '50.0')

    def test_lassolars(self):
        #Set an events
        #AthletePageID = 'profile.aspx?athleteid=537630'
        AthletePageID = 'profile.aspx?athleteid=377028'
        Event = '400'
        #Fetch results for an athlete
        Results = fetchresults(Event, AthletePageID)
        #Predict next result using ridge
        Prediction = lassolarsregression(Results)
        #Check the prediction
        print('LassoLars:' , Prediction)
        #self.assertEqual(Prediction, '50.0')


    def test_effectiveness(self):
        Event = '400'
        NoDays = 365*2.5
        #Set an events
        #AthletePageID = 'profile.aspx?athleteid=537630'
        for x in range(0, len(self.Athletes)):
            Predictions = []
            AthletePageID = 'profile.aspx?athleteid=' + self.Athletes[x]
            #Fetch results for an athlete
            Results = fetchresults(Event, AthletePageID, NoDays)
            #print(Results)
            MostRecentResult = Results[0]
            OtherResults = Results[1:]
            #Predict next result using ridge
            Predictions.append(ridgeregression(OtherResults, MostRecentResult['date']))
            Predictions.append(linearregression(OtherResults, MostRecentResult['date']))
            Predictions.append(lassoregression(OtherResults, MostRecentResult['date']))
            Predictions.append(lassolarsregression(OtherResults, MostRecentResult['date']))
            Predictions.append(bayesianregression(OtherResults, MostRecentResult['date']))
            #Check the prediction
            print('Effectiveness:', self.Athletes[x], Predictions, MostRecentResult['performance'], Predictions[0] - MostRecentResult['performance'], MostRecentResult['date'])
            print('Distance from true value:', Predictions[0] - MostRecentResult['performance'], Predictions[4] - MostRecentResult['performance'])
            print()
            #self.assertEqual(Prediction, '50.0')
