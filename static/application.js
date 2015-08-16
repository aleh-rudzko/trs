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
              templateUrl: "ui/src/templates/project/list.html",
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
        //      templateUrl: "ui/src/templates/state2.list.html",
        //      controller: function($scope){
        //        $scope.things = ["A", "Set", "Of", "Things"];
        //      }
        //  })
    });;/**
 * Created by Aleh on 16.08.2015.
 */
app.controller('LoginController', ['$scope', function($scope) {
    console.log('LoginController');
}]);;/**
 * Created by Aleh on 16.08.2015.
 */

app.controller('ProjectMainController', ['$scope', function($scope){
    console.log('ProjectMainController');
}]);

app.controller('ProjectListController', ['$scope', 'Projects', function ($scope, Projects) {
    $scope.projects = Projects.query();
    console.log($scope.projects);
    console.log('ProjectListController');
}]);

app.controller('ProjectDetailController', ['$scope', '$stateParams', 'Projects', function($scope, $stateParams, Projects) {
    $scope.project = Projects.get({id: $stateParams.id});
    console.log($scope.project)
    console.log('ProjectDetailController');
}]);;/**
 * Created by Aleh on 16.08.2015.
 */

app.factory('Projects', ['$resource', function($resource){
    return $resource('/api/projects/projects/:id', {id: '@id'})
}]);;angular.module('TimeSystemApp').run(['$templateCache', function($templateCache) {
  'use strict';

  $templateCache.put('ui/src/templates/auth/login.html',
    "<form>\r" +
    "\n" +
    "    <div class=\"form-group\">\r" +
    "\n" +
    "        <span>Login</span>\r" +
    "\n" +
    "        <input type=\"text\" class=\"form-control\">\r" +
    "\n" +
    "    </div>\r" +
    "\n" +
    "    <div class=\"form-group\">\r" +
    "\n" +
    "        <span>Password</span>\r" +
    "\n" +
    "        <input type=\"password\" class=\"form-control\">\r" +
    "\n" +
    "    </div>\r" +
    "\n" +
    "    <input type=\"submit\" class=\"btn btn-primary\">\r" +
    "\n" +
    "</form>"
  );


  $templateCache.put('ui/src/templates/project/detail.html',
    "<h3>Detail</h3>\r" +
    "\n" +
    "<div class=\"row\">\r" +
    "\n" +
    "    <div class=\"col-md-12\">\r" +
    "\n" +
    "        <h3>{{ project.name }}</h3>\r" +
    "\n" +
    "        <span>Date start - {{ project.start_date }}</span>\r" +
    "\n" +
    "        <div>{{ project.description }}</div>\r" +
    "\n" +
    "        <span>Date end - {{ project.end_date }}</span>\r" +
    "\n" +
    "    </div>\r" +
    "\n" +
    "\r" +
    "\n" +
    "</div>\r" +
    "\n" +
    "<div ui-view></div>"
  );


  $templateCache.put('ui/src/templates/project/list.html',
    "<h3>List</h3>\r" +
    "\n" +
    "<table class=\"table table-hover\">\r" +
    "\n" +
    "    <tr ui-sref=\"project.list\">\r" +
    "\n" +
    "        <th>Name</th>\r" +
    "\n" +
    "        <th>Description</th>\r" +
    "\n" +
    "        <th>Start date</th>\r" +
    "\n" +
    "        <th>End date</th>\r" +
    "\n" +
    "    </tr>\r" +
    "\n" +
    "    <tr ng-repeat=\"project in projects\" ui-sref=\"project.list.detail({id:{{ project.id }}})\">\r" +
    "\n" +
    "        <td>{{ project.name }}</td>\r" +
    "\n" +
    "        <td>{{ project.description }}</td>\r" +
    "\n" +
    "        <td>{{ project.start_date }}</td>\r" +
    "\n" +
    "        <td>{{ project.end_date }}</td>\r" +
    "\n" +
    "    </tr>\r" +
    "\n" +
    "</table>\r" +
    "\n" +
    "<div ui-view></div>\r" +
    "\n"
  );


  $templateCache.put('ui/src/templates/project/main.html',
    "<h3>Main</h3>\r" +
    "\n" +
    "<div ui-view></div>\r" +
    "\n"
  );

}]);
