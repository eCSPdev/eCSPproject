'use strict';
/* Controller used for accessing root scope and state variables */

app.controller('partialViewCtrl', ["$scope", "$rootScope", "$state", function($scope, $rootScope, $state) {

    // Grab current page state
    $scope.pageState = $state.current.name;

}]);