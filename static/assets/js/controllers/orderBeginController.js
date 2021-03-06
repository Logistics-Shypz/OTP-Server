bookingOrderApp.controller('orderBeginController',['$scope','$rootScope','sharedOrderInfo',function($scope,$rootScope,sharedOrderInfo){
    
    console.log("In order begin controller")
    $scope.locationDetails = sharedOrderInfo.locationObj;
    
    $('#shiftingDatepicker').datepicker({
        minDate: new Date(),
        changeMonth: true,
        changeYear: true,
        showAnim : 'clip'
    });
    
    //Initialize with defaults
    $scope.sourceCityNames = ['Bangalore','Delhi','Hyderabad'];
    $scope.destCityNames = ['Bangalore','Delhi','Hyderabad'];    
    $scope.locationDetails.sourcePropType = 'apartment';
    $scope.locationDetails.destPropType = 'apartment';
    $scope.locationDetails.sourcePacking = 'yes';
    $scope.locationDetails.destUnPacking = 'yes';
    $scope.locationDetails.sourceLoading = 'yes';
    $scope.locationDetails.destUnLoading = 'yes';
    $scope.locationDetails.sourceElevator = 'yes';
    $scope.locationDetails.destElevator = 'yes';
    
    $scope.continueArticlePage = function(){
    	console.log($scope.locationDetails);
        //console.log($scope.locationDetails);
        sharedOrderInfo.sendLocationDet($scope.locationDetails);
    };
}]);