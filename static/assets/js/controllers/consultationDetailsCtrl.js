'use strict';
/** 
  * controllers used for the dashboard
*/
app.controller('consultationDetailsCtrl', ["$scope", "$rootScope", "$state", function ($scope, $rootScope, $state) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.consultationDetailsSearch  = '';     // set the default search/filter term

	/* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
        $state.go('login.signin');
    }

	// create the list of patients
	$scope.documents = [
	{ documentName: 'Lab_Results.pdf', documentType: 'Results', uploadDate: '20 February 2017', uploadedBy: 'Stark, Antonio' },
	{ documentName: 'Neurologist_Referral.pdf', documentType: 'Referral', uploadDate: '28 February 2017', uploadedBy: 'Stark, Antonio' },
	{ documentName: 'Initial_Form.pdf', documentType: 'Consultation Notes', uploadDate: '3 February 2017', uploadedBy: 'Talavera, Dr. Fulgencio' },
	{ documentName: 'Naproxel_Prescription.pdf', documentType: 'Prescription', uploadDate: '13 February 2017', uploadedBy: 'Talavera, Dr. Fulgencio' }
	];


}]);

