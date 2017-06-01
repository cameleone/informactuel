myapp = angular.module('app', ['ngResource']);

myapp.factory('Chain', function ($resource) {
    return $resource(
        'http://localhost:8000/api/chains/:id/',
        {},
        {
            'query': {
                method: 'GET',
                isArray: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            },
            'get': {
                method: 'GET'

            },
            'save': {method: 'POST'},
            'update': {method: 'PUT'},
            'remove': {method: 'DELETE'},
            'delete': {method: 'DELETE'}


        },
        {
            stripTrailingSlashes: false
        }
    );
});

myapp.factory('Store', function ($resource) {
    return $resource(
        'http://localhost:8000/api/stores/:id/',
        {id: '@id'},

        {
            stripTrailingSlashes: false
        }
    );
});

myapp.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
}]);


myapp.controller("testCtrl", function ($scope,$http, Chain, Store) {
    $scope.chains = new Chain();
    $scope.stores = new Store();

    $scope.reactualiser = function () {
        Chain.query().$promise.then(function (data) {
            $scope.chains = data;
        });
        Store.query().$promise.then(function (data) {
            $scope.stores = data;
            // console.log('enticipation' + JSON.stringify($scope.stores));
        });
        $scope.chain = new Chain();
    };

    $scope.reactualiser();

  console.log($scope.chains);
    $scope.save = function () {
        $scope.chain.$save();
        $scope.reactualiser();
        console.log('created');
    };


    $scope.search = function () {
        Chain.query().$promise.then(function (data) {
            $scope.chains = data;
            for (i = 0; i < $scope.chains.length; i++) {

                if ($scope.chains[i].name == $scope.name || $scope.chains[i].description == $scope.name) {
                    $scope.chain = $scope.chains[i];
                }
            }

        });
    };


    $scope.modifier = function () {
        $scope.chain.$update({id: $scope.chain.id});
        $scope.reactualiser();
        console.log('updated');
    };

    $scope.supprimer = function () {

        $scope.chain.$delete({id:$scope.chain.id});
        console.log($scope.chain + 'est supprimé');
        $scope.reactualiser();
        console.log('deleted');
    }
});
