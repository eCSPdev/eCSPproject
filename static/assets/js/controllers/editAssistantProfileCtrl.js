'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('editAssistantProfileCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModal", function ($scope, $rootScope, $state, $http, $uibModal) {


    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
      $state.go('login.signin');
    }
    else {
      if($rootScope.currentUser.role == 'Assistant' || $rootScope.currentUser.role == 'Patient') {
        $state.go('app.home');
      }
    }

    $scope.thisAssistant = { };
    $scope.temporaryPassword = '';

    /* HTTP GET Request: getAssistantByID() */
    /* Get assistant personal information */
    $http.get('/Doctor/eCSP/Assistant/PersonalInformation?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&assistantid=' + $rootScope.chosenAssistant + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
    .then(function success(response) {

      console.log(response);

      $scope.temporaryPassword = response.data.Assistant.pssword;
      delete response.data.Assistant.pssword;
      $scope.thisAssistant = response.data.Assistant;

    }, function error(response) {
      if(response.data && response.data.Error == 'Invalid Token') {
        alert("Invalid credentials. Please login again.");
        $state.go('login.signin');
      }
    });

    $scope.thisAssistant.assistantid = $rootScope.chosenAssistant;
    $scope.thisAssistant.username = $rootScope.currentUser.username;
    $scope.thisAssistant.token = $rootScope.currentUser.token;

  	// open() Function Definition
    $scope.open = function (size) {

      var modalInstance = $uibModal.open({
       templateUrl: 'modal1.html',
       controller: 'ModalInstanceCtrl',
       size: size,
       backdrop: 'static',
       resolve: { 
        chosenAssistant: function() {
          return [$scope.thisAssistant, $scope.temporaryPassword];
        }
      }
    });

      modalInstance.result.then(function (confirmation) {
       if(confirmation == true) {  }
     });
    };

  }]);

// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$rootScope", "$state", "$http", "chosenAssistant", "$uibModalInstance", function ($scope, $rootScope, $state, $http, chosenAssistant, $uibModalInstance) {

	$scope.ok = function () {

    $scope.thisAssistant = chosenAssistant[0];

    if(!$scope.thisAssistant.pssword) {
            $scope.thisAssistant.pssword = $scope.temporaryPassword;
    }

    console.log($scope.thisAssistant.pssword);

    /* HTTP PUT Request: getAssistantByID() */
    /* Update (PUT) assistant personal information */
    $http.put('/Doctor/eCSP/Assistant/PersonalInformation?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.thisAssistant) 
    .then(function success(response) {

      $scope.thisAssistant = response.data.Assistant;
      $state.go('app.users.manage_users.manage_assistants.view_profile');


    }, function error(response) { 
      if(response.data && response.data.Error == 'Invalid Token') {
        alert("Invalid credentials. Please login again.");
        $state.go('login.signin');
      }
    });

    $uibModalInstance.close(true);
  };

  $scope.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
}]);