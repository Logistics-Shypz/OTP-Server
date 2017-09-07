myApp.controller('orderContactController',['$scope','$rootScope','sharedOrderInfo',function($scope,$rootScope,sharedOrderInfo){
    
    $scope.locationObj = sharedOrderInfo.locationObj;
    $scope.contactDetails = sharedOrderInfo.contactObj;
    $scope.articleObj = sharedOrderInfo.articleObj;

    
    //Get the selected Object
    $scope.confirmDetails = function(){
      console.log($scope.contactDetails);
    };
    
    $scope.$on('getLocationDetails',function(){
        $scope.locationObj = sharedOrderInfo.locationObj;
    });
    
    
    $scope.$on('getArticleDetails',function(){
        $scope.articleObj = sharedOrderInfo.articleObj;
    });
    
    $scope.confirmDetails = function(){
      var finalOrderObj = {};
      finalOrderObj.locationDet = $scope.locationObj;
      finalOrderObj.contactDet  = $scope.contactDetails;
      finalOrderObj.articleDet  = $scope.articleObj;
      sessionStorage.setItem('tempSessObj',JSON.stringify(finalOrderObj));    
      //console.log(finalOrderObj);  
    };
    
}]);