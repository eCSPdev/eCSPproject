'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('managePatientsCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

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
	{ name: 'Cordero, Jacinto', record: '123', status: 'Active' },
	{ name: 'Melendez, Teófilo', record: '456', status: 'Inactive' },
	{ name: 'Reyes, Adelaida', record: '789', status: 'Active' },
	{ name: 'González, Rigoberta', record: '321', status: 'Inactive' }
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


}]);

