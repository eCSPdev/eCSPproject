'use strict';
/** 
  * controllers used for the dashboard
*/

app.controller('homepageCtrl', ["$scope", "$rootScope", "$state", function($scope, $rootScope, $state) {
    
    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }

    $scope.nextState = " ";

    if($rootScope.currentUser.role == "doctor" || $rootScope.currentUser.role == "assistant") {
            $scope.nextState = "app.users.view_records";
    }

    else if($rootScope.currentUser.role == "patient") {
            $scope.nextState = "app.users.consultation_details";
    }

}]);