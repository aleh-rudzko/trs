/**
 * Created by Aleh on 16.08.2015.
 */

app.factory('Projects', ['$resource', function($resource){
    return $resource('/api/projects/projects/:id', {id: '@id'})
}]);