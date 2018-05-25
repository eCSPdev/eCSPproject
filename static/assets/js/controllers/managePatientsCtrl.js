'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('managePatientsCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModal", "NgTableParams", function ($scope, $rootScope, $state, $http, $uibModal, NgTableParams) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.patientSearch   = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
      $state.go('login.signin');
  }
  else {
      if($rootScope.currentUser.role == 'Patient') {
         $state.go('app.home');
     }
 }

	// Patient that is being managed
	$rootScope.chosenPatient = '';

    if ($rootScope.currentUser) {
    	if($rootScope.currentUser.role == 'Doctor')
    	{
    		/* HTTP GET Request: getAllPatients() */
    		/* Get list of all patients */
    		$http.get('/Doctor/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
    		.then(function success(response) {

        	// Search bar
        	for(var i = 0; i < response.data.Patient.length; i++) 
        	{
        		if(response.data.Patient[i].status == true)
        		{
        			response.data.Patient[i].status = 'Active';
        		}

        		else
        		{
        			response.data.Patient[i].status = 'Inactive';
        		}
        	}

    		// Populate the list of patients
    		$scope.patients = response.data.Patient; 

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
                total: $scope.patients.length, 
                dataset: $scope.patients
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
    	}

    	else
    	{
    		/* HTTP GET Request: getAllPatients() */
    		/* Get list of all patients */
    		$http.get('/Assistant/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token) 
    		.then(function success(response) {

        	// Search bar
        	for(var i = 0; i < response.data.Patient.length; i++) 
        	{
        		if(response.data.Patient[i].status == true)
        		{
        			response.data.Patient[i].status = 'Active';
        		}

        		else
        		{
        			response.data.Patient[i].status = 'Inactive';
        		}
        	}

    		// Populate the list of patients
    		$scope.patients = response.data.Patient; 

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
                total: $scope.patients.length, 
                dataset: $scope.patients
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
    	}
    }

    $scope.getPatientProfile = function(button, patientID) {

      $rootScope.chosenPatient = patientID;
      
      if(button == 'view') {
         $state.go('app.users.manage_users.manage_patients.view_profile');
     }

     else if(button == 'edit') {
         $state.go('app.users.manage_users.manage_patients.edit_profile');
     }
 }

    // openActivate() Function Definition
    $scope.openActivate = function (size, patientID) {

      if($rootScope.activatePatientCount == 0) {
         var modalInstance = $uibModal.open({
            templateUrl: 'modal_activate.html',
            controller: 'ModalInstanceCtrl',
            size: size,
            backdrop: 'static',
            resolve: {
               chosenPatient: function() {
                  return patientID;
              }
          }
      }).result.catch(function(res) {
          if (!(res === 'cancel' || res === 'escape key press')) {
            console.log(res);
            throw res;
        }
    });

      $rootScope.activatePatientCount++;
  }

  else {
    var modalInstance = $uibModal.open({
        templateUrl: 'modal_activate.html',
        controller: 'ModalInstanceCountCtrl',
        size: size,
        backdrop: 'static',
        resolve: {
           chosenPatient: function() {
              return patientID;
          }
      }
  }).result.catch(function(res) {
      if (!(res === 'cancel' || res === 'escape key press')) {
        console.log(res);
        throw res;
    }
});
}
}

    // openDeactivate() Function Definition
    $scope.openDeactivate = function (size, patientID) {

      if($rootScope.deactivatePatientCount == 0) {
        var modalInstance = $uibModal.open({
          templateUrl: 'modal_deactivate.html',
          controller: 'ModalInstanceCtrl',
          size: size,
          backdrop: 'static',
          resolve: {
            chosenPatient: function() {
              return patientID;
          }
      }
  }).result.catch(function(res) {
    if (!(res === 'cancel' || res === 'escape key press')) {
        throw res;
    }
});

  $rootScope.deactivatePatientCount++;
}

else {
    var modalInstance = $uibModal.open({
      templateUrl: 'modal_deactivate.html',
      controller: 'ModalInstanceCountCtrl',
      size: size,
      backdrop: 'static',
      resolve: {
        chosenPatient: function() {
          return patientID;
      }
  }
}).result.catch(function(res) {
  if (!(res === 'cancel' || res === 'escape key press')) {
    throw res;
}
});
}

}

}]);

// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModalInstance", "chosenPatient", function ($scope, $rootScope, $state, $http, $uibModalInstance, chosenPatient) {

    $scope.changeStatus = function(button) {

        if($rootScope.currentUser.role == 'Doctor') {

            if(button == 'activate') {
                $http.put('/Doctor/eCSP/Patient/Activate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + chosenPatient)
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
                $http.put('/Doctor/eCSP/Patient/Deactivate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + chosenPatient  + '&daysofgrace=' + $scope.daysofgrace)
                .then(function success(response) { 
                    $state.reload();
                }, function error(response) { 
                    if(response.data && response.data.Error == 'Invalid Token') {
                      alert("Invalid credentials. Please login again.");
                      $state.go('login.signin');
                  }
              });
            }
        }

        else {

            if(button == 'activate') {
                $http.put('/Assistant/eCSP/Patient/Activate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + chosenPatient)
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
                $http.put('/Assistant/eCSP/Patient/Deactivate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + chosenPatient  + '&daysofgrace=' + $scope.daysofgrace)
                .then(function success(response) { 
                    $state.reload();
                }, function error(response) { 
                    if(response.data && response.data.Error == 'Invalid Token') {
                      alert("Invalid credentials. Please login again.");
                      $state.go('login.signin');
                  }
              });
            }
        }

        $uibModalInstance.close(true);
    };

    $scope.cancel = function () {
        $scope.daysofgrace = '30';
        $uibModalInstance.dismiss('cancel');
    };

}]);

// Popup/Modal Controller
app.controller('ModalInstanceCountCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModalInstance", "chosenPatient", function ($scope, $rootScope, $state, $http, $uibModalInstance, chosenPatient) {

    $scope.changeStatus = function(button) {

        if($rootScope.currentUser.role == 'Doctor') {

            if(button == 'activate') {
                $http.put('/Doctor/eCSP/Patient/Activate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + chosenPatient)
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
                $http.put('/Doctor/eCSP/Patient/Deactivate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + chosenPatient  + '&daysofgrace=' + $scope.daysofgrace)
                .then(function success(response) { 
                    $state.reload();
                }, function error(response) { 
                    if(response.data && response.data.Error == 'Invalid Token') {
                      alert("Invalid credentials. Please login again.");
                      $state.go('login.signin');
                  }
              });
            }
        }

        else {

            if(button == 'activate') {
                $http.put('/Assistant/eCSP/Patient/Activate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + chosenPatient)
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
                $http.put('/Assistant/eCSP/Patient/Deactivate?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + chosenPatient  + '&daysofgrace=' + $scope.daysofgrace)
                .then(function success(response) { 
                    $state.reload();
                }, function error(response) { 
                    if(response.data && response.data.Error == 'Invalid Token') {
                      alert("Invalid credentials. Please login again.");
                      $state.go('login.signin');
                  }
              });
            }
        }

        $uibModalInstance.close(true);
    };

    $scope.cancel = function () {
        $scope.daysofgrace = '30';
        $uibModalInstance.dismiss('cancel');
    };

}]);