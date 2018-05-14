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

          console.log(response.data);
          
          $rootScope.currentUser.username = response.data.Patient.username;
          $rootScope.currentUser.token = response.data.Patient.token;
          $rootScope.currentUser.role = response.data.Patient.rle;

          $rootScope.currentUser.firstname = response.data.Patient.firstname;

          $rootScope.isLoggedIn = true;

          // Redirect to homepage
          $state.go('app.home');

        }, function error(response) {
          console.log(response);
          alert('Invalid username or password. Please try again.');
          $scope.credentials.password = '';
        });
 };

}]);

