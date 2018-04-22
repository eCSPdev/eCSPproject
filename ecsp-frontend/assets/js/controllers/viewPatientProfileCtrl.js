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

  }]);

