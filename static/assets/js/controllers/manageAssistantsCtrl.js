'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('manageAssistantsCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModal", "NgTableParams", function ($scope, $rootScope, $state, $http, $uibModal, NgTableParams) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.assistantSearch   = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
	if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
		$state.go('login.signin');
	}
    else {
		if($rootScope.currentUser.role == 'Assistant' || $rootScope.currentUser.role == 'Patient') {
			$state.go('app.home');
		}
	}

    // Assistant that is being managed
    $rootScope.chosenAssistant = '';

    /* HTTP GET Request: getAllAssistant() */
    /* Get list of all assistants */
    $http.get('/Doctor/eCSP/AssistantList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
    .then(function success(response) {

		// Populate the list of assistants
		$scope.assistants = response.data.Assistant; 

        // Declaration of table parameters
        $scope.tableParams = new NgTableParams({
        	// Show first page
        	page: 1, 

        	// Count per page
        	count: 25,

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

        if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }

        // Declaration of table parameters
        $scope.tableParams = new NgTableParams({
            // Show first page
            page: 1, 

            // Count per page
            count: 25,

            // initial sort order
            sorting: {
                name: "asc"
            }
        }, {
            // Array with information to display in table ($data in HTML)
            // Length of data
            total: 0, 
            dataset: ""
        });
        
     });

    $scope.getAssistantProfile = function(button, assistantID) {

    	$rootScope.chosenAssistant = assistantID;

    	if(button == 'view') {
    		$state.go('app.users.manage_users.manage_assistants.view_profile');
    	}

    	else if(button == 'edit') {
    		$state.go('app.users.manage_users.manage_assistants.edit_profile');
    	}
    }

    // openActivate() Function Definition
    $scope.openActivate = function (size, assistantID) {

    	var modalInstance = $uibModal.open({
    		templateUrl: 'modal_activate.html',
    		controller: 'ModalInstanceCtrl',
    		size: size,
        backdrop: 'static',
    		resolve: {
    			chosenAssistant: function() {
          		return assistantID;
          		}
    		}
   		}).result.catch(function(res) {
          if (!(res === 'cancel' || res === 'escape key press')) {
            throw res;
        }
    });
    }

    // openDeactivate() Function Definition
    $scope.openDeactivate = function (size, assistantID) {

    	var modalInstance = $uibModal.open({
    		templateUrl: 'modal_deactivate.html',
    		controller: 'ModalInstanceCtrl',
    		size: size,
        backdrop: 'static',
    		resolve: {
    			chosenAssistant: function() {
          		return assistantID;
          		}
    		}
   }).result.catch(function(res) {
          if (!(res === 'cancel' || res === 'escape key press')) {
            throw res;
        }
    });
}

}]);


// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModalInstance", "chosenAssistant", function ($scope, $rootScope, $state, $http, $uibModalInstance, chosenAssistant) {

  // $route.reload();

	$scope.changeStatus = function(button) {

    console.log('Changing status');

		if(button == 'activate') {
			$http.put('/Doctor/eCSP/Assistant/Activate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&assistantid=' + chosenAssistant)
			.then(function success(response) { 
				$state.reload();
			}, function error(response) {
                if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }
             });
		}

		else if(button == 'deactivate') {

      console.log('Deactivating here');
      console.log(chosenAssistant);

			$http.put('/Doctor/eCSP/Assistant/Deactivate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&assistantid=' + chosenAssistant)
			.then(function success(response) { 
				$state.reload();
			}, function error(response) {
                if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }
             });
		}

    	$uibModalInstance.close(true);
	};

  $scope.cancel = function () {
    console.log('Canceled');
    $uibModalInstance.close(true);
  };

}]);