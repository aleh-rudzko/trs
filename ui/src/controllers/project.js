/**
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
}]);