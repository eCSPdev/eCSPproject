'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('editPatientProfileCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModal", function ($scope, $rootScope, $state, $http, $uibModal) {

    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
      $state.go('login.signin');
    }

    $scope.thisPatient = {};

    if ($rootScope.currentUser) {
      if($rootScope.currentUser.role == 'Doctor')
      {
        /* HTTP GET Request: getPatientByID() */
        /* Get patient personal information */
        $http.get('/Doctor/eCSP/Patient/PersonalInformation?patientid=' + $rootScope.chosenPatient + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
        .then(function success(response) {

          delete response.data.Patient.pssword;
          $scope.thisPatient = response.data.Patient;

        }, function error(response) { });
      }

      else
      {
        /* HTTP GET Request: getPatientByID() */
        /* Get patient personal information */
        $http.get('/Assistant/eCSP/Patient/PersonalInformation?patientid=' + $rootScope.chosenPatient + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
        .then(function success(response) {

          delete response.data.Patient.pssword;
          $scope.thisPatient = response.data.Patient;

        }, function error(response) { });
      }
    }

    $scope.thisPatient.patientid = $rootScope.chosenPatient;
    $scope.thisPatient.username = $rootScope.currentUser.username;
    $scope.thisPatient.token = $rootScope.currentUser.token;

  	// open() Function Definition
    $scope.open = function (size) {

      var modalInstance = $uibModal.open({
       templateUrl: 'modal1.html',
       controller: 'ModalInstanceCtrl',
       size: size,
       resolve: { 
        chosenPatient: function() {
          return $scope.thisPatient;
        }
      }
    });

      modalInstance.result.then(function (confirmation) {
       // if(confirmation == true) { }
    });
    };

  }]);

// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$rootScope", "$state", "$http", "chosenPatient", "$uibModalInstance", function ($scope, $rootScope, $state, $http, chosenPatient, $uibModalInstance) {

  // Confirm (OK) button
  $scope.ok = function () {

    if($rootScope.currentUser.role == 'Doctor')
    {

      $scope.thisPatient = chosenPatient;

      /* HTTP PUT Request: getPatientByID() */
      /* Update (PUT) patient personal information */
      $http.put('/Doctor/eCSP/Patient/PersonalInformation?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.thisPatient) 
      .then(function success(response) {

        $scope.thisPatient = response.data.Patient;
        $state.go('app.users.manage_users.manage_patients.view_profile');

      }, function error(response) { });
    }

    else
    {

      $scope.thisPatient = chosenPatient;

      /* HTTP PUT Request: getPatientByID() */
      /* Update (PUT) patient personal information */
      $http.put('/Assistant/eCSP/Patient/PersonalInformation?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.thisPatient) 
      .then(function success(response) {

        $scope.thisPatient = response.data.Patient;
        $state.go('app.users.manage_users.manage_patients.view_profile');

      }, function error(response) { });
    }


    $uibModalInstance.close(true);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
}]);