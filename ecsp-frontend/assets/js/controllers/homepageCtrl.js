'use strict';
/** 
  * controllers used for the dashboard
*/

app.controller('homepageCtrl', ["$scope", "$rootScope", "$state", function($scope, $rootScope, $state) {

    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }

    $scope.manageRedirect = function() {
        if($rootScope.currentUser.role == "doctor" || $rootScope.currentUser.role == "assistant") {
            $state.go('app.users.view_records');
        }

        else if($rootScope.currentUser.role == "patient") {
            $state.go('app.users.view_records.patient_consultations.consultation_details');
        }
    }

}]);