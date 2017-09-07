myApp.controller('myProfileController',['$scope','loggedUserInfo',function($scope,loggedUserInfo){
    $scope.userProfileData = loggedUserInfo.userDetails;
    $scope.$on('getUserData',function(){
        $scope.userProfileData = loggedUserInfo.userDetails;
    });
}]);