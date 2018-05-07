'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('manageAssistantsCtrl', ["$scope", "$rootScope", "$state", "NgTableParams", function ($scope, $rootScope, $state, NgTableParams) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.assistantSearch   = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
		$state.go('login.signin');
	}

	if($rootScope.isLoggedIn == true) {
		if($rootScope.currentUser.role == 'assistant' || $rootScope.currentUser.role == 'patient') {
			$state.go('app.home');
		}
	}

    // Assistant that is being managed
    $rootScope.chosenAssistant = "";

	// create the list of assistants
	$scope.assistants = [
	{ name: 'Castillo, Francisco', employeeID: '1', status: 'Active' },
	{ name: 'Méndez, Benzeno', employeeID: '2', status: 'Inactive' },
	{ name: 'Hernández, Santa', employeeID: '3', status: 'Active' },
	{ name: 'Suárez, Roberto', employeeID: '4', status: 'Inactive' },
	{ name: 'Castillo, Francisco', employeeID: '11', status: 'Active' },
	{ name: 'Méndez, Benzeno', employeeID: '21', status: 'Inactive' },
	{ name: 'Hernández, Santa', employeeID: '31', status: 'Active' },
	{ name: 'Suárez, Roberto', employeeID: '41', status: 'Inactive' },
	{ name: 'Castillo, Francisco', employeeID: '13', status: 'Active' },
	{ name: 'Méndez, Benzeno', employeeID: '23', status: 'Inactive' },
	{ name: 'Hernández, Santa', employeeID: '33', status: 'Active' },
	{ name: 'Suárez, Roberto', employeeID: '43', status: 'Inactive' },
	{ name: 'Castillo, Francisco', employeeID: '12', status: 'Active' },
	{ name: 'Méndez, Benzeno', employeeID: '22', status: 'Inactive' },
	{ name: 'Hernández, Santa', employeeID: '32', status: 'Active' },
	{ name: 'Suárez, Roberto', employeeID: '42', status: 'Inactive' }
	];

	$scope.getAssistantProfile = function(button, employeeID) {

		$rootScope.chosenAssistant = employeeID;

		if(button == 'view') {
			$state.go('app.users.manage_users.manage_assistants.view_profile');
		}

		else if(button == 'edit') {
			$state.go('app.users.manage_users.manage_assistants.edit_profile');
		}
	}

	// Declaration of table parameters
	$scope.tableParams = new NgTableParams({
        page: 1, // show first page
        count: 5, // count per page
        // initial sort order
        sorting: {
        	name: "asc"
        }
    }, {
    		// Array with information to display in table ($data in HTML)
            total: $scope.assistants.length, // length of data
            dataset: $scope.assistants
        });
}]);