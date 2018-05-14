'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('addNewUserCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
      $state.go('login.signin');
    }

    if($rootScope.isLoggedIn == true) {
      if($rootScope.currentUser.role == 'Patient') {
        $state.go('app.home');
      }
    }

    $scope.newUser = { };

    $scope.addUser = function() {
      console.log($scope.newUser);

      if($rootScope.currentUser.role == 'Doctor')
      {

      // Create (INSERT) new patient
      if($scope.newUser.type == 'patient')
      {
        console.log($scope.newUser);

        /* HTTP POST Request: insertPatient() */
        /* Create new patient */
        $http.post('/Doctor/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.newUser) 
        .then(function success(response) {

          $scope.newUser = response.data;

          console.log($scope.newUser);

          $state.go('app.users.manage_users.manage_patients');

        }, function error(response) { });
      }

      else
      {
        console.log($scope.newUser);

        /* HTTP POST Request: insertAssistant() */
        /* Create new assistant */
        $http.post('/Doctor/eCSP/AssistantList', $scope.newUser) 
        .then(function success(response) {

          $scope.newUser = response.data;

          console.log($scope.newUser);

          $state.go('app.users.manage_users.manage_assistants');

        }, function error(response) { });
      }

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

