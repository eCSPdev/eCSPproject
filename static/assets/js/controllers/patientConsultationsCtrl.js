'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('patientConsultationsCtrl', ["$scope", "$rootScope", "$state", "$http", "NgTableParams", function ($scope, $rootScope, $state, $http, NgTableParams) {

  	/* Redirect user to login page if he or she is not logged in correctly */
  	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}

  	if($rootScope.isLoggedIn == true) {
  		if($rootScope.currentUser.role == 'Patient') {
      		$state.go('app.home');
      	}
    }

	$scope.sortType     = 'consultationDate'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.consultationSearch   = '';     // set the default search/filter term


	function convertMonth(monthNumber) {
		var months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
		return months[monthNumber];
	}

	$http.get('/Doctor/eCSP/Patient/Files/Dates?patientid=' + $rootScope.chosenRecord.patientID) 
		.then(function success(response) {

			for (var i = 0; i < response.data.FilesDates.length; i++) {
				response.data.FilesDates[i].monthName = convertMonth(response.data.FilesDates[i].month);
			}

			// console.log(response.data);

			$scope.consultations = response.data.FilesDates;

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
	            total: $scope.consultations.length, 
	            dataset: $scope.consultations
	        });
		},
			function error(response) {});


	$rootScope.consultationDate = { };

	// getPatientConsultation() Function Definition
	$scope.getPatientConsultation = function(month, year) {

		$rootScope.consultationDate.month = month;
		$rootScope.consultationDate.year = year;
		// console.log('Month of Consultation: ' + consultationDate);
		$state.go("app.users.view_records.patient_consultations.consultation_details");
	}
}]);

