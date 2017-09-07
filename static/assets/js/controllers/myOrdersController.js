myApp.controller('myOrdersController',['$scope','sharedOrderInfo',function($scope,sharedOrderInfo){
    $scope.orders=[
        {
            'orderId':'ID07052017205215',
            'orderDate':'07-05-2017',
            'orderData':{
                "locationDet": {
                    "sourcePropType": "apartment",
                    "destPropType": "apartment",
                    "sourcePacking": "yes",
                    "destUnPacking": "yes",
                    "sourceLoading": "yes",
                    "destUnLoading": "yes",
                    "shiftingDate": "07/19/2017",
                    "sourceCity": "Delhi",
                    "destinationCity": "Delhi",
                    "sourceFloorNum": 5,
                    "destFloorNum": 4,
                    "destElevator": "yes",
                    "sourceElevator": "no"
                },
                "contactDet": {
                    "contactName": "Devi",
                    "contactEmail": "ravi@mail.com",
                    "contactMobile": "1234567890",
                    "contactOrigAddr1": "aadr1",
                    "contactOrigAddr2": "addr2",
                    "contactOrigState": "ap",
                    "contactOrigZip": "123",
                    "contactOrigLandmark": "qwe",
                    "contactDestAddr1": "addr3",
                    "contactDestAddr2": "addr4",
                    "contactDestState": "ts",
                    "contactDestZip": "3211",
                    "contactDestLandmark": "rewq"
                },
                "articleDet": {
                    "sizePropType": "1 bhk",
                    "livingSelected": {
                        "0": {
                            "item": true,
                            "count": 4
                        },
                        "6": {
                            "item": true,
                            "count": 6
                        }
                    }
                }
            }
        },
        {
            'orderId':'ID07042017072215',
            'orderDate':'07-04-2017',
            'orderData':''
        }
    ];
    $scope.continueSelectedOrder=function(){
        sharedOrderInfo.locationObj = $scope.orders[0].orderData.locationDet;
        sharedOrderInfo.articleObj = $scope.orders[0].orderData.articleDet;
        sharedOrderInfo.contactObj = $scope.orders[0].orderData.contactDet;
    };
}]);