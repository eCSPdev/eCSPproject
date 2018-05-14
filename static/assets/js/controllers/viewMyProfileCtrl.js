'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('viewMyProfileCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

  	/* Redirect user to login page if he or she is not logged in correctly */
  	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
  		$state.go('login.signin');
  	}

    /* HTTP GET Request: getAssistantByID() */
    /* Get assistant personal information */
    $http.get('/Doctor/eCSP/Assistant/PersonalInformation?assistantid=' + $rootScope.chosenAssistant + '&username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
    .then(function success(response) {

      $scope.thisAssistant = response.data.Assistant;
      console.log($scope.thisAssistant);

    }, function error(response) { });


  	/* Currently logged in user */
  	$scope.thisUser = { 
      firstName: 'Fulgencio',
      middleName: '',
      lastName: 'Talavera',
      phoneNumber: '(787) 452-1244',
      addressLine1: 'HC-73 1232 Bo. Molina',
      addressLine2: 'Apt. #212',
      state: 'PR',
      city: 'Fajardo',
      countryRegion: 'Puerto Rico',
      zipCode: '00738',
      email: 'fulgencio.talavera@gmail.com'
      
    };

  }]);

