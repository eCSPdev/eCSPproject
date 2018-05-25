'use strict';
/** 
  * controllers used for the dashboard
  */
  app.controller('addNewUserCtrl', ["$scope", "$rootScope", "$state", "$http", function ($scope, $rootScope, $state, $http) {

    /* Redirect user to login page if he or she is not logged in correctly */
    if($rootScope.isLoggedIn == false || $rootScope.isLoggedIn == undefined) {
      $state.go('login.signin');
    }
    else {
      if($rootScope.currentUser.role == 'Patient') {
        $state.go('app.home');
      }
    }

    // Set default (non-required) values for new user
    $scope.newUser = {};
    $scope.newUser.registeredby = $rootScope.currentUser.username;
    $scope.newUser.middlename = '';
    $scope.newUser.insurancecompanyname = '';
    $scope.newUser.aptno = '';
    $scope.newUser.st = '';
    $scope.newUser.email = "";
    $scope.newUser.status = true;

    $scope.tempBirthdate = '';

    if($rootScope.currentUser.role == 'Assistant') {
      $scope.newUser.role = 'patient';
    }

    $scope.addUser = function() {

      var birthdate = new Date($scope.newUser.birthdate);
      var today = new Date();

      if (birthdate >= today || birthdate == 'Invalid Date') {
        alert('Date of birth cannot be later than the current date. Try again.');
        $scope.newUser.birthdate = '';
        return;
      }

      // Save as date
      $scope.tempBirthdate = $scope.newUser.birthdate;
      $scope.newUser.birthdate = birthdate;

      // Create (INSERT) new patient
      if($scope.newUser.role == 'patient')
      {
        if($rootScope.currentUser.role == 'Doctor') {
          /* HTTP POST Request: insertPatient() */
          /* Create new patient */
          $http.post('/Doctor/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.newUser)
          .then(function success(response) {

            if(response.data && response.data.Error == 'A Patient with this information already exist.') {
              alert("A patient with this information exists. Please try again.");
              $scope.newUser.birthdate = $scope.tempBirthdate;
              return;
            }

            else if(response.data && response.data.Error == 'Username is already taken.') {
              alert("Username is already taken. Please try again.");
              $scope.newUser.username = '';
              $scope.newUser.birthdate = $scope.tempBirthdate;
              return;
            }

            else if(response.data && response.data.Error == 'Record Number is already taken.') {
              alert("Record number already exists. Please try again.");
              $scope.newUser.recordno == '';
              $scope.newUser.birthdate = $scope.tempBirthdate;
              return;
            }

            alert("New patient added successfuly!");
            $scope.newUser = response.data;
            $state.go('app.users.manage_users.manage_patients');

          }, function error(response) {

            console.log(response);

            if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }

          });
        }

        else {
          /* HTTP POST Request: insertPatient() */
          /* Create new patient */
          $http.post('/Assistant/eCSP/PatientList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.newUser) 
          .then(function success(response) {
            
            if(response.data && response.data.Error == 'A Patient with this information already exist.') {
              alert("A patient with this information exists. Please try again.");
              $scope.newUser.birthdate = $scope.tempBirthdate;
              return;
            }

            else if(response.data && response.data.Error == 'Username is already taken.') {
              alert("Username is already taken. Please try again.");
              $scope.newUser.username = '';
              $scope.newUser.birthdate = $scope.tempBirthdate;
              return;
            }

            else if(response.data && response.data.Error == 'Record Number is already taken.') {
              alert("Record number already exists. Please try again.");
              $scope.newUser.recordno == '';
              $scope.newUser.birthdate = $scope.tempBirthdate;
              return;
            }

            alert("New patient added successfuly!");
            $scope.newUser = response.data;
            $state.go('app.users.manage_users.manage_patients');

          }, function error(response) {
              if(response.data && response.data.Error == 'Invalid Token') {
                alert("Invalid credentials. Please login again.");
                $state.go('login.signin');
              }

           });
        }
      }

      // Create (INSERT) new assistant
      else
      {
        
        /* HTTP POST Request: insertAssistant() */
        /* Create new assistant */
        $http.post('/Doctor/eCSP/AssistantList?username=' + $rootScope.currentUser.username + '&token=' + $rootScope.currentUser.token, $scope.newUser) 
        .then(function success(response) {

          if(response.data && response.data.Error == 'A Assistant with this information already exist.') {
              alert("An assistant with this information exists. Please try again.");
              $scope.newUser.birthdate = $scope.tempBirthdate;
              return;
           }

          if(response.data && response.data.Error == 'Username is already taken.') {
              alert("Username is already taken. Please try again.");
              $scope.newUser.username = '';
              $scope.newUser.birthdate = $scope.tempBirthdate;
              return;
          }

          alert("New assistant added successfuly!");
          $scope.newUser = response.data;
          $state.go('app.users.manage_users.manage_assistants');

        }, function error(response) {
            if(response.data && response.data.Error == 'Invalid Token') {
              alert("Invalid credentials. Please login again.");
              $state.go('login.signin');
            }

         });
      }

    }

  }]);