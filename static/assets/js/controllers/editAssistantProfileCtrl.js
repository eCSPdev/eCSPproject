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

    /* HTTP GET Request: getAssistantByID() */
      /* Get patient personal information */
    $http.get('/Doctor/eCSP/Assistant/PersonalInformation?assistantid=' + $rootScope.chosenAssistant + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
    .then(function success(response) {

      $scope.thisAssistant = response.data.Assistant;

    }, function error(response) { });

    $scope.thisAssistant.assistantid = $rootScope.chosenAssistant;
    $scope.thisAssistant.username = $rootScope.currentUser.username;
    $scope.thisAssistant.token = $rootScope.currentUser.token;

  	// open() Function Definition
    $scope.open = function (size) {

      var modalInstance = $uibModal.open({
       templateUrl: 'modal1.html',
       controller: 'ModalInstanceCtrl',
       size: size,
       resolve: { 
        chosenAssistant: function() {
          return $scope.thisAssistant;
        }
      }
     });

      modalInstance.result.then(function (confirmation) {
       if(confirmation == true) {  }
    });
    };

  }]);

// Please note that $uibModalInstance represents a modal window (instance) dependency.
// It is not the same as the $uibModal service used above.

// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$rootScope", "$state", "$http", "chosenAssistant", "$uibModalInstance", function ($scope, $rootScope, $state, $http, chosenAssistant, $uibModalInstance) {

	$scope.ok = function () {

      $scope.thisAssistant = chosenAssistant;

      /* HTTP PUT Request: getAssistantByID() */
      /* Update (PUT) assistant personal information */
      $http.put('/Doctor/eCSP/Assistant/PersonalInformation', $scope.thisAssistant) 
      .then(function success(response) {

        $scope.thisAssistant = response.data.Assistant;
        $state.go('app.users.manage_users.manage_assistants.view_profile');


      }, function error(response) { });

		$uibModalInstance.close(true);
	};

	$scope.cancel = function () {
		$uibModalInstance.dismiss('cancel');
	};
}]);