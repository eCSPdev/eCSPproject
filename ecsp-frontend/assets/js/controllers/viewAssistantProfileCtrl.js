'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('viewAssistantProfileCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

  	/* Redirect user to login page if he or she is not logged in correctly */
  	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}

  	if($rootScope.isLoggedIn == true) {
  		if($rootScope.currentUser.role == 'assistant' || $rootScope.currentUser.role == 'patient') {
      		$state.go('app.home');
      	}
    }

    $scope.thisAssistant = 
    {
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

  }]);

