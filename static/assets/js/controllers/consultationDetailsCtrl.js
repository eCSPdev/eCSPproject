'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('consultationDetailsCtrl', ["$scope", "$rootScope", "$state", "$http", "$window", "$uibModal", "NgTableParams", 'FileUploader', function ($scope, $rootScope, $state, $http, $window, $uibModal, NgTableParams, FileUploader) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.consultationDetailsSearch  = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }

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

   $scope.patientid = '';


    // if($rootScope.currentUser) {
        if($rootScope.currentUser.role == 'Doctor' || $rootScope.currentUser.role == 'Assistant') {
        	$scope.patientid = $rootScope.chosenRecord.patientID;
        }
        else {
        	$scope.patientid = $rootScope.currentUser.userid;
        	$rootScope.chosenRecord.lName = $rootScope.currentUser.lastname;
        	$rootScope.chosenRecord.fName = $rootScope.currentUser.firstname;
        	$rootScope.chosenRecord.mName = $rootScope.currentUser.middlename;
        }
    // }

    $rootScope.populatePatientFiles = function() {
        if($rootScope.currentUser.role == 'Doctor') {
            $http.get('/Doctor/eCSP/Patient/Files?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $scope.patientid + '&month=' + $rootScope.consultationDate.month + '&year=' + $rootScope.consultationDate.year) 
            .then(function success(response) {

               $scope.documents = response.data.FilesList;

               for (var i = 0; i < $scope.documents.length; i++) {
                $scope.documents[i].dateofupload = $scope.documents[i].dateofupload.split(" ")[0]; //Get date only
                $scope.documents[i].typeDisplayName = changeTypeDisplayName($scope.documents[i].type);

                if ($scope.documents[i].sign == 'undefined') {
                    $scope.documents[i].sign = $rootScope.chosenRecord.username;
                }
            }
            
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
     function error(response) {
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
		            total: 0, 
		            dataset: ""
		        });

          });
        }

        else if($rootScope.currentUser.role == 'Assistant') {
            $http.get('/Assistant/eCSP/Patient/Files?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $scope.patientid + '&month=' + $rootScope.consultationDate.month + '&year=' + $rootScope.consultationDate.year) 
            .then(function success(response) {

               $scope.documents = response.data.FilesList;

               for (var i = 0; i < $scope.documents.length; i++) {
                $scope.documents[i].dateofupload = $scope.documents[i].dateofupload.split(" ")[0]; //Get date only
                $scope.documents[i].typeDisplayName = changeTypeDisplayName($scope.documents[i].type);

                if ($scope.documents[i].sign == 'undefined') {
                    $scope.documents[i].sign = $rootScope.chosenRecord.username;
                }
            }

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
        function error(response) {
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
                    total: 0, 
                    dataset: ""
                });

            });
        }

        else {
            $http.get('/Patient/eCSP/Files?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.currentUser.userid + '&month=' + $rootScope.consultationDate.month + '&year=' + $rootScope.consultationDate.year) 
            .then(function success(response) {

               $scope.documents = response.data.FilesList;

               for (var i = 0; i < $scope.documents.length; i++) {
                $scope.documents[i].dateofupload = $scope.documents[i].dateofupload.split(" ")[0]; //Get date only
                $scope.documents[i].typeDisplayName = changeTypeDisplayName($scope.documents[i].type);

                if ($scope.documents[i].sign == 'undefined') {
                    $scope.documents[i].sign = $rootScope.currentUser.username;
                }
            }

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
        function error(response) {
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
                    total: 0, 
                    dataset: ""
                });

            });
        }
    }

    $scope.download = function(pid, type, fileid) {

        if($rootScope.currentUser.role == 'Doctor') {
          $http.get('/Doctor/eCSP/Patient/Files/Download?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + pid + '&type=' + type + '&fileid=' + fileid) 
          .then(function success(response) {
            $window.open(response.data.FileLink, '_blank');
        }, 
        function error(response) { }
        );

      }

      else if($rootScope.currentUser.role == 'Assistant') {
          $http.get('/Assistant/eCSP/Patient/Files/Download?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + pid + '&type=' + type + '&fileid=' + fileid) 
          .then(function success(response) {
            $window.open(response.data.FileLink, '_blank');
        }, 
        function error(response) { }
        );
      }

      else {
        $http.get('/Patient/eCSP/Files/Download?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + pid + '&type=' + type + '&fileid=' + fileid) 
        .then(function success(response) {
            $window.open(response.data.FileLink, '_blank');
        }, 
        function error(response) { 
        }
        );
    }
}

    // Execute query
    $rootScope.populatePatientFiles();

	// openActivate() Function Definition
    $scope.open = function () {

    	var modalInstance = $uibModal.open({
    		templateUrl: 'modal_upload.html',
    		controller: 'ModalInstanceCtrl',
    		size: 'md'
     });
    }

}]);

// Popup/Modal Controller
app.controller('ModalInstanceCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModalInstance", "FileUploader", function ($scope, $rootScope, $state, $http, $uibModalInstance, FileUploader) {

	
	$scope.fileType = '';

	var uploader = $scope.uploader = new FileUploader({
        url: '/upload'
    });

	// Esto es un callback function que se llama antes de que se suba el file
	// Dentro de esta funcion es cuando unico se puede cambiar el url pq una vez se define arriba, no se puede cambiar.
    uploader.onBeforeUploadItem = function (item) {

    	switch($scope.fileType) {
            case 'consultationnote':
            if ($rootScope.currentUser.role == 'Doctor') {
                item.url = '/Doctor/eCSP/Patient/ConsultationNotes?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=' + $rootScope.currentUser.username + '&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else if ($rootScope.currentUser.role == 'Assistant') {
                item.url = '/Assistant/eCSP/Patient/ConsultationNotes?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=' + $rootScope.currentUser.username + '&doctorusername=undefined&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else {
                item.url = '/Patient/eCSP/ConsultationNotes?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.currentUser.userid + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=undefined&recordno=' +  $rootScope.currentUser.recordno;
            }

            return;
            case 'initialform':
            if ($rootScope.currentUser.role == 'Doctor') {
                item.url = '/Doctor/eCSP/Patient/InitialForm?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=' + $rootScope.currentUser.username + '&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else if ($rootScope.currentUser.role == 'Assistant') {
                item.url = '/Assistant/eCSP/Patient/InitialForm?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=' + $rootScope.currentUser.username + '&doctorusername=undefined&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else {
                item.url = '/Patient/eCSP/InitialForm?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.currentUser.userid + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=undefined&recordno=' +  $rootScope.currentUser.recordno;
            }

            return;
            case 'prescription':
            if ($rootScope.currentUser.role == 'Doctor') {
                item.url = '/Doctor/eCSP/Patient/Prescription?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=' + $rootScope.currentUser.username + '&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else if ($rootScope.currentUser.role == 'Assistant') {
                item.url = '/Assistant/eCSP/Patient/Prescription?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=' + $rootScope.currentUser.username + '&doctorusername=undefined&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else {
                item.url = '/Patient/eCSP/Prescription?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.currentUser.userid + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=undefined&recordno=' +  $rootScope.currentUser.recordno;
            }
            return;
            case 'referral':
            if ($rootScope.currentUser.role == 'Doctor') {
                item.url = '/Doctor/eCSP/Patient/Referral?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=' + $rootScope.currentUser.username + '&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else if ($rootScope.currentUser.role == 'Assistant') {
                item.url = '/Assistant/eCSP/Patient/Referral?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=' + $rootScope.currentUser.username + '&doctorusername=undefined&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else {
                item.url = '/Patient/eCSP/Referral?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.currentUser.userid + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=undefined&recordno=' +  $rootScope.currentUser.recordno;
            }
            return;
            case 'result':
            if ($rootScope.currentUser.role == 'Doctor') {
                item.url = '/Doctor/eCSP/Patient/Result?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=' + $rootScope.currentUser.username + '&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else if ($rootScope.currentUser.role == 'Assistant') {
                item.url = '/Assistant/eCSP/Patient/Result?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=' + $rootScope.currentUser.username + '&doctorusername=undefined&recordno=' +  $rootScope.chosenRecord.recordno;
            }
            else {
                item.url = '/Patient/eCSP/Result?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token + '&patientid=' + $rootScope.currentUser.userid + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=undefined&recordno=' +  $rootScope.currentUser.recordno;
            }
            return;
        }
    };

    uploader.onCompleteAll = function () {
        $rootScope.populatePatientFiles();
    };

    $scope.upload = function() {

        //Upload execute
        uploader.queue[0].upload(); 
        $uibModalInstance.close(true);

        //Save data for reload
        $rootScope.uploaded.bool = true;
        if ($rootScope.consultationDate.month != undefined) {
            $rootScope.uploaded.month = $rootScope.consultationDate.month;
            $rootScope.uploaded.year = $rootScope.consultationDate.year;
        }
        else {
            var date = new Date();
            $rootScope.consultationDate.month = date.getMonth()+1;
            $rootScope.consultationDate.year = date.getFullYear();
            $rootScope.uploaded.month = $rootScope.consultationDate.month;
            $rootScope.uploaded.year = $rootScope.consultationDate.year;
        }

    };

    $scope.cancel = function () {
      $uibModalInstance.dismiss('cancel');
  };

}]);

