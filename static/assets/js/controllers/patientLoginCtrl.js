'use strict';
/** 
  * Controller for Patient login page
  */
  app.controller('patientLoginCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

  	$scope.credentials = {};

  	/* Token to determine if a user is logged in */
  	$rootScope.isLoggedIn = false;

    /* Variable used to store username, token, and role of logged in user */
    $rootScope.currentUser = {};

  	/* Function to validate Patient login information */
  	$scope.validateLogin = function(username, password) {

      /* HTTP POST Request: DAlogin() */
        /* Doctor login */
        $http.get('/Patient/eCSP/Login?username=' + username + '&pssword=' + password)
        .then(function success(response) {
          
          $rootScope.currentUser.username = response.data.Patient.username;
          $rootScope.currentUser.token = response.data.Patient.token;
          $rootScope.currentUser.role = response.data.Patient.rle;
          $rootScope.currentUser.userid = response.data.Patient.patientid;
          $rootScope.currentUser.recordno = response.data.Patient.recordno;

          $rootScope.currentUser.firstname = response.data.Patient.firstname;
          $rootScope.currentUser.middlename = response.data.Patient.middlename;
          $rootScope.currentUser.lastname = response.data.Patient.lastname;

          $rootScope.isLoggedIn = true;

          // Redirect to homepage
          $state.go('app.home');

        }, function error(response) {
          alert('Invalid username or password. Please try again.');
          $scope.credentials.password = '';
        });
 };

}]);

