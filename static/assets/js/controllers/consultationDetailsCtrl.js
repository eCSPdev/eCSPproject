'use strict';
/** 
  * controllers used for the dashboard
*/
app.controller('consultationDetailsCtrl', ["$scope", "$rootScope", "$state", "$http", "$uibModal", "NgTableParams", 'FileUploader', function ($scope, $rootScope, $state, $http, $uibModal, NgTableParams, FileUploader) {

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
    // console.log($rootScope.chosenRecord);

    if($rootScope.currentUser.role == 'Doctor' || $rootScope.currentUser.role == 'Assistant') {
    	$scope.patientid = $rootScope.chosenRecord.patientID;
    }
    else {
    	$scope.patientid = $rootScope.currentUser.userid;
    	$rootScope.chosenRecord.lName = $rootScope.currentUser.lastname;
    	$rootScope.chosenRecord.fName = $rootScope.currentUser.firstname;
    	$rootScope.chosenRecord.mName = $rootScope.currentUser.middlename;

    }

    $http.get('/Doctor/eCSP/Patient/Files?patientid=' + $scope.patientid + '&month=' + $rootScope.consultationDate.month + '&year=' + $rootScope.consultationDate.year) 
		.then(function success(response) {

			$scope.documents = response.data.FilesList;

			for (var i = 0; i < $scope.documents.length; i++) {
				$scope.documents[i].dateofupload = $scope.documents[i].dateofupload.split(" ")[0]; //Get date only
				$scope.documents[i].typeDisplayName = changeTypeDisplayName($scope.documents[i].type);
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

	$scope.download = function(pid, type, fileid) {
		console.log(pid);

		$http.get('/Doctor/eCSP/Patient/Files/Download?patientid=' + pid + '&type=' + type + '&fileid=' + fileid) 
			.then(function success(response) {
				console.log(response.data);

			}, function error(response) {
				
			}
		);

	}

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

	// 
	$scope.fileType = '';

	var uploader = $scope.uploader = new FileUploader({
        url: '/upload' //aqui es donde se pondra la ruta del query del file upload
    });

	//Esto es un callback function que se llama antes de que se suba el file
	//Dentro de esta funcion es cuando unico se puede cambiar el url pq una vez se define arriba, no se puede cambiar.
    uploader.onBeforeUploadItem = function (item) {

    	switch($scope.fileType) {
    		case 'consultationnote':
    			if ($rootScope.currentUser.role == 'Doctor') {
			    	item.url = '/Doctor/eCSP/Patient/ConsultationNotes?patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=' + $rootScope.currentUser.username + '&recordno=' +  $rootScope.chosenRecord.recordno;
    			}
    			else if ($rootScope.currentUser.role == 'Assistant') {
			    	item.url = '/Assistant/eCSP/Patient/ConsultationNotes?patientid=' + $rootScope.chosenRecord.patientID + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=' + $rootScope.currentUser.username + '&doctorusername=undefined&recordno=' +  $rootScope.chosenRecord.recordno;
    			}
    			else {
			    	item.url = '/Patient/eCSP/ConsultationNotes?patientid=' + $rootScope.currentUser.userid + '&filepath=' + item.file + '&filename=' + item.file.name + '&assistantusername=undefined&doctorusername=undefined&recordno=' +  $rootScope.currentUser.recordno;
    			}

    			return;
    		case 'initialform':
    			if ($rootScope.currentUser.role == 'Doctor') {

    			}
    			else if ($rootScope.currentUser.role == 'Assistant') {

    			}
    			else {
    				
    			}

    			return 'Initial Form';
    		case 'prescription':
    			if ($rootScope.currentUser.role == 'Doctor') {

    			}
    			else if ($rootScope.currentUser.role == 'Assistant') {

    			}
    			else {
    				
    			}
    			return 'Prescription';
    		case 'referral':
    			if ($rootScope.currentUser.role == 'Doctor') {

    			}
    			else if ($rootScope.currentUser.role == 'Assistant') {

    			}
    			else {
    				
    			}
    			return 'Referral';
    		case 'result':
    			if ($rootScope.currentUser.role == 'Doctor') {

    			}
    			else if ($rootScope.currentUser.role == 'Assistant') {

    			}
    			else {
    				
    			}
    			return 'Result';
    	}

        // console.info('onBeforeUploadItem', item);
    };

    $scope.upload = function() {

    	//Upload execute
    	uploader.queue[0].upload();	
    	$uibModalInstance.close(true);
    	// $state.reload();
    };

	$scope.cancel = function () {
		$uibModalInstance.dismiss('cancel');
	};

}]);

