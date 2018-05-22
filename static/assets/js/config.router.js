'use strict';



/**
 * Config for the router
 */
 app.config(['$stateProvider', '$locationProvider', '$urlRouterProvider', '$controllerProvider', '$compileProvider', '$filterProvider', '$provide', '$ocLazyLoadProvider', 'JS_REQUIRES',
    function ($stateProvider, $locationProvider, $urlRouterProvider, $controllerProvider, $compileProvider, $filterProvider, $provide, $ocLazyLoadProvider, jsRequires) {

        app.controller = $controllerProvider.register;
        app.directive = $compileProvider.directive;
        app.filter = $filterProvider.register;
        app.factory = $provide.factory;
        app.service = $provide.service;
        app.constant = $provide.constant;
        app.value = $provide.value;

    // LAZY MODULES

    $ocLazyLoadProvider.config({
        debug: false,
        events: true,
        modules: jsRequires.modules
    });

    // APPLICATION ROUTES
    // -----------------------------------
    $urlRouterProvider.otherwise("/login");
    $locationProvider.hashPrefix('');

    //
    // Set up the states
    $stateProvider.state('app', {
        url: "",
        templateUrl: "static/assets/views/app.html",
        resolve: loadSequence('modernizr', 'moment', 'angularMoment', 'uiSwitch', 'perfect-scrollbar-plugin', 'toaster', 'ngAside', 'vAccordion', 'sweet-alert', 'chartjs', 'tc.chartjs', 'oitozero.ngSweetAlert', 'truncate', 'htmlToPlaintext', 'angular-notification-icons'),
        abstract: true
    }).state('app.home', {
        url: "/home",
        templateUrl: "static/assets/views/homepage.html",
        resolve: loadSequence('jquery-sparkline', 'homepageCtrl'),
        title: 'Home',
        ncyBreadcrumb: {
            label: 'Home'
        }
    }).state('app.users', {
        url: '/home',
        template: '<div ui-view class="fade-in-up"></div>',
        title: 'Home',
        ncyBreadcrumb: {
            label: 'Home'
        }
    }).state('app.users.contact', {
        url: "/contactUs",
        templateUrl: "static/assets/views/contact_page.html",
        resolve: loadSequence('jquery-sparkline', 'ngMap', 'mapsCtrl', 'partialViewCtrl'),
        title: 'Contact Page',
        ncyBreadcrumb: {
            label: 'Contact Us'
        }
    }).state('app.users.manage_users', {
        url: "/manageUsers",
        templateUrl: "static/assets/views/manage_users.html",
        resolve: loadSequence('jquery-sparkline', 'manageUsersCtrl'),
        title: 'Manage Users',
        ncyBreadcrumb: {
            label: 'Manage Users'
        }
    }).state('app.users.manage_users.manage_patients', {
        url: "/patients",
        templateUrl: "static/assets/views/manage_patients.html",
        resolve: loadSequence('ngTable', 'managePatientsCtrl'),
        title: 'Manage Patients',
        ncyBreadcrumb: {
            label: 'Patients'
        }
    }).state('app.users.manage_users.manage_patients.view_profile', {
        url: "/viewPatientProfile",
        templateUrl: "static/assets/views/view_patient_profile.html",
        resolve: loadSequence('jquery-sparkline', 'viewPatientProfileCtrl'),
        title: 'View Profile',
        ncyBreadcrumb: {
            label: 'View Profile'
        }
    }).state('app.users.manage_users.manage_patients.edit_profile', {
        url: "/editPatientProfile",
        templateUrl: "static/assets/views/edit_patient_profile.html",
        resolve: loadSequence('jquery-sparkline', 'editPatientProfileCtrl'),
        title: 'Edit Profile',
        ncyBreadcrumb: {
            label: 'Edit Profile'
        }
    }).state('app.users.manage_users.manage_assistants', {
        url: "/assistants",
        templateUrl: "static/assets/views/manage_assistants.html",
        resolve: loadSequence('ngTable', 'manageAssistantsCtrl'),
        title: 'Manage Assistants',
        ncyBreadcrumb: {
            label: 'Assistants'
        }
    }).state('app.users.manage_users.manage_assistants.view_profile', {
        url: "/viewAssistantProfile",
        templateUrl: "static/assets/views/view_assistant_profile.html",
        resolve: loadSequence('jquery-sparkline', 'viewAssistantProfileCtrl'),
        title: 'View Profile',
        ncyBreadcrumb: {
            label: 'View Profile'
        }
    }).state('app.users.manage_users.manage_assistants.edit_profile', {
        url: "/editAssistantProfile",
        templateUrl: "static/assets/views/edit_assistant_profile.html",
        resolve: loadSequence('jquery-sparkline', 'editAssistantProfileCtrl'),
        title: 'Edit Profile',
        ncyBreadcrumb: {
            label: 'Edit Profile'
        }
    }).state('app.users.manage_users.add_new_user', {
        url: "/addUser",
        templateUrl: "static/assets/views/add_new_user.html",
        resolve: loadSequence('jquery-sparkline', 'addNewUserCtrl'),
        title: 'Add New User',
        ncyBreadcrumb: {
            label: 'New User'
        }
    }).state('app.users.view_my_profile', {
        url: "/viewMyProfile",
        templateUrl: "static/assets/views/view_my_profile.html",
        resolve: loadSequence('jquery-sparkline', 'viewMyProfileCtrl'),
        title: 'User Profile',
        ncyBreadcrumb: {
            label: 'View Profile'
        }
    }).state('app.users.edit_my_profile', {
        url: "/editMyProfile",
        templateUrl: "static/assets/views/edit_my_profile.html",
        resolve: loadSequence('jquery-sparkline', 'editMyProfileCtrl'),
        title: 'Edit Profile',
        ncyBreadcrumb: {
            label: 'Edit Profile'
        }
    }).state('app.users.view_records', {
        url: "/viewRecords",
        templateUrl: "static/assets/views/view_records.html",
        resolve: loadSequence('ngTable', 'viewRecordsCtrl'),
        title: 'View Records',
        ncyBreadcrumb: {
            label: 'View Patient Records'
        }
    }).state('app.users.view_records.patient_consultations', {
        url: "/consultations",
        templateUrl: "static/assets/views/patient_consultations.html",
        resolve: loadSequence('ngTable', 'jquery-sparkline', 'patientConsultationsCtrl'),
        title: 'Patient Consultations',
        ncyBreadcrumb: {
            label: 'Consultations'
        }
    }).state('app.users.view_records.patient_consultations.consultation_details', {
        url: "/consultationDetails",
        templateUrl: "static/assets/views/consultation_details.html",
        resolve: loadSequence('ngTable', 'angularFileUpload', 'consultationDetailsCtrl'),
        title: 'Consultation Details',
        ncyBreadcrumb: {
            label: 'Consultation Details'
        }
    }).state('app.users.consultation_details', {
        url: "/consultationDetails",
        templateUrl: "static/assets/views/consultation_details.html",
        resolve: loadSequence('ngTable', 'angularFileUpload', 'consultationDetailsCtrl'),
        title: 'Consultation Details',
        ncyBreadcrumb: {
            label: 'Consultation Details'
        }
    }).state('error', {
        url: '/error',
        template: '<div ui-view class="fade-in-up"></div>'
    }).state('error.404', {
        url: '/404',
        templateUrl: "static/assets/views/utility_404.html",
    }).state('error.500', {
        url: '/500',
        templateUrl: "static/assets/views/utility_500.html",
    })

	// Login routes

	.state('login', {
       url: '',
       template: '<div ui-view class="fade-in-right-big smooth"></div>',
       abstract: true
   }).state('login.signin', {
       url: '/login',
       templateUrl: "/static/assets/views/patient_login.html",
       resolve: loadSequence('patientLoginCtrl')
   }).state('login.admin_signin', {
       url: '/adminLogin',
       templateUrl: "/static/assets/views/admin_login.html",
       resolve: loadSequence('adminLoginCtrl')
   });


    // Generates a resolve object previously configured in constant.JS_REQUIRES (config.constant.js)
    function loadSequence() {
        var _args = arguments;
        return {
            deps: ['$ocLazyLoad', '$q',
            function ($ocLL, $q) {
             var promise = $q.when(1);
             for (var i = 0, len = _args.length; i < len; i++) {
                 promise = promiseThen(_args[i]);
             }
             return promise;

             function promiseThen(_arg) {
                 if (typeof _arg == 'function') {
                    return promise.then(_arg);
                }
                else {
                 return promise.then(function () {
                     var nowLoad = requiredData(_arg);
                     if (!nowLoad) {
                         return $.error('Route resolve: Bad resource name [' + _arg + ']');
                     }
                     return $ocLL.load(nowLoad);
                 });
             }
         }

         function requiredData(name) {
             if (jsRequires.modules)
                 for (var m in jsRequires.modules)
                     if (jsRequires.modules[m].name && jsRequires.modules[m].name === name) {
                         return jsRequires.modules[m];
                     }
                     return jsRequires.scripts && jsRequires.scripts[name];
                 }
             }]
         };
     }
 }]);