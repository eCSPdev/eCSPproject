var app = angular.module('clipApp', ['clip-two']);
app.run(['$rootScope', '$state', '$stateParams', '$trace',
    function ($rootScope, $state, $stateParams, $trace) {

		// Attach Fastclick for eliminating the 300ms delay between a physical tap and the firing of a click event on mobile browsers
		FastClick.attach(document.body);

		// Set some reference to access them from any scope
		$rootScope.$state = $state;
		$rootScope.$stateParams = $stateParams;

		// Set login variable as "false" initially
		$rootScope.isLoggedIn = false;

		// GLOBAL APP SCOPE
		// set below basic information
		$rootScope.app = {
			name: 'eCSP', // name of your project
			author: 'KLC Tech Solutions', // author's name or company name
			description: '', // brief description
			version: '1.0', // current version
			year: ((new Date()).getFullYear()), // automatic current year (for copyright information)
			isMobile: (function () {// true if the browser is a mobile device
				var check = false;
				if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
					check = true;
				};
				return check;
			})(),
			layout: {
				isNavbarFixed: true, //true if you want to initialize the template with fixed header
				isSidebarFixed: false, // true if you want to initialize the template with fixed sidebar
				isSidebarClosed: true, // true if you want to initialize the template with closed sidebar
				isFooterFixed: true, // true if you want to initialize the template with fixed footer
				theme: 'theme-1', // indicate the theme chosen for your project
				logo: 'static/assets/images/ecsp-logo.png', // relative path of the project logo
			}
		};

	}]);


// configuration: Angular-Loading-Bar
app.config(['cfpLoadingBarProvider', function (cfpLoadingBarProvider) {
	cfpLoadingBarProvider.includeBar = true;
	cfpLoadingBarProvider.includeSpinner = false;
}]);

