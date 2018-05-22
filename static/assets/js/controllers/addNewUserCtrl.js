'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('addNewUserCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
      $state.go('login.signin');
    }
    else {
      if($rootScope.currentUser.role == 'Patient') {
        $state.go('app.home');
      }
    }

    // Set default (non-required) values for new user
    $scope.newUser = {};
    $scope.newUser.registeredby = $rootScope.currentUser.username;
    $scope.newUser.middlename = '';
    $scope.newUser.insurancecompanyname = '';
    $scope.newUser.aptno = '';
    $scope.newUser.st = '';
    $scope.newUser.email = "";
    $scope.newUser.status = true;

    $scope.addUser = function() {

      // Create (INSERT) new patient
      if($scope.newUser.role == 'patient')
      {
        if($rootScope.currentUser.role == 'Doctor') {
          /* HTTP POST Request: insertPatient() */
          /* Create new patient */
          $http.post('/Doctor/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.newUser)
          .then(function success(response) {

            $scope.newUser = response.data;

            $state.go('app.users.manage_users.manage_patients');

          }, function error(response) {
            if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }
          });
        }

        else {
          /* HTTP POST Request: insertPatient() */
          /* Create new patient */
          $http.post('/Assistant/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.newUser) 
          .then(function success(response) {

            $scope.newUser = response.data;

            $state.go('app.users.manage_users.manage_patients');

          }, function error(response) {
              if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }
           });
        }
      }

      // Create (INSERT) new assistant
      else
      {
        /* HTTP POST Request: insertAssistant() */
        /* Create new assistant */
        $http.post('/Doctor/eCSP/AssistantList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.newUser) 
        .then(function success(response) {

          $scope.newUser = response.data;
          $state.go('app.users.manage_users.manage_assistants');

        }, function error(response) {
            if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }
         });
      }

    }

  }]);