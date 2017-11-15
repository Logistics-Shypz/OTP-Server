bookingOrderApp.controller('orderArticleController',['$scope','$rootScope','sharedOrderInfo','getServices',function($scope,$rootScope,sharedOrderInfo,getServices){
    
	
	console.log("in order article controller");
    //Call Articles Data from items Service
    var callArticlesData = getServices.getData('http://localhost:8082/api/v1/items');
    callArticlesData.then(function(result){
       $scope.articlesData = result; 
       console.log($scope.articlesData);
    });
    
    
    //Check if articles selected Data is available for the logged user.
    $scope.orderArticleDetails = sharedOrderInfo.articleObj;    
    
    
    
    
    //Proceed to Contact Details Page
    $scope.proceedContact = function(){
    	console.log($scope.orderArticleDetails);
        sharedOrderInfo.sendArticleDet($scope.orderArticleDetails);
    };
    
    //Make First Tab Active & Show First tab results
    $scope.activeblock = 1;
    $scope.setBlock = function(id){
        $scope.activeblock = id;
    }
    $scope.showBlock = function(id){
        if($scope.activeblock == id){
            return true;
        }
        else
            return false;
    }
}]);