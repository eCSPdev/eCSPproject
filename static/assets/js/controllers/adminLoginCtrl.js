'use strict';
/** 
  * Controller for Admin (Doctor and Assistant) login page
  */
  app.controller('adminLoginCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

  	$scope.credentials = {};

  	/* Token to determine if a user is logged in */
  	$rootScope.isLoggedIn = false;

    /* Variable used to store username, token, and role of logged in user */
    $rootScope.currentUser = {};

    /* Function to validate Admin login information */
    $scope.validateLogin = function(username, password, role) {
      if(role == 'doctor') {
        /* HTTP POST Request: DAlogin() */
        /* Doctor login */
        $http.get('/Doctor/eCSP/Login?username=' + username + '&pssword=' + password)
        .then(function success(response) {

          $rootScope.currentUser.username = response.data.Doctor.username;
          $rootScope.currentUser.token = response.data.Doctor.token;
          $rootScope.currentUser.role = response.data.Doctor.rle;
          $rootScope.currentUser.userid = response.data.Doctor.doctorid;

          $rootScope.currentUser.firstname = response.data.Doctor.firstname;
          $rootScope.currentUser.middlename = response.data.Doctor.middlename;
          $rootScope.currentUser.lastname = response.data.Doctor.lastname;

          $rootScope.isLoggedIn = true;

          // Redirect to homepage
          $state.go('app.home');

        }, function error(response) {
          alert('Invalid username or password. Please try again.');
          $scope.credentials.password = '';
        });
      }

      else {
        /* HTTP POST Request: DAlogin*/
        /* Assistant login */
        $http.get('/Assistant/eCSP/Login?username=' + username + '&pssword=' + password)
        .then(function success(response) {

          $rootScope.currentUser.username = response.data.Assistant.username;
          $rootScope.currentUser.token = response.data.Assistant.token;
          $rootScope.currentUser.role = response.data.Assistant.rle;
          $rootScope.currentUser.userid = response.data.Assistant.assistantid;

          $rootScope.currentUser.firstname = response.data.Assistant.firstname;
          $rootScope.currentUser.middlename = response.data.Assistant.middlename;
          $rootScope.currentUser.lastname = response.data.Assistant.lastname;

          $rootScope.isLoggedIn = true;

          // Redirect to homepage
          $state.go('app.home');

        }, function error(response) {
          alert('Invalid username or password. Please try again.');
          $scope.credentials.password = '';
        });
      }
 };
}]);

