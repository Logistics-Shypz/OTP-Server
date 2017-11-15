myApp.service('apiServices',['$http',function($http){
    this.callApiPostService = function(postServiceObj,apiPath){
        $http({
                method: 'POST',
                url: apiPath,
                headers: {'Content-Type':'application/json'},
                data : postServiceObj            
            }).success(function(response,status){
                if(response.length == 0)
                {
                    alert(response);
                    return response;
                }
                else if(response.length > 0)
                {
                   alert(response);
                    return response;
                }
            }).error(function(data,status){
                console.log('Login Error:'+status);alert(status);
            });  
    };
    this.callApiGetService = function(apiPath){ 
        $http({
                method: 'GET',
                url: apiPath,
                //headers: {'Content-Type':undefined},            
            }).success(function(response,status){
                if(response.length == 0)
                {
                    return response;
                }
                else if(response.length > 0)
                {
                   return response;
                }
            }).error(function(data,status){
                console.log('Login Error:'+status);alert(status);
            });  
    };
    this.callFacebookApi = function(apiPath){
        $http({
                method: 'POST',
                url: apiPath,
                //headers: {'Content-Type':undefined},            
            }).success(function(response,status){
                if(response.length == 0)
                {
                    alert(response);
                }
                else if(response.length > 0)
                {
                   alert(response);
                }
            }).error(function(data,status){
                console.log('Login Error:'+status);alert(status);
            }); 
    };
}]); 

bookingOrderApp.factory('getServices',function($http){
   var getData = function(apiPath){
        return $http({method:"GET", url:apiPath}).then(function(result){            
            return result.data;
        });  
   };
   return {getData : getData};
});

myApp.factory('postServices',function($http){
   var postData = function(apiPath,dataObj){
        return $http({method:"POST", url:apiPath, data:dataObj}).then(function(result){            
            return result.data;
        });  
   };
   return {postData : postData};
});

bookingOrderApp.factory('loggedUserInfo',['$rootScope',function($rootScope){
    var userObj = {};
    userObj.userDetails = {}; 
    userObj.pushUserData = function(obj){
      this.userDetails = obj;  
      this.broadCastUserDetails();
    };
    userObj.broadCastUserDetails = function(){
        $rootScope.$broadcast('getUserData');
    }
    return userObj;
}]);

bookingOrderApp.factory('sharedOrderInfo',['$rootScope',function($rootScope){
    var orderObj = {};
    orderObj.locationObj = {};
    orderObj.articleObj = {};
    orderObj.contactObj = {};
    sessionStorage.getItem('tempSessObj');
    orderObj.sendLocationDet = function(obj){
        this.locationObj = obj;
        this.broadCastLocation();
    };
    orderObj.broadCastLocation = function(){
        $rootScope.$broadcast('getLocationDetails');
    };
    orderObj.sendArticleDet = function(obj){
        this.articleObj = obj;
        this.broadCastArticles();
    };
    orderObj.broadCastArticles = function(){
        $rootScope.$broadcast('getArticleDetails');
    };   

    console.log(orderObj);
    return orderObj;

}]);