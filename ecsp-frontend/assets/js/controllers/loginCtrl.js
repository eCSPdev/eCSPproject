'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('loginCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

  	$scope.usernameOrEmail = "";
  	$scope.password = "";

  	/* Array of dummy user data */
  	$scope.user = [{
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
  		name: 'Leslie',
  		lastName: 'Knope'
  	},

  	{
  		role: 'patient',
  		email: 'phillip.fry@gmail.com',
  		username: 'phillip.fry',
  		password: 'iLoveLeela@',
  		name: 'Phillip',
  		lastName: 'Fry'
  	}];

  	/* Token to determine if a user is logged in */
  	$rootScope.isLoggedIn = false;

  	/* Currently logged in user */
  	$rootScope.currentUser = { };

  	/* Function to validate login information */
  	$scope.validateLogin = function(usernameOrEmail, password) {

  		console.log('here');
  		for(var i = 0; i < $scope.user.length; i++) {

  			if(usernameOrEmail == $scope.user[i].email || usernameOrEmail == $scope.user[i].username) {
  				if(password == $scope.user[i].password) {
  					$rootScope.isLoggedIn = true;
  					$rootScope.currentUser = $scope.user[i];

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

