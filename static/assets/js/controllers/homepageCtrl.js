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
    $rootScope.consultationDate = { };
    $rootScope.uploaded = { };
    $rootScope.chosenRecord = { };

    if ($rootScope.currentUser) {

        if($rootScope.currentUser.role == 'Doctor' || $rootScope.currentUser.role == 'Assistant') {
                $scope.nextState = "app.users.view_records";
        }

        else if($rootScope.currentUser.role == 'Patient') {
                $scope.nextState = "app.users.view_records.patient_consultations";
        }
    }

}]);