'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('patientConsultationsCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

  	/* Redirect user to login page if he or she is not logged in correctly */
  	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}

  	if($rootScope.isLoggedIn == true) {
  		if($rootScope.currentUser.role == 'patient') {
      		$state.go('app.home');
      	}
    }

	$scope.sortType     = 'consultationDate'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.consultationSearch   = '';     // set the default search/filter term

	// create the list of patient consultations
	$scope.consultations = [
	{ consultationDate: 'December 2016', lastUpdated: '17 December 2016', updatedBy: 'Cordero, Jacinto' },
	{ consultationDate: 'May 2017', lastUpdated: '25 June 2017', updatedBy: 'Talavera, Dr. Fulgencio' },
	{ consultationDate: 'October 2017', lastUpdated: '31 October 2016', updatedBy: 'Reyes, Adelaida' },
	{ consultationDate: 'April 2018', lastUpdated: '21 April 2018', updatedBy: 'Cordero, Jacinto' }
	];

	$rootScope.currentRecord = { };

	// getPatientConsultation() Function Definition
	$scope.getPatientConsultation = function(consultationDate) {

		$rootScope.consultationDate = consultationDate;
		console.log('Month of Consultation: ' + consultationDate);
		$state.go("app.users.view_records.patient_consultations.consultation_details");
	}
}]);

