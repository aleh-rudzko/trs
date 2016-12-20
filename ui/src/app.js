/**
 * Created by Aleh on 16.08.2015.
 */
var app = angular.module('trs', ['ui.router', 'ui.bootstrap', 'ngResource']);

app.config(function($stateProvider, $urlRouterProvider) {

  // For any unmatched url, redirect to /projects
    $urlRouterProvider.otherwise("/projects");
  //
  // Now set up the states
    $stateProvider
        .state('trs', {
            url: '',
            abstract: true,
            templateUrl: '/static/views/main.html'
        })
        .state('trs.projects', {
            url: "/projects",
            templateUrl: "/static/views/projects/list.html",
            controller: 'ProjectListController',
            resolve: {
                projects: ['ProjectService', '']
            }
        })
            .state('trs.projects.preview', {
                templateUrl: '/static/views/projects/detail.html'
            })
        .state('trs.projects_detail', {
            url: "/projects/:project_id",
            templateUrl: "/static/views/projects/detail.html",
            controller: 'ProjectDetailController'
        })
    //     .state('projects.detail.tasks', {
    //         url: "/tasks",
    //         templateUrl: "/static/tasks/list.html",
    //         controller: function($scope) {
    //             $scope.items = ["A", "List", "Of", "Items"];
    //         }
    //     })
    //     .state('projects.detail.tasks.detail', {
    //         url: "/:task_id",
    //         templateUrl: "/static/tasks/detail.html"
    //     });
        //.state('projects.detail.tasks.detail.reports', {
        //    url: "/list",
        //    templateUrl: "static/partials/state2.list.html",
        //    controller: function($scope) {
        //        $scope.things = ["A", "Set", "Of", "Things"];
        //    }
        //});
});

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.config(['$resourceProvider', function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);