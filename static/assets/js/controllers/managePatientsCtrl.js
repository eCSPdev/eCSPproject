'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('managePatientsCtrl', ["$scope", "$rootScope", "$state", "$http", "NgTableParams", function ($scope, $rootScope, $state, $http, NgTableParams) {

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

	// TODO
	// Change variable to rootScope to reflect currently logged in user !
	$scope.username = 'fulgencio.talavera';

	/* HTTP GET Request: getAllPatients() */
    /* Get list of all patients */
    $http.get('/Doctor/eCSP/PatientList?username=%s, token=%s', $scope.username, $scope.token) 
    .then(function success(response) {
    	console.log(response.data);
    	console.log($scope.username);
    	console.log(response.status);
		
		// Populate the list of patients
        $scope.patients = response.data.Patient; 

        // Declaration of table parameters
		$scope.tableParams = new NgTableParams({
        	// Show first page
        	page: 1, 

        	// Count per page
        	count: 10,

        	// initial sort order
        	sorting: {
        		name: "asc"
        	}
    	}, {
    		// Array with information to display in table ($data in HTML)
            // Length of data
            total: $scope.patients.length, 
            dataset: $scope.patients
        });

	}, function error(response) {
		console.log(response);
	});

	$scope.getPatientProfile = function(button, recordID) {

		$rootScope.chosenPatient = recordID;

		if(button == 'view') {
			$state.go('app.users.manage_users.manage_patients.view_profile');
		}

		else if(button == 'edit') {
			$state.go('app.users.manage_users.manage_patients.edit_profile');
		}
	}
}]);