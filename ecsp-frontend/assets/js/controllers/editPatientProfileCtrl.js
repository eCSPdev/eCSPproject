'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('editPatientProfileCtrl', ["$scope", "$rootScope", "$state", "$uibModal", function ($scope, $rootScope, $state, $uibModal) {

  	$scope.userType = "";

    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }

    $scope.chosenPatient = {
      firstName: 'Leslie', 
      middleName: 'Anne', 
      lastName: 'Knope', 
      insuranceCompany: '',
      phoneNumber: '308-321-0092', 
      addressLine1: 'Winfree Apartments Apt. 123', 
      addressLine2: '',
      countryRegion: 'United States',
      state: 'IN',
      city: 'Pawnee',
      countryRegion: 'US',
      zipCode: '00213',
      email: ''
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