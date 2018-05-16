'use strict';
/** 
  * controllers used for the dashboard
*/
app.controller('consultationDetailsCtrl', ["$scope", "$rootScope", "$state", "$http", "NgTableParams", function ($scope, $rootScope, $state, $http, NgTableParams) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.consultationDetailsSearch  = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }

    console.log($rootScope.chosenRecord);

    //Make sure type is displayed correctly in table
    function changeTypeDisplayName(type) {
    	switch(type) {
    		case 'consultationnote':
    			return 'Consultation Note';
    		case 'initialform':
    			return 'Initial Form';
    		case 'prescription':
    			return 'Prescription';
    		case 'referral':
    			return 'Referral';
    		case 'result':
    			return 'Result';
    	}
    }

    $http.get('/Doctor/eCSP/Patient/Files?patientid=' + $rootScope.chosenRecord.patientID + '&month=' + $rootScope.consultationDate.month + '&year=' + $rootScope.consultationDate.year) 
		.then(function success(response) {

			console.log($scope.documents);

			$scope.documents = response.data.FilesList;

			for (var i = 0; i < $scope.documents.length; i++) {
				$scope.documents[i].dateofupload = $scope.documents[i].dateofupload.split(" ")[0]; //Get date only
				$scope.documents[i].type = changeTypeDisplayName($scope.documents[i].type);
			}

			console.log($scope.documents);

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
	            total: $scope.documents.length, 
	            dataset: $scope.documents
	        });
		},
			function error(response) {});

	$scope.download = function(data) {
		console.log(data);
		window.location.assign(data);
	}



}]);

