'use strict';
/** 
  * controllers used for the dashboard
*/
app.controller('viewRecordsCtrl', ["$scope", function ($scope) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.recordSearch   = '';     // set the default search/filter term

	// create the list of patient records
	$scope.records = [
	{ name: 'Cordero, Jacinto', recordID: '123', status: 'Active', lastUpdated: '20 February 2018' },
	{ name: 'Melendez, Teófilo', recordID: '456', status: 'Inactive' , lastUpdated: '3 August 2016'},
	{ name: 'Reyes, Adelaida', recordID: '789', status: 'Active', lastUpdated: '15 December 2017' },
	{ name: 'González, Rigoberta', recordID: '321', status: 'Inactive', lastUpdated: '9 May 2017' }
	];

	// getPatientRecord() Function Definition
	$scope.getPatientRecord = function(recordID) {

		console.log('Record Number: ' + recordID);
	}

}]);

