'use strict';
/** 
  * controllers used for the dashboard
*/
app.controller('viewRecordsCtrl', ["$scope", "$rootScope", "$state", "$http", "NgTableParams", function ($scope, $rootScope, $state, $http, NgTableParams) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.recordSearch   = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
   	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }
    //Patient is logged in
  	else {
  		if($rootScope.currentUser.role == 'Patient') {
      		$state.go('app.users.view_records.patient_consultations');
      	}
    }

    if ($rootScope.currentUser) {
	    if($rootScope.currentUser.role == 'Doctor')
		{
			/* HTTP GET Request: getAllPatients() */
			/* Get list of all patients */
			$http.get('/Doctor/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
			.then(function success(response) {

				// console.log(response.data.Patient);

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

	    	}, function error(response) { 

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
		            total: 0, 
		            dataset: ""
		        });

	    	});
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

	    	}, function error(response) {

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
		            total: 0, 
		            dataset: ""
		        });

	    	 });
		}

	}

	$rootScope.chosenRecord = { };

	// getPatientRecord() Function Definition
	$scope.getPatientRecord = function(patientID, recordno, lName, fName, mName) {

		$rootScope.chosenRecord.patientID = patientID;
		$rootScope.chosenRecord.recordno = recordno;
		$rootScope.chosenRecord.lName = lName;
		$rootScope.chosenRecord.fName = fName;
		$rootScope.chosenRecord.mName = mName;
		// console.log('Chosen Record: ' + $rootScope.chosenRecord);
		$state.go("app.users.view_records.patient_consultations");
	}

}]);

