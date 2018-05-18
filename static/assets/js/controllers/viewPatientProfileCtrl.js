'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('viewPatientProfileCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

  	/* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}
    //Logged in
  	else {
  		if($rootScope.currentUser.role == 'Patient') {
      		$state.go('app.home');
      	}
    }

    if ($rootScope.currentUser) {
      if($rootScope.currentUser.role == 'Doctor')
      {
        /* HTTP GET Request: getPatientByID() */
        /* Get patient personal information */
        $http.get('/Doctor/eCSP/Patient/PersonalInformation?patientid=' + $rootScope.chosenPatient + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
        .then(function success(response) {

          $scope.thisPatient = response.data.Patient;
          console.log($scope.thisPatient);

        }, function error(response) { });
      }

      else
      {
        /* HTTP GET Request: getPatientByID() */
        /* Get patient personal information */
        $http.get('/Assistant/eCSP/Patient/PersonalInformation?patientid=' + $rootScope.chosenPatient + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
        .then(function success(response) {

          $scope.thisPatient = response.data.Patient;
          console.log($scope.thisPatient);

        }, function error(response) { });
      }
    }

  }]);

