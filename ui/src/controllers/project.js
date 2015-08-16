/**
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
}]);