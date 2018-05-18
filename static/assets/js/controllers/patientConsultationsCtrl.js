'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('patientConsultationsCtrl', ["$scope", "$rootScope", "$state", "$http", "NgTableParams", function ($scope, $rootScope, $state, $http, NgTableParams) {

  	/* Redirect user to login page if he or she is not logged in correctly */
  	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}

  	// if($rootScope.isLoggedIn == true) {
  	// 	if($rootScope.currentUser.role == 'Patient') {
   //    		$state.go('app.home');
   //    	}
   //  }

	$scope.sortType     = 'consultationDate'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.consultationSearch   = '';     // set the default search/filter term

	//Esto es pa que me redireccione para la pagina de files cuando se suba un file
	if($rootScope.uploaded && $rootScope.uploaded.bool == true) {
		// console.log($rootScope.uploaded)
		$rootScope.uploaded.bool = false;
		$state.go("app.users.view_records.patient_consultations.consultation_details");
	}


	function convertMonth(monthNumber) {
		var months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
		return months[monthNumber];
	}


	if ($rootScope.currentUser) {
		if($rootScope.currentUser.role == 'Doctor') {
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
			function error(response) {

				//Te redirecciono pa la pagina de files ya que el paciente no tiene files, de esta manera pueden subir files
				$state.go("app.users.view_records.patient_consultations.consultation_details");

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

		else if($rootScope.currentUser.role == 'Assistant') {
			$http.get('/Assistant/eCSP/Patient/Files/Dates?patientid=' + $rootScope.chosenRecord.patientID) 
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
			function error(response) {

				//Te redirecciono pa la pagina de files ya que el paciente no tiene files, de esta manera pueden subir files
				$state.go("app.users.view_records.patient_consultations.consultation_details");

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

		else {

			$http.get('/Patient/eCSP/Files/Dates?patientid=' + $rootScope.currentUser.userid) 
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
			function error(response) {

				//Te redirecciono pa la pagina de files ya que el paciente no tiene files, de esta manera pueden subir files
				$state.go("app.users.view_records.patient_consultations.consultation_details");

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

	// getPatientConsultation() Function Definition
	$scope.getPatientConsultation = function(month, year) {

		$rootScope.consultationDate.month = month;
		$rootScope.consultationDate.year = year;
		// console.log('Month of Consultation: ' + consultationDate);
		$state.go("app.users.view_records.patient_consultations.consultation_details");
	}
}]);

