'use strict';
/** 
  * Controller for Admin (Doctor and Assistant) login page
  */
  app.controller('adminLoginCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

  	$scope.usernameOrEmail = "";
  	$scope.password = "";

  	/* Token to determine if a user is logged in */
  	$rootScope.isLoggedIn = false;

    /* Variable used to store username, token, and role of logged in user */
    $rootScope.currentUser = {};

  	/* Function to validate login information */
  	$scope.validateLogin = function(usernameOrEmail, password) {

      /* HTTP POST Request: DAlogin() */
      /* Doctor login */
      $http.get('/Doctor/eCSP/Login?username=' + usernameOrEmail + '&pssword=' + password)
      .then(function success(response) {
        console.log(response.data);

        // TODO
        // $rootScope.currentUser.username = ;

      }, function error(response) {
        console.log(response);
      });

   //    for(var i = 0; i < $rootScope.user.length; i++) {

   //     if(usernameOrEmail == $rootScope.user[i].email || usernameOrEmail == $rootScope.user[i].username) {
   //      if(password == $scope.user[i].password) {
   //       $rootScope.isLoggedIn = true;
   //       $rootScope.currentUser = $rootScope.user[i];

   //       $state.go('app.home');
   //     }
   //   }
   // }

   // if($rootScope.isLoggedIn == false) {
   //   alert("Username or password is incorrect. Please try again.");
   //   $scope.password = "";
   // }
 };

}]);

