'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('editMyProfileCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModal", function ($scope, $rootScope, $state, $http, $uibModal) {


    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
      $state.go('login.signin');
    }

    $scope.thisUser = {};
    
    if($rootScope.currentUser.role == 'Doctor')
    {
      /* HTTP GET Request: getDoctorByID() */
      /* Get doctor personal information */
      $http.get('/Doctor/eCSP/PersonalInformation?doctorid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
      .then(function success(response) {

        $scope.thisUser = response.data.Doctor;

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

  	// open() Function Definition
    $scope.open = function (size) {

      var modalInstance = $uibModal.open({
       templateUrl: 'modal1.html',
       controller: 'ModalInstanceCtrl',
       size: size,
       resolve: {
        chosenUser: function() {
          return $scope.thisUser;
        }
      }
    });

      modalInstance.result.then(function (confirmation) {
       if(confirmation == true) {
       }
     });
    };

  }]);

// Please note that $uibModalInstance represents a modal window (instance) dependency.
// It is not the same as the $uibModal service used above.

// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$rootScope", "$state", "$http", "chosenUser", "$uibModalInstance", function ($scope, $rootScope, $state, $http, chosenUser, $uibModalInstance) {

  $scope.ok = function () {

    $scope.thisUser = chosenUser;
    // $scope.thisUser.licenseno = '0';

    if($rootScope.currentUser.role == 'Doctor')
    {
      /* HTTP PUT Request: getDoctorByID() */
      /* Update doctor personal information */
      $http.put('/Doctor/eCSP/PersonalInformation', $scope.thisUser) 
      .then(function success(response) {

        $scope.thisUser = response.data.Doctor;
        $state.go('app.users.view_my_profile');

      }, function error(response) { });
    }

    else if($rootScope.currentUser.role == 'Assistant')
    {
      /* HTTP PUT Request: getAssistantByID() */
      /* Update assistant personal information */
      $http.put('/Assistant/eCSP/PersonalInformation', $scope.thisUser) 
      .then(function success(response) {

        $scope.thisUser = response.data.Assistant;
        $state.go('app.users.view_my_profile');

      }, function error(response) { });
    }

    else 
    {
      /* HTTP PUT Request: getPatientByID() */
      /* Update patient personal information */
      $http.put('/Patient/eCSP/PersonalInformation', $scope.thisUser) 
      .then(function success(response) {

        $scope.thisUser = response.data.Patient;
        $state.go('app.users.view_my_profile');

      }, function error(response) { });
    }

    $uibModalInstance.close(true);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
}]);