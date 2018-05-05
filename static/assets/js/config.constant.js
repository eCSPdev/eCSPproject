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
        'modernizr': 'static/bower_components/modernizr/modernizr.js',
        'moment': ['static/bower_components/moment/min/moment.min.js'],
        'spin': 'static/bower_components/spin.js/spin.js',

        //*** jQuery Plugins
        'perfect-scrollbar-plugin': ['static/bower_components/perfect-scrollbar/js/min/perfect-scrollbar.jquery.min.js', 'static/bower_components/perfect-scrollbar/css/perfect-scrollbar.min.css'],
        'ladda': ['static/bower_components/ladda/dist/ladda.min.js', 'static/bower_components/ladda/dist/ladda-themeless.min.css'],
        'sweet-alert': ['static/bower_components/sweetalert/dist/sweetalert.min.js', 'static/bower_components/sweetalert/dist/sweetalert.css'],
        'chartjs': 'static/bower_components/chart.js/dist/Chart.min.js',
        'jquery-sparkline': 'static/bower_components/jquery.sparkline.build/dist/jquery.sparkline.min.js',
        'ckeditor-plugin': 'static/bower_components/ckeditor/ckeditor.js',
        'jquery-nestable-plugin': ['static/bower_components/jquery-nestable/jquery.nestable.js'],
        'touchspin-plugin': ['static/bower_components/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.min.js', 'static/bower_components/bootstrap-touchspin/dist/jquery.bootstrap-touchspin.min.css'],
		'spectrum-plugin': ['static/bower_components/spectrum/spectrum.js', 'static/bower_components/spectrum/spectrum.css'],
		
        //*** Controllers
        'homepageCtrl': 'static/assets/js/controllers/homepageCtrl.js',
        'manageUsersCtrl': 'static/assets/js/controllers/manageUsersCtrl.js',
        'managePatientsCtrl': 'static/assets/js/controllers/managePatientsCtrl.js',
        'manageAssistantsCtrl': 'static/assets/js/controllers/manageAssistantsCtrl.js',
        'addNewUserCtrl': 'static/assets/js/controllers/addNewUserCtrl.js',
        'viewMyProfileCtrl': 'static/assets/js/controllers/viewMyProfileCtrl.js',
        'editMyProfileCtrl': 'static/assets/js/controllers/editMyProfileCtrl.js',
        'viewPatientProfileCtrl': 'static/assets/js/controllers/viewPatientProfileCtrl.js',
        'editPatientProfileCtrl': 'static/assets/js/controllers/editPatientProfileCtrl.js',
        'viewAssistantProfileCtrl': 'static/assets/js/controllers/viewAssistantProfileCtrl.js',
        'editAssistantProfileCtrl': 'static/assets/js/controllers/editAssistantProfileCtrl.js',
        'viewRecordsCtrl': 'static/assets/js/controllers/viewRecordsCtrl.js',
        'patientConsultationsCtrl': 'static/assets/js/controllers/patientConsultationsCtrl.js',
        'consultationDetailsCtrl': 'static/assets/js/controllers/consultationDetailsCtrl.js',
        'loginCtrl': '/static/assets/js/controllers/loginCtrl.js',
        'partialViewCtrl': 'static/assets/js/controllers/partialViewCtrl.js',
        'iconsCtrl': 'static/assets/js/controllers/iconsCtrl.js',
        'ngTableCtrl': 'static/assets/js/controllers/ngTableCtrl.js',
        'toasterCtrl': 'static/assets/js/controllers/toasterCtrl.js',
        'sweetAlertCtrl': 'static/assets/js/controllers/sweetAlertCtrl.js',
        'mapsCtrl': 'static/assets/js/controllers/mapsCtrl.js',
        'nestableCtrl': 'static/assets/js/controllers/nestableCtrl.js',
        'validationCtrl': ['static/assets/js/controllers/validationCtrl.js'],
        'selectCtrl': 'static/assets/js/controllers/selectCtrl.js',
        'wizardCtrl': 'static/assets/js/controllers/wizardCtrl.js',
        'uploadCtrl': 'static/assets/js/controllers/uploadCtrl.js',
        'xeditableCtrl': 'static/assets/js/controllers/xeditableCtrl.js',
        'dynamicTableCtrl': 'static/assets/js/controllers/dynamicTableCtrl.js',
        
        //*** Filters
        'htmlToPlaintext': 'static/assets/js/filters/htmlToPlaintext.js'
    },
    //*** angularJS Modules
    modules: [{
        name: 'angularMoment',
        files: ['static/bower_components/angular-moment/angular-moment.min.js']
    }, {
        name: 'toaster',
        files: ['static/bower_components/AngularJS-Toaster/toaster.js', 'static/bower_components/AngularJS-Toaster/toaster.css']
    }, {
        name: 'angularBootstrapNavTree',
        files: ['static/bower_components/angular-bootstrap-nav-tree/dist/abn_tree_directive.js', 'static/bower_components/angular-bootstrap-nav-tree/dist/abn_tree.css']
    }, {
        name: 'angular-ladda',
        files: ['static/bower_components/angular-ladda/dist/angular-ladda.min.js']
    }, {
        name: 'ngTable',
        files: ['static/bower_components/ng-table/dist/ng-table.min.js', 'static/bower_components/ng-table/dist/ng-table.min.css']
    }, {
        name: 'ui.select',
        files: ['static/bower_components/angular-ui-select/dist/select.min.js', 'static/bower_components/angular-ui-select/dist/select.min.css', 'static/bower_components/select2/dist/css/select2.min.css', 'static/bower_components/select2-bootstrap-css/select2-bootstrap.min.css', 'static/bower_components/selectize/dist/css/selectize.bootstrap3.css']
    }, {
        name: 'ui.mask',
        files: ['static/bower_components/angular-ui-mask/dist/mask.min.js']
    }, {
        name: 'ngImgCrop',
        files: ['static/bower_components/ng-img-crop/compile/minified/ng-img-crop.js', 'static/bower_components/ng-img-crop/compile/minified/ng-img-crop.css']
    }, {
        name: 'angularFileUpload',
        files: ['static/bower_components/angular-file-upload/dist/angular-file-upload.min.js']
    }, {
        name: 'ngAside',
        files: ['static/bower_components/angular-aside/dist/js/angular-aside.min.js', 'static/bower_components/angular-aside/dist/css/angular-aside.min.css']
    }, {
        name: 'truncate',
        files: ['static/bower_components/angular-truncate/src/truncate.js']
    }, {
        name: 'oitozero.ngSweetAlert',
        files: ['static/bower_components/ngSweetAlert/SweetAlert.min.js']
    }, {
        name: 'monospaced.elastic',
        files: ['static/bower_components/angular-elastic/elastic.js']
    }, {
        name: 'ngMap',
        files: ['static/bower_components/ngmap/build/scripts/ng-map.min.js']
    }, {
        name: 'tc.chartjs',
        files: ['static/bower_components/tc-angular-chartjs/dist/tc-angular-chartjs.min.js']
    }, {
        name: 'flow',
        files: ['static/bower_components/ng-flow/dist/ng-flow-standalone.min.js']
    }, {
        name: 'uiSwitch',
        files: ['static/bower_components/angular-ui-switch/angular-ui-switch.min.js', 'static/bower_components/angular-ui-switch/angular-ui-switch.min.css']
    }, {
        name: 'ckeditor',
        files: ['static/bower_components/angular-ckeditor/angular-ckeditor.min.js']
    }, {
        name: 'mwl.calendar',
        files: ['static/bower_components/angular-bootstrap-calendar/dist/js/angular-bootstrap-calendar-tpls.js', 'static/bower_components/angular-bootstrap-calendar/dist/css/angular-bootstrap-calendar.min.css', 'static/assets/js/config/config-calendar.js']
    }, {
        name: 'ng-nestable',
        files: ['static/bower_components/ng-nestable/src/angular-nestable.js']
    }, {
        name: 'vAccordion',
        files: ['static/bower_components/v-accordion/dist/v-accordion.min.js', 'static/bower_components/v-accordion/dist/v-accordion.min.css']
    }, {
        name: 'xeditable',
        files: ['static/bower_components/angular-xeditable/dist/js/xeditable.min.js', 'static/bower_components/angular-xeditable/dist/css/xeditable.css', 'static/assets/js/config/config-xeditable.js']
    }, {
        name: 'checklist-model',
        files: ['static/bower_components/checklist-model/checklist-model.js']
    }, {
        name: 'angular-notification-icons',
        files: ['static/bower_components/angular-notification-icons/dist/angular-notification-icons.min.js', 'static/bower_components/angular-notification-icons/dist/angular-notification-icons.min.css']
    }, {
        name: 'angularSpectrumColorpicker',
        files: ['static/bower_components/angular-spectrum-colorpicker/dist/angular-spectrum-colorpicker.min.js']
    }]
});
