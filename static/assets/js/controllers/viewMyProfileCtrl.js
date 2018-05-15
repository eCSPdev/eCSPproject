'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('viewMyProfileCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

  	/* Redirect user to login page if he or she is not logged in correctly */
  	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}

    if($rootScope.currentUser.role == 'Doctor')
    {

      console.log($scope.thisUser);

      /* HTTP GET Request: getDoctorByID() */
      /* Get doctor personal information */
      $http.get('/Doctor/eCSP/PersonalInformation?doctorid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
      .then(function success(response) {

        $scope.thisUser = response.data.Doctor;
        console.log('GET');
        console.log($scope.thisUser);

      }, function error(response) { });
    }

    else if($rootScope.currentUser.role == 'Assistant')
    {
      /* HTTP GET Request: getAssistantByID() */
      /* Get assistant personal information */
      $http.get('/Assistant/eCSP/PersonalInformation?assistantid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
      .then(function success(response) {

        $scope.thisUser = response.data.Assistant;

      }, function error(response) { });
    }

    else 
    {
      /* HTTP GET Request: getPatientByID() */
      /* Get patient personal information */
      $http.get('/Patient/eCSP/PersonalInformation?patientid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
      .then(function success(response) {

        $scope.thisUser = response.data.Patient;

      }, function error(response) { });
    }

  }]);