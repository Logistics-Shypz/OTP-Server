myApp.controller('loginController',['$scope','$modalInstance','apiServices', 'postServices','loggedUserInfo',function($scope,$modalInstance,apiServices,postServices,loggedUserInfo){
    $scope.registerCheck = false;
    $scope.close = function () {
        $modalInstance.close();
    };
    var loginApi='/api/login';
    var registerApi = '/api/registerUser';
    var fbApi = '/connect/facebook';
    var googleApi = '/api/google';
    var registerUserResponse,loginUserResponse;    
    
    $scope.userLogin = function(loginObj){          
        var loginCall = postServices.postData(loginApi,loginObj);
        loginCall.then(function(result){
            if((result.Name!=undefined) && (result.Name!=null)){
                $scope.close();
                loggedUserInfo.pushUserData(result);
            }
            else if(result.Error!=undefined){
                alert('Invalid User/Password. Please try again.');
            }
        });
    }; 
    
    $scope.userRegister = function(registerObj){   
       if(registerObj.password == $scope.registerConfirmPassword){               
            var registerCall = postServices.postData(registerApi,registerObj);
            registerCall.then(function(result){
            if((result!=undefined) && (result!=null)){
                $scope.close();
                alert('You have successfully Registered');
            }
        });
        }
        else
            alert('Passwords mismatch');
    };
    
    $scope.signUpFB = function(){    
        $scope.close();
    };
    $scope.signUpGoogle = function(){        
        googleApiResponse = apiServices.callApiGetService(googleApi);
    };
    
}]);



 //{"mobile":"3883838", "email":"mukesh@gmail.com", "password":"123456", "username":"mukesh"}