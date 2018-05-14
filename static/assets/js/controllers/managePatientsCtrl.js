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
		if($rootScope.currentUser.role == 'Patient') {
			$state.go('app.home');
		}
	}

	// Patient that is being managed
	$rootScope.chosenPatient = '';

	if($rootScope.currentUser.role == 'Doctor')
	{
		/* HTTP GET Request: getAllPatients() */
		/* Get list of all patients */
		$http.get('/Doctor/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
		.then(function success(response) {

    	// Search bar
    	for(var i = 0; i < response.data.Patient.length; i++) 
    	{
    		if(response.data.Patient[i].status == true)
    		{
    			response.data.Patient[i].status = 'Active';
    		}

    		else
    		{
    			response.data.Patient[i].status = 'Inactive';
    		}
    	}

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

    }, function error(response) { });
	}

	else
	{
		/* HTTP GET Request: getAllPatients() */
		/* Get list of all patients */
		$http.get('/Assistant/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
		.then(function success(response) {

    	// Search bar
    	for(var i = 0; i < response.data.Patient.length; i++) 
    	{
    		if(response.data.Patient[i].status == true)
    		{
    			response.data.Patient[i].status = 'Active';
    		}

    		else
    		{
    			response.data.Patient[i].status = 'Inactive';
    		}
    	}

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

    }, function error(response) { });
	}

	$scope.getPatientProfile = function(button, patientID) {

		$rootScope.chosenPatient = patientID;
		
		if(button == 'view') {
			$state.go('app.users.manage_users.manage_patients.view_profile');
		}

		else if(button == 'edit') {
			$state.go('app.users.manage_users.manage_patients.edit_profile');
		}
	}
}]);