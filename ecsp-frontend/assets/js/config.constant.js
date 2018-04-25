'use strict';

/**
 * Config constant
 */
app.constant('APP_MEDIAQUERY', {
    'desktopXL': 1200,
    'desktop': 992,
    'tablet': 768,
    'mobile': 480
});
app.constant('JS_REQUIRES', {
    //*** Scripts
    scripts: {
        //*** Javascript Plugins
        'modernizr': ['bower_components/modernizr/modernizr.js'],
        'moment': ['bower_components/moment/min/moment.min.js'],
        'spin': 'bower_components/spin.js/spin.js',

        //*** jQuery Plugins
        'perfect-scrollbar-plugin': ['bower_components/perfect-scrollbar/js/min/perfect-scrollbar.jquery.min.js', 'bower_components/perfect-scrollbar/css/perfect-scrollbar.min.css'],
        'ladda': ['bower_components/ladda/dist/ladda.min.js', 'bower_components/ladda/dist/ladda-themeless.min.css'],
        'sweet-alert': ['bower_components/sweetalert/dist/sweetalert.min.js', 'bower_components/sweetalert/dist/sweetalert.css'],
        'chartjs': 'bower_components/chart.js/dist/Chart.min.js',
        'jquery-sparkline': 'bower_components/jquery.sparkline.build/dist/jquery.sparkline.min.js',
        'ckeditor-plugin': 'bower_components/ckeditor/ckeditor.js',
        'jquery-nestable-plugin': ['bower_components/jquery-nestable/jquery.nestable.js'],
        'touchspin-plugin': ['bower_components/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.min.js', 'bower_components/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.min.css'],
		'spectrum-plugin': ['bower_components/spectrum/spectrum.js', 'bower_components/spectrum/spectrum.css'],
		
        //*** Controllers
        'homepageCtrl': 'assets/js/controllers/homepageCtrl.js',
        'manageUsersCtrl': 'assets/js/controllers/manageUsersCtrl.js',
        'managePatientsCtrl': 'assets/js/controllers/managePatientsCtrl.js',
        'manageAssistantsCtrl': 'assets/js/controllers/manageAssistantsCtrl.js',
        'addNewUserCtrl': 'assets/js/controllers/addNewUserCtrl.js',
        'viewMyProfileCtrl': 'assets/js/controllers/viewMyProfileCtrl.js',
        'editMyProfileCtrl': 'assets/js/controllers/editMyProfileCtrl.js',
        'viewPatientProfileCtrl': 'assets/js/controllers/viewPatientProfileCtrl.js',
        'editPatientProfileCtrl': 'assets/js/controllers/editPatientProfileCtrl.js',
        'viewAssistantProfileCtrl': 'assets/js/controllers/viewAssistantProfileCtrl.js',
        'editAssistantProfileCtrl': 'assets/js/controllers/editAssistantProfileCtrl.js',
        'viewRecordsCtrl': 'assets/js/controllers/viewRecordsCtrl.js',
        'patientConsultationsCtrl': 'assets/js/controllers/patientConsultationsCtrl.js',
        'consultationDetailsCtrl': 'assets/js/controllers/consultationDetailsCtrl.js',
        'loginCtrl': 'assets/js/controllers/loginCtrl.js',
        'partialViewCtrl': 'assets/js/controllers/partialViewCtrl.js',
        'iconsCtrl': 'assets/js/controllers/iconsCtrl.js',
        'ngTableCtrl': 'assets/js/controllers/ngTableCtrl.js',
        'toasterCtrl': 'assets/js/controllers/toasterCtrl.js',
        'sweetAlertCtrl': 'assets/js/controllers/sweetAlertCtrl.js',
        'mapsCtrl': 'assets/js/controllers/mapsCtrl.js',
        'nestableCtrl': 'assets/js/controllers/nestableCtrl.js',
        'validationCtrl': ['assets/js/controllers/validationCtrl.js'],
        'selectCtrl': 'assets/js/controllers/selectCtrl.js',
        'wizardCtrl': 'assets/js/controllers/wizardCtrl.js',
        'uploadCtrl': 'assets/js/controllers/uploadCtrl.js',
        'xeditableCtrl': 'assets/js/controllers/xeditableCtrl.js',
        'dynamicTableCtrl': 'assets/js/controllers/dynamicTableCtrl.js',
        
        //*** Filters
        'htmlToPlaintext': 'assets/js/filters/htmlToPlaintext.js'
    },
    //*** angularJS Modules
    modules: [{
        name: 'angularMoment',
        files: ['bower_components/angular-moment/angular-moment.min.js']
    }, {
        name: 'toaster',
        files: ['bower_components/AngularJS-Toaster/toaster.js', 'bower_components/AngularJS-Toaster/toaster.css']
    }, {
        name: 'angularBootstrapNavTree',
        files: ['bower_components/angular-bootstrap-nav-tree/dist/abn_tree_directive.js', 'bower_components/angular-bootstrap-nav-tree/dist/abn_tree.css']
    }, {
        name: 'angular-ladda',
        files: ['bower_components/angular-ladda/dist/angular-ladda.min.js']
    }, {
        name: 'ngTable',
        files: ['bower_components/ng-table/dist/ng-table.min.js', 'bower_components/ng-table/dist/ng-table.min.css']
    }, {
        name: 'ui.select',
        files: ['bower_components/angular-ui-select/dist/select.min.js', 'bower_components/angular-ui-select/dist/select.min.css', 'bower_components/select2/dist/css/select2.min.css', '../bower_components/select2-bootstrap-css/select2-bootstrap.min.css', '../bower_components/selectize/dist/css/selectize.bootstrap3.css']
    }, {
        name: 'ui.mask',
        files: ['bower_components/angular-ui-mask/dist/mask.min.js']
    }, {
        name: 'ngImgCrop',
        files: ['bower_components/ng-img-crop/compile/minified/ng-img-crop.js', 'bower_components/ng-img-crop/compile/minified/ng-img-crop.css']
    }, {
        name: 'angularFileUpload',
        files: ['bower_components/angular-file-upload/dist/angular-file-upload.min.js']
    }, {
        name: 'ngAside',
        files: ['bower_components/angular-aside/dist/js/angular-aside.min.js', 'bower_components/angular-aside/dist/css/angular-aside.min.css']
    }, {
        name: 'truncate',
        files: ['bower_components/angular-truncate/src/truncate.js']
    }, {
        name: 'oitozero.ngSweetAlert',
        files: ['bower_components/ngSweetAlert/SweetAlert.min.js']
    }, {
        name: 'monospaced.elastic',
        files: ['bower_components/angular-elastic/elastic.js']
    }, {
        name: 'ngMap',
        files: ['bower_components/ngmap/build/scripts/ng-map.min.js']
    }, {
        name: 'tc.chartjs',
        files: ['bower_components/tc-angular-chartjs/dist/tc-angular-chartjs.min.js']
    }, {
        name: 'flow',
        files: ['bower_components/ng-flow/dist/ng-flow-standalone.min.js']
    }, {
        name: 'uiSwitch',
        files: ['bower_components/angular-ui-switch/angular-ui-switch.min.js', 'bower_components/angular-ui-switch/angular-ui-switch.min.css']
    }, {
        name: 'ckeditor',
        files: ['bower_components/angular-ckeditor/angular-ckeditor.min.js']
    }, {
        name: 'mwl.calendar',
        files: ['bower_components/angular-bootstrap-calendar/dist/js/angular-bootstrap-calendar-tpls.js', 'bower_components/angular-bootstrap-calendar/dist/css/angular-bootstrap-calendar.min.css', 'assets/js/config/config-calendar.js']
    }, {
        name: 'ng-nestable',
        files: ['bower_components/ng-nestable/src/angular-nestable.js']
    }, {
        name: 'vAccordion',
        files: ['bower_components/v-accordion/dist/v-accordion.min.js', 'bower_components/v-accordion/dist/v-accordion.min.css']
    }, {
        name: 'xeditable',
        files: ['bower_components/angular-xeditable/dist/js/xeditable.min.js', 'bower_components/angular-xeditable/dist/css/xeditable.css', 'assets/js/config/config-xeditable.js']
    }, {
        name: 'checklist-model',
        files: ['bower_components/checklist-model/checklist-model.js']
    }, {
        name: 'angular-notification-icons',
        files: ['bower_components/angular-notification-icons/dist/angular-notification-icons.min.js', 'bower_components/angular-notification-icons/dist/angular-notification-icons.min.css']
    }, {
        name: 'angularSpectrumColorpicker',
        files: ['bower_components/angular-spectrum-colorpicker/dist/angular-spectrum-colorpicker.min.js']
    }]
});
