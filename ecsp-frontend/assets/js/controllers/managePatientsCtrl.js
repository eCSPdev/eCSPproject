'use strict';
/** 
  * controllers used for the dashboard
*/
app.controller('managePatientsCtrl', ["$scope", function ($scope) {

	$scope.sortType     = 'record'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.patientSearch   = '';     // set the default search/filter term

	// create the list of patients
	$scope.patients = [
	{ name: 'Cordero, Jacinto', record: '123', status: 'Active' },
	{ name: 'Melendez, Teófilo', record: '456', status: 'Inactive' },
	{ name: 'Reyes, Adelaida', record: '789', status: 'Active' },
	{ name: 'González, Rigoberta', record: '321', status: 'Inactive' }
	];


}]);

