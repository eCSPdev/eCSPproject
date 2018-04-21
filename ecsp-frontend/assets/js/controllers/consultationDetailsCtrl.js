'use strict';
/** 
  * controllers used for the dashboard
*/
app.controller('consultationDetailsCtrl', ["$scope", function ($scope) {

	$scope.sortType     = 'status'; // set the default sort type
	$scope.sortReverse  = false;  // set the default sort order
	$scope.consultationDetailsSearch  = '';     // set the default search/filter term

	// create the list of patients
	$scope.documents = [
	{ documentName: 'Lab_Results.pdf', uploadDate: '20 February 2017', uploadedBy: 'Stark, Antonio' },
	{ documentName: 'Neurologist_Referral.pdf', uploadDate: '28 February 2017', uploadedBy: 'Stark, Antonio' },
	{ documentName: 'Initial_Form.pdf', uploadDate: '3 February 2017', uploadedBy: 'Talavera, Dr. Fulgencio' },
	{ documentName: 'Naproxel_Prescription.pdf', uploadDate: '13 February 2017', uploadedBy: 'Talavera, Dr. Fulgencio' }
	];


}]);

