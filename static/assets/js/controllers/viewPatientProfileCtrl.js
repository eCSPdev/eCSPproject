'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('viewPatientProfileCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

  	/* Redirect user to login page if he or she is not logged in correctly */
  	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}

  	if($rootScope.isLoggedIn == true) {
  		if($rootScope.currentUser.role == 'patient') {
      		$state.go('app.home');
      	}
    }

    $scope.thisPatient = {
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

  }]);

