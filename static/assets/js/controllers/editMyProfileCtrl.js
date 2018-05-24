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
    $scope.temporaryPassword = '';
    
    if ($rootScope.currentUser) {
      if($rootScope.currentUser.role == 'Doctor')
      {
        /* HTTP GET Request: getDoctorByID() */
        /* Get doctor personal information */
        $http.get('/Doctor/eCSP/PersonalInformation?doctorid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
        .then(function success(response) {

          $scope.temporaryPassword = response.data.Doctor.pssword;
          delete response.data.Doctor.pssword;
          $scope.thisUser = response.data.Doctor;

        }, function error(response) {
          if(response.data && response.data.Error == 'Invalid Token') {
            alert("Invalid credentials. Please login again.");
            $state.go('login.signin');
          }
         });
      }

      else if($rootScope.currentUser.role == 'Assistant')
      {
        /* HTTP GET Request: getAssistantByID() */
        /* Get assistant personal information */
        $http.get('/Assistant/eCSP/PersonalInformation?assistantid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
        .then(function success(response) {

          $scope.temporaryPassword = response.data.Assistant.pssword;
          delete response.data.Assistant.pssword;
          $scope.thisUser = response.data.Assistant;

        }, function error(response) { 
          if(response.data && response.data.Error == 'Invalid Token') {
            alert("Invalid credentials. Please login again.");
            $state.go('login.signin');
          }
        });
      }

      else 
      {
        /* HTTP GET Request: getPatientByID() */
        /* Get patient personal information */
        $http.get('/Patient/eCSP/PersonalInformation?patientid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
        .then(function success(response) {

          $scope.temporaryPassword = response.data.Patient.pssword;
          delete response.data.Patient.pssword;
          $scope.thisUser = response.data.Patient;

        }, function error(response) { 
          if(response.data && response.data.Error == 'Invalid Token') {
            alert("Invalid credentials. Please login again.");
            $state.go('login.signin');
          }
        });
      }
    }

  	// open() Function Definition
    $scope.open = function (size) {

      var modalInstance = $uibModal.open({
       templateUrl: 'modal1.html',
       controller: 'ModalInstanceCtrl',
       size: size,
       backdrop: 'static',
       resolve: {
        chosenUser: function() {
          if(!$scope.thisUser.pssword) {
            $scope.thisUser.pssword = $scope.temporaryPassword;
          }
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

// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$rootScope", "$state", "$http", "chosenUser", "$uibModalInstance", function ($scope, $rootScope, $state, $http, chosenUser, $uibModalInstance) {

  $scope.ok = function () {

    $scope.thisUser = chosenUser;

    console.log($scope.thisUser);
    if($rootScope.currentUser.role == 'Doctor')
    {
      /* HTTP PUT Request: getDoctorByID() */
      /* Update doctor personal information */
      $http.put('/Doctor/eCSP/PersonalInformation?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.thisUser) 
      .then(function success(response) {

        $scope.thisUser = response.data.Doctor;

        $rootScope.currentUser.firstname = response.data.Doctor.firstname;
        $rootScope.currentUser.middlename = response.data.Doctor.middlename;
        $rootScope.currentUser.lastname = response.data.Doctor.lastname;

        $state.go('app.users.view_my_profile');

      }, function error(response) {
          if(response.data && response.data.Error == 'Invalid Token') {
            alert("Invalid credentials. Please login again.");
            $state.go('login.signin');
          }
       });
    }

    else if($rootScope.currentUser.role == 'Assistant')
    {
      /* HTTP PUT Request: getAssistantByID() */
      /* Update assistant personal information */
      $http.put('/Assistant/eCSP/PersonalInformation?assistantid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.thisUser) 
      .then(function success(response) {

        $scope.thisUser = response.data.Assistant;

        $rootScope.currentUser.firstname = response.data.Assistant.firstname;
        $rootScope.currentUser.middlename = response.data.Assistant.middlename;
        $rootScope.currentUser.lastname = response.data.Assistant.lastname;

        $state.go('app.users.view_my_profile');

      }, function error(response) {
        if(response.data && response.data.Error == 'Invalid Token') {
            alert("Invalid credentials. Please login again.");
            $state.go('login.signin');
          }
       });
    }

    else 
    {
      /* HTTP PUT Request: getPatientByID() */
      /* Update patient personal information */
      $http.put('/Patient/eCSP/PersonalInformation?patientid=' + $rootScope.currentUser.userid + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.thisUser) 
      .then(function success(response) {

        $scope.thisUser = response.data.Patient;

        $rootScope.currentUser.firstname = response.data.Patient.firstname;
        $rootScope.currentUser.middlename = response.data.Patient.middlename;
        $rootScope.currentUser.lastname = response.data.Patient.lastname;

        $state.go('app.users.view_my_profile');

      }, function error(response) { 
        if(response.data && response.data.Error == 'Invalid Token') {
            alert("Invalid credentials. Please login again.");
            $state.go('login.signin');
          }
      });
    }

    $uibModalInstance.close(true);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
}]);