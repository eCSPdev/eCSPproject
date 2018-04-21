'use strict';
/** 
  * controllers used for the dashboard
*/
app.controller('manageAssistantsCtrl', ["$scope", function ($scope) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.assistantSearch   = '';     // set the default search/filter term

	// create the list of assistants
	$scope.assistants = [
	{ name: 'Rodríguez, Magali', employeeID: '1', status: 'Active' },
	{ name: 'Méndez, Benzeno', employeeID: '2', status: 'Inactive' },
	{ name: 'Hernández, Santa', employeeID: '3', status: 'Active' },
	{ name: 'Suárez, Roberto', employeeID: '4', status: 'Inactive' }
	];


}]);

