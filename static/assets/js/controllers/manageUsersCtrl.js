'use strict';
/** 
  * Controller for "Manage Users" page
  * define dependencies
*/
app.controller('manageUsersCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

	/* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }
    
  	if($rootScope.isLoggedIn == true) {
  		if($rootScope.currentUser.role == 'Patient') {
      		$state.go('app.home');
      	}
    }
	
}]);