'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('manageAssistantsCtrl', ["$scope", "$rootScope", "$state", "$http", "NgTableParams", function ($scope, $rootScope, $state, $http, NgTableParams) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.assistantSearch   = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
		$state.go('login.signin');
	}

	if($rootScope.isLoggedIn == true) {
		if($rootScope.currentUser.role == 'Assistant' || $rootScope.currentUser.role == 'Patient') {
			$state.go('app.home');
		}
	}

    // Assistant that is being managed
    $rootScope.chosenAssistant = "";

    /* HTTP GET Request: getAllAssistant() */
    /* Get list of all assistants */
    $http.get('/Doctor/eCSP/AssistantList') 
    .then(function success(response) {
    	console.log(response.status);
		
		// Populate the list of assistants
        $scope.assistants = response.data.Assistant; 

        // Declaration of table parameters
		$scope.tableParams = new NgTableParams({
        	// Show first page
        	page: 1, 

        	// Count per page
        	count: 10,

        	// initial sort order
        	sorting: {
        		name: "asc"
        	}
    	}, {
    		// Array with information to display in table ($data in HTML)
            // Length of data
            total: $scope.assistants.length, 
            dataset: $scope.assistants
        });

	}, function error(response) {
		console.log(response);
	});

	$scope.getAssistantProfile = function(button, employeeID) {

		$rootScope.chosenAssistant = employeeID;

		if(button == 'view') {
			$state.go('app.users.manage_users.manage_assistants.view_profile');
		}

		else if(button == 'edit') {
			$state.go('app.users.manage_users.manage_assistants.edit_profile');
		}
	}
}]);