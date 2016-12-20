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
            controller: 'ProjectListController'
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
}]);;/**
 * Created by Aleh on 16.08.2015.
 */
app.controller('LoginController', ['$scope', function($scope) {
    console.log('LoginController');
}]);;/**
 * Created by Aleh on 16.08.2015.
 */

app.controller('MainController', ['$scope', function($scope){
    console.log('MainController');
}]);

app.controller('ProjectListController', ['$scope', '$uibModal','Projects',
    function ($scope, $modal, Projects) {

        $scope.open = function (size) {
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: 'static/modals/myModalContent.html',
                controller: 'ModalInstanceCtrl',
                size: size,
                resolve: {
                    items: function () {
                        return [1, 2];
                    }
                }
            });

            modalInstance.result.then(function (project) {
                $scope.projects.push(project)
            }, function () {
                console.log('Cancel')
            });
      };

        $scope.projects = Projects.query();
        console.log('ProjectListController');
}]);

app.controller('ProjectDetailController', ['$scope', '$stateParams', 'Projects',
    function($scope, $stateParams, Projects) {
        $scope.project = Projects.get({id: $stateParams.project_id});
        console.log('ProjectDetailController');
}]);

app.controller('ModalInstanceCtrl', ['$scope', '$uibModalInstance', 'Projects',
    function ($scope, $modalInstance, Projects) {

        $scope.checkInvalidField = function (field) {
            return field.$dirty && field.$invalid
        };


        $scope.save = function () {
            Projects.save($scope.project, function(data) {
                $modalInstance.close(data);
            });
        };

        $scope.cancel = function () {
            $modalInstance.dismiss('cancel');
        };
        console.log('ModalInstanceCtrl');
}]);;/**
 * Created by Aleh on 16.08.2015.
 */

app.factory('Projects', ['$resource', function($resource){
    return $resource('/api/projects/:id', {id: '@id'})
}]);