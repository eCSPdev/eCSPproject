'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('loginCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

  	$scope.usernameOrEmail = "";
  	$scope.password = "";

  	/* Array of dummy user data */
  	$rootScope.user = [{
  		role: 'doctor',
  		email: 'fulgencio.talavera@gmail.com',
  		username: 'fulgencio.talavera',
  		password: 'testing123',
  		name: 'Fulgencio',
  		lastName: 'Talavera'
  	},

  	{
  		role: 'assistant',
  		email: 'francisco.castillo@gmail.com',
  		username: 'francisco.castillo',
  		password: 'probando567',
  		name: 'Francisco',
  		lastName: 'Castillo'
  	},

  	{
  		role: 'assistant',
  		email: 'michael.scott@gmail.com',
  		username: 'michael.scott',
  		password: 'dunderMifflin8',
  		name: 'Michael',
  		lastName: 'Scott'
  	},

  	{
  		role: 'patient',
  		email: 'leslie.knope@gmail.com',
  		username: 'leslie.knope',
  		password: 'joeBidenRulz!',
  		recordID: '12345',
  		name: 'Leslie',
  		lastName: 'Knope'
  	},

  	{
  		role: 'patient',
  		email: 'phillip.fry@gmail.com',
  		username: 'phillip.fry',
  		password: 'iLoveLeela@',
  		recordID: '55554',
  		name: 'Phillip',
  		lastName: 'Fry'
  	}];

  	/* Token to determine if a user is logged in */
  	$rootScope.isLoggedIn = false;

  	/* Currently logged in user */
  	$rootScope.currentUser = { };

  	/* Function to validate login information */
  	$scope.validateLogin = function(usernameOrEmail, password) {

  		for(var i = 0; i < $rootScope.user.length; i++) {

  			if(usernameOrEmail == $rootScope.user[i].email || usernameOrEmail == $rootScope.user[i].username) {
  				if(password == $scope.user[i].password) {
  					$rootScope.isLoggedIn = true;
  					$rootScope.currentUser = $rootScope.user[i];

  					$state.go('app.home');
  				}
  			}
  		}

  		if($rootScope.isLoggedIn == false) {
  			alert("Username or password is incorrect. Please try again.");
  			$scope.password = "";
  		}
  	};

  }]);

