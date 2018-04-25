'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('editAssistantProfileCtrl', ["$scope", "$rootScope", "$state", "$uibModal", function ($scope, $rootScope, $state, $uibModal) {

  	$scope.userType = "";

    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }

    if($rootScope.isLoggedIn == true) {
      if($rootScope.currentUser.role == 'assistant' || $rootScope.currentUser.role == 'patient') {
          $state.go('app.home');
        }
    }

    $scope.chosenAssistant = { 
      firstName: 'Francisco', 
      middleName: '', 
      lastName: 'Castillo', 
      phoneNumber: '315-120-1123', 
      addressLine1: 'One Batch St. Penny-Dime Avenue', 
      addressLine2: 'Apartment 404',
      countryRegion: 'United States',
      state: 'NY',
      city: 'New York City',
      countryRegion: 'US',
      zipCode: '10012',
      email: 'frank.castle@gmail.com'
    };

  	// open() Function Definition
    $scope.open = function (size) {

      var modalInstance = $uibModal.open({
       templateUrl: 'modal1.html',
       controller: 'ModalInstanceCtrl',
       size: size,
     });

      modalInstance.result.then(function (confirmation) {
       if(confirmation == true) {
        console.log('worked');
      }
    });
    };

  }]);

// Please note that $uibModalInstance represents a modal window (instance) dependency.
// It is not the same as the $uibModal service used above.

// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$uibModalInstance", function ($scope, $uibModalInstance) {

	$scope.ok = function () {
		$uibModalInstance.close(true);
	};

	$scope.cancel = function () {
		$uibModalInstance.dismiss('cancel');
	};
}]);