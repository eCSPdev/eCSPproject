'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('managePatientsCtrl', ["$scope", "$rootScope", "$state", "NgTableParams", function ($scope, $rootScope, $state, NgTableParams) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.patientSearch   = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
		$state.go('login.signin');
	}

	
	if($rootScope.isLoggedIn == true) {
		if($rootScope.currentUser.role == 'patient') {
			$state.go('app.home');
		}
	}

	// Patient that is being managed
	$rootScope.chosenPatient = "";

	// create the list of patients
	$scope.patients = [
	{ name: 'Knope, Leslie', record: '123', status: 'Active' },
	{ name: 'Melendez, Teófilo', record: '456', status: 'Inactive' },
	{ name: 'Reyes, Adelaida', record: '789', status: 'Active' },
	{ name: 'González, Rigoberta', record: '321', status: 'Inactive' },
	{ name: 'Knope, Leslie', record: '1233', status: 'Active' },
	{ name: 'Melendez, Teófilo', record: '4563', status: 'Inactive' },
	{ name: 'Reyes, Adelaida', record: '7893', status: 'Active' },
	{ name: 'González, Rigoberta', record: '3213', status: 'Inactive' },
	{ name: 'Knope, Leslie', record: '1231', status: 'Active' },
	{ name: 'Melendez, Teófilo', record: '4561', status: 'Inactive' },
	{ name: 'Reyes, Adelaida', record: '7891', status: 'Active' },
	{ name: 'González, Rigoberta', record: '3214', status: 'Inactive' },
	{ name: 'Knope, Leslie', record: '1234', status: 'Active' },
	{ name: 'Melendez, Teófilo', record: '4564', status: 'Inactive' },
	{ name: 'Reyes, Adelaida', record: '7894', status: 'Active' },
	{ name: 'González, Rigoberta', record: '3212', status: 'Inactive' }
	];

	$scope.getPatientProfile = function(button, recordID) {

		$rootScope.chosenPatient = recordID;

		if(button == 'view') {
			$state.go('app.users.manage_users.manage_patients.view_profile');
		}

		else if(button == 'edit') {
			$state.go('app.users.manage_users.manage_patients.edit_profile');
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
            total: $scope.patients.length, // length of data
            dataset: $scope.patients
        });


}]);

