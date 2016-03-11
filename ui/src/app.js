/**
 * Created by Aleh on 16.08.2015.
 */
var app = angular.module('TimeSystemApp', ['ui.router', 'ngResource']);

 app.config(function($stateProvider, $urlRouterProvider){

      // For any unmatched url, send to /route1
      $urlRouterProvider.otherwise("/project");

      $stateProvider
        .state('project', {
            url: "/project",
            templateUrl: "ui/src/templates/project/main.html",
            controller: 'ProjectMainController'
        })
          .state('project.list', {
              url: "/list",
              templateUrl: "ui/src/templates/project/project_list.html",
              controller: 'ProjectListController'
          })
            .state('project.list.detail', {
              url: "/:id",
              templateUrl: "ui/src/templates/project/detail.html",
              controller: 'ProjectDetailController'
          })
        .state('login', {
              url: "/login",
              templateUrl: "ui/src/templates/auth/login.html",
              controller: 'LoginController'
          })
        //.state('state2', {
        //    url: "/state2",
        //    templateUrl: "ui/src/templates/state2.html"
        //})
        //  .state('state2.list', {
        //      url: "/list",
        //      templateUrl: "ui/src/templates/state2.project_list.html",
        //      controller: function($scope){
        //        $scope.things = ["A", "Set", "Of", "Things"];
        //      }
        //  })
    });