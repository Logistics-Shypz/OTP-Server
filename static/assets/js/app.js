'use strict';
var myApp = angular.module('myApp',['ui.router','ui.bootstrap']);

myApp.config(function($stateProvider, $urlRouterProvider,$locationProvider) {
    $urlRouterProvider.otherwise('/');
    $stateProvider
    /*.state('home', {
            url: '/',
            templateUrl : "static/partials/landing.html",
            controller : 'landingController'
        })*/
    .state('order_begin', {
            url: '/order-begin',
            templateUrl: "static/partials/order-begin.html"
        })
    .state('order_article',{           
           url: '/order-article',
           templateUrl: "static/partials/order-article.html"      
        })
    .state('order_contact',{           
           url: '/order-contact',
           templateUrl: "static/partials/order-contact.html"     
        })
    .state('my-orders',{           
           url: '/my-orders',
           templateUrl: "static/partials/my-orders.html"
        })
    .state('my-profile',{           
           url: '/my-profile',
           templateUrl: "static/partials/my-profile.html"        
        })
    .state('loginFb',{           
           url: '/loginFb',
           templateUrl: "static/partials/loginfb.html"       
        })
    .state('confirm_facebook',{
            url: '/confirmFb',
           templateUrl: "static/partials/confirmFb.html"
    }).state('contact',{
            url: '/contact',
           templateUrl: "static/partials/contactus.html" 
    }).state('my-testimonials',{
            url: '/my-testimonials',
           templateUrl: "static/partials/my-testimonials.html"
    });
    $locationProvider.html5Mode(true);
});
/*
var app = angular.module("UserDashboardApp", ["ngRoute"]);
      app.config(function($routeProvider) {
          $routeProvider
          .when("/", {
              templateUrl : "{{url_for('address')}}",
              controller : "addressShypzController"
          })
          .when("/contact", {
              templateUrl : "{{url_for('contact')}}"
          })
          .when("/password", {
              templateUrl : "{{url_for('password')}}"
          })
          .when("/promotions", {
              templateUrl : "{{url_for('promotions')}}"
          });
      });


angular.bootstrap(document.getElementById("UserDashboardNav"), ['UserDashboardApp']);
*/
