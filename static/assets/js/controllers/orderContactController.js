bookingOrderApp.controller('orderContactController',['$scope','$rootScope','$http','$location','$window','sharedOrderInfo','loggedUserInfo',function($scope,$rootScope,$http,$location,$window,sharedOrderInfo,loggedUserInfo){
    
    $scope.locationObj = sharedOrderInfo.locationObj;
    $scope.contactDetails = sharedOrderInfo.contactObj;
    $scope.articleObj = sharedOrderInfo.articleObj;
    $scope.userObj = {};
    $scope.userObj.userDetails = {}; 
    
    
   // $scope.userobj = loggedUserInfo.userObj;
    
    //console.log("The user object is : " + $scope.userobj);
    
    
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
     
      var sessionapi = 'http://localhost:5000/server/session';
      
      $http.get(sessionapi).then(function(response){
    	  
    	  console.log(response.data);
    	  var user_session_name = response.data;
    	  
    	  if(user_session_name == "guest"){
    		  var uobj = {};
    		  uobj.uname = user_session_name;
    		  
    		  $scope.userObj.userDetails = uobj;
    		  
    		  console.log($scope.userObj);
    		  
    		  finalOrderObj.locationDet = $scope.locationObj;
    	      finalOrderObj.contactDet  = $scope.contactDetails;
    	      finalOrderObj.articleDet  = $scope.articleObj;
    	      finalOrderObj.userDet = $scope.userObj;
    	      //sessionStorage.setItem('InContactSubmit',"yes");
    	      sessionStorage.setItem('tempSessObj',JSON.stringify(finalOrderObj));
    	      console.log(finalOrderObj);
    	      
    	     /* $http.get('/orderSummary').then(function(response){
  	    	  	
    	      });*/
    	      
    	      $window.location.href = "/orderSummary";
    	      
    	      
    	  }
    	  else{
    		  var userApi = 'http://localhost:8080/api/users/name/' + user_session_name;
    		  
    		  $http.get(userApi).then(function(response){
    			  var user_id = response.data['User']['id'];
    			  var uobj = {};
        		  uobj.uname = user_session_name;
        		  uobj.uid = user_id;
        		  
        		  $scope.userObj.userDetails = uobj;
        		  console.log($scope.userObj);
        		  
        		  finalOrderObj.locationDet = $scope.locationObj;
        	      finalOrderObj.contactDet  = $scope.contactDetails;
        	      finalOrderObj.articleDet  = $scope.articleObj;
        	      finalOrderObj.userDet = $scope.userObj;
        	      //sessionStorage.setItem('InContactSubmit',"yes");
        	      sessionStorage.setItem('tempSessObj',JSON.stringify(finalOrderObj));
        	      console.log(finalOrderObj);
        	     
        	      var url = $location.absUrl();
        	      console.log(url);
        	      
        	      $window.location.href = "/orderSummary";
        	      
    		  });
    		  
    		  
    		  
    		  
    		  
    	  }
    	  
    	 
    	  
      });
      
      
      //console.log("In final order json");
     
      
      
      
    };
    
}]);