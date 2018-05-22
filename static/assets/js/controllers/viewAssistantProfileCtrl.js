'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('viewAssistantProfileCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

  	/* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}

  	else {
  		if($rootScope.currentUser.role == 'Assistant' || $rootScope.currentUser.role == 'Patient') {
      		$state.go('app.home');
      	}
    }

    /* HTTP GET Request: getAssistantByID() */
    /* Get assistant personal information */
    $http.get('/Doctor/eCSP/Assistant/PersonalInformation?assistantid=' + $rootScope.chosenAssistant + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
    .then(function success(response) {

      $scope.thisAssistant = response.data.Assistant;

    }, function error(response) { 
      if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }
    });

  }]);

