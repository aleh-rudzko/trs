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
        .state('projects', {
            url: "/projects",
            templateUrl: "static/projects/list.html",
            controller: 'ProjectListController'
        })
        .state('projects.detail', {
            url: "/:project_id",
            templateUrl: "static/projects/detail.html",
            controller: 'ProjectDetailController'
        })
        .state('projects.detail.tasks', {
            url: "/tasks",
            templateUrl: "static/tasks/list.html",
            controller: function($scope) {
                $scope.items = ["A", "List", "Of", "Items"];
            }
        })
        .state('projects.detail.tasks.detail', {
            url: "/:task_id",
            templateUrl: "static/tasks/detail.html"
        });
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
}]);;angular.module('trs').run(['$templateCache', function($templateCache) {
  'use strict';

  $templateCache.put('ui/src/templates/auth/login.html',
    "<form>\n" +
    "    <div class=\"form-group\">\n" +
    "        <span>Login</span>\n" +
    "        <input type=\"text\" class=\"form-control\">\n" +
    "    </div>\n" +
    "    <div class=\"form-group\">\n" +
    "        <span>Password</span>\n" +
    "        <input type=\"password\" class=\"form-control\">\n" +
    "    </div>\n" +
    "    <input type=\"submit\" class=\"btn btn-primary\">\n" +
    "</form>"
  );


  $templateCache.put('ui/src/templates/project/detail.html',
    "<h3>Detail</h3>\n" +
    "<div class=\"row\">\n" +
    "    <div class=\"col-md-12\">\n" +
    "        <h3>{{ project.name }}</h3>\n" +
    "        <span>Date start - {{ project.start_date }}</span>\n" +
    "        <div>{{ project.description }}</div>\n" +
    "        <span>Date end - {{ project.end_date }}</span>\n" +
    "    </div>\n" +
    "\n" +
    "</div>\n" +
    "<div ui-view></div>"
  );


  $templateCache.put('ui/src/templates/project/list.html',
    "<h3>List</h3>\n" +
    "<table class=\"table table-hover\">\n" +
    "    <tr ui-sref=\"project.list\">\n" +
    "        <th>Name</th>\n" +
    "        <th>Description</th>\n" +
    "        <th>Start date</th>\n" +
    "        <th>End date</th>\n" +
    "    </tr>\n" +
    "    <tr ng-repeat=\"project in projects\" ui-sref=\"project.list.detail({id:{{ project.id }}})\">\n" +
    "        <td>{{ project.name }}</td>\n" +
    "        <td>{{ project.description }}</td>\n" +
    "        <td>{{ project.start_date }}</td>\n" +
    "        <td>{{ project.end_date }}</td>\n" +
    "    </tr>\n" +
    "</table>\n" +
    "<div ui-view></div>\n"
  );


  $templateCache.put('ui/src/templates/project/main.html',
    "<h3>Main</h3>\n" +
    "<div ui-view></div>\n"
  );

}]);
