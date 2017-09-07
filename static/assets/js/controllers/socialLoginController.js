myApp.controller('socialLoginController',['$modal','$scope','getServices','sharedOrderInfo','loggedUserInfo',function($modal,$scope,getServices,sharedOrderInfo,loggedUserInfo){
    //Check user Session
    var sessionApi='/api/loginSession';  
    var sessionCall = getServices.getData(sessionApi);
    sessionCall.then(function(result){
       if((result.session != "null")&&(result.session != "NULL")&&(result.session != undefined)&&(result.session != ''))
           {
               var sessionUserApi = '/api/users/id/'+result.session;
               var activeUser = getServices.getData(sessionUserApi);
               activeUser.then(function(result){
                  loggedUserInfo.pushUserData(result); 
               });
           }
    });
    
    //Get information If User Logs In/ Registers In.
    $scope.loggedUserData = loggedUserInfo.userDetails;
    
    if($scope.loggedUserData.Name == undefined)
        $scope.boolLoggedUser = false;    
    else
        $scope.boolLoggedUser = true;
    
    $scope.$on('getUserData',function(){
        $scope.loggedUserData = loggedUserInfo.userDetails;
        $scope.boolLoggedUser = true;
    });
    
    //Opens Login Modal
    this.loginModal = function() {
      var modalInstance = $modal.open({
        controller: 'loginController',
        templateUrl: 'partials/loginModal.html',
        windowClass : 'loginModalWindow'
      });
    };  
    
    //Logouts current User
    var logoutApi = '/api/logout';
    $scope.logoutUser = function(){
        var logoutCall = getServices.getData(logoutApi);
        logoutCall.then(function(result){
           if((result.session=="NULL") || (result.session == "null")){
               $scope.boolLoggedUser = false; 
               alert('Logged out Successfully')
           }
        });
    }
    
}]);