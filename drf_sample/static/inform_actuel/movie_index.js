/**
 * Created by Administrateur on 03/05/2017.
 */






//Initiate module
myapp = angular.module('app', ['ngResource', 'ngRoute', 'ngYoutubeEmbed']);
jQuery(function ($) {
    $('.field-input').focus(function () {
        $parent = $(this).parent();
        if ($(this).val() == '') {
            $parent.addClass('is-focused');
        }
        $(this).parent().addClass('label-has-text');
    });

    $('.field-input').blur(function () {
        $parent = $(this).parent();
        if ($(this).val() == '') {
            $parent.removeClass('label-has-text');
        }
        $parent.removeClass('is-focused');
    })
});
//Url-Route-redirection
myapp.config(function ($routeProvider) {
    $routeProvider
        .when('/', {templateUrl: '/static/html/home.html'})
        .when('/movie/:id', {
            templateUrl: '/static/html/details.html'
        })
        .otherwise({redirectTo: '/'})
});

//Activate CSRF for Angular
myapp.config(['$httpProvider', function ($httpProvider) {
    // $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);


//Service : Movie-Comment-User-
myapp.factory('Movie', function ($resource) {
    return $resource(
        'http://localhost:8000/api/inform/movies/:id/',
        {id: '@id'},
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

            }
        },
        {
            stripTrailingSlashes: false
        }
    );
});
myapp.factory('Comment', function ($resource) {
    return $resource(
        'http://localhost:8000/api/inform/comments/:id/',
        {id: '@id'},
        {
            'query': {
                method: 'GET',
                isArray: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            },
            'get': {
                method: 'GET',
                isArray: true,
                headers: {
                    'Content-Type': 'application/json'
                }

            },
            'save': {method: 'POST'}
        },
        {
            stripTrailingSlashes: false
        }
    );
});
myapp.factory('Panier', function ($resource) {
    return $resource(
        'http://localhost:8000/api/inform/paniers/:id/',
        {id: '@id'},
        {
            'query': {
                method: 'GET',
                isArray: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            },
            'get': {
                method: 'GET',
                isArray: true,
                headers: {
                    'Content-Type': 'application/json'
                }

            },
            'save': {method: 'POST'}
        },
        {
            stripTrailingSlashes: false
        }
    );
});
myapp.factory('PanierList', function ($resource) {
    return $resource(
        'http://localhost:8000/api/inform/paniersList/:id/',
        {id: '@id'},
        {
            'query': {
                method: 'GET',
                isArray: true,
                headers: {
                    'Content-Type': 'application/json'
                }
            },
            'get': {
                method: 'GET',
                isArray: true,
                headers: {
                    'Content-Type': 'application/json'
                }

            }
        },

        {
            stripTrailingSlashes: false
        }
    );
});
myapp.factory('CurrentUser', function ($resource) {
    return $resource(
        'http://localhost:8000/api/inform/currentUser/',
        {id: '@id'},
        {
            'query': {
                method: 'GET',
                isArray: false,
                headers: {
                    'Content-Type': 'application/json'
                }
            }
        },
        {

            stripTrailingSlashes: false
        }
    );
});
myapp.factory('PagerService', function (Range) {
    var service = {};
    service.GetPager = GetPager;
    return service;
    function GetPager(totalItems, currentPage, pageSize) {
        // default to first page

        currentPage = currentPage || 1;

        // default page size is 10
        pageSize = pageSize || 18;

        // calculate total pages
        var totalPages = Math.ceil(totalItems / pageSize);

        var startPage, endPage;
        if (totalPages <= 10) {
            // less than 10 total pages so show all
            startPage = 1;
            endPage = totalPages;
        } else {
            // more than 10 total pages so calculate start and end pages
            if (currentPage <= 6) {
                startPage = 1;
                endPage = 10;
            } else if (currentPage + 4 >= totalPages) {
                startPage = totalPages - 9;
                endPage = totalPages;
            } else {
                startPage = currentPage - 5;
                endPage = currentPage + 4;
            }
        }

        // calculate start and end item indexes
        var startIndex = (currentPage - 1) * pageSize;
        var endIndex = Math.min(startIndex + pageSize - 1, totalItems - 1);

        // create an array of pages to ng-repeat in the pager control


        var pages = Range.setRange(startPage, endPage + 1);

        // return object with all pager properties required by the view
        return {
            totalItems: totalItems,
            currentPage: currentPage,
            pageSize: pageSize,
            totalPages: totalPages,
            startPage: startPage,
            endPage: endPage,
            startIndex: startIndex,
            endIndex: endIndex,
            pages: pages
        };
    };
});
myapp.filter('startFrom', function () {
    return function (input, start) {
        start = +start; //parse to int
        return input.slice(start);
    }
});

myapp.service('Range', function () {
    this.setRange = function (min, max, step) {
        step = step || 1;
        var input = [];
        for (var i = min; i <= max; i += step) {
            input.push(i);
        }
        return input;
    };
});

//controller - Home Page
myapp.controller("homeCtrl", function ($scope, Movie, $filter, PanierList, CurrentUser, PagerService) {
    jQuery(function ($) {
        $('.field-input').focus(function () {
            $parent = $(this).parent();
            if ($(this).val() == '') {
                $parent.addClass('is-focused');
            }
            $(this).parent().addClass('label-has-text');
        });

        $('.field-input').blur(function () {
            $parent = $(this).parent();
            if ($(this).val() == '') {
                $parent.removeClass('label-has-text');
            }
            $parent.removeClass('is-focused');
        })

        $('.detail').mouseleave(function () {
            $(this).parent().addClass('link-focused');
        })

    });
    $('.bxslider').bxSlider({
        minSlides: 3,
        maxSlides: 15,
        slideWidth: 150,
        slideMargin:15,
        speed:500,
        randomStart:true,
        auto:true,
        tickerHover:true

    });
    $scope.search = function () {
        var def = 'movie';
        $scope.homePageInitMovieList();
    };

    $scope.homePageInitMovieList = function () {

        Movie.query().$promise.then(function (data) {

            $scope.getData = function () {
                var items = [];
                if ($scope.q == undefined || $scope.q == '') {
                    items = data;
                } else {
                    for (i = 0; i < data.length; i++) {
                        var titre = '';
                        titre = data[i].titre.toLowerCase();
                        if (titre.indexOf($scope.q.toLowerCase()) > -1) {
                            items.push(data[i]);
                        } else
                            for (j = 0; j < data[i].acteurs.length; j++) {

                                var nom_act = '';
                                var prenom_act = '';

                                nom_act = data[i].acteurs[j].nom_act.toLowerCase();
                                prenom_act = data[i].acteurs[j].prenom_act.toLowerCase();
                                if (nom_act.indexOf($scope.q.toLowerCase()) > -1 || prenom_act.indexOf($scope.q.toLowerCase()) > -1) {
                                    items.push(data[i]);
                                }
                                if (nom_act.indexOf($scope.q.toLowerCase()) > -1 & prenom_act.indexOf($scope.q.toLowerCase()) > -1) {
                                    items.push(data[i]);
                                }
                            }

                        for (k = 0; k < data[i].realisateurs.length; k++) {
                            var nom_real = '';
                            var prenom_real = '';

                            nom_real = data[i].realisateurs[k].nom_real.toLowerCase();
                            prenom_real = data[i].realisateurs[k].prenom_real.toLowerCase();

                            if (nom_real.indexOf($scope.q.toLowerCase()) > -1 || prenom_real.indexOf($scope.q.toLowerCase()) > -1) {
                                items.push(data[i]);
                            }
                        }
                    }
                }
                return items;
            };

            var moviesItems = [];
            moviesItems = $scope.getData();

            $scope.pager = {};
            $scope.setPage = setPage;

            initController();

            function initController() {
                // initialize to page 1
                $scope.setPage(1);
            }

            function setPage(page) {
                if (page < 1 || page > $scope.pager.totalPages) {
                    return;
                }

                // get pager object from service
                $scope.pager = PagerService.GetPager(moviesItems.length, page);

                // get current page of items
                $scope.movies = moviesItems.slice($scope.pager.startIndex, $scope.pager.endIndex + 1);

                /*return $filter('filter')($scope.movies, $scope.q);*/
            }


        });

        $scope.currentUser = new CurrentUser();
        CurrentUser.query().$promise.then(function (data) {
            $scope.currentUser = data;

            $scope.date = $filter('date')(new Date(), 'yyyy-MM-dd');

            $scope.paniers = new PanierList();
            PanierList.query().$promise.then(function (data) {
                $scope.paniers = data;
            })

        });
    };

    $scope.homePageInitMovieList();

});


//Controller - Page detail
myapp.controller("movieDetailCtrl", function ($scope,
                                              Movie,
                                              Comment,
                                              $routeParams,
                                              Panier,
                                              $location) {

    $scope.getCSRFToken = function () {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, 10) == ('csrftoken' + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(10));
                    break;
                }
            }
        }
        return cookieValue;
    };


    //Init and reload
    $scope.detailPageInitFirst = function () {

        $scope.movieDetail = new Movie();
        Movie.query(function (data) {
            $scope.movieDetail = data[$routeParams.id - 1];
            $scope.videoURL = $scope.movieDetail.url_trailer;
        });
//$scope.movieDetail.url_detail;


        $scope.comments = new Comment();
        Comment.get(movie = $scope.movieDetail).$promise.then(function (data) {
            $scope.comments = data;
        });
        $scope.newComment = new Comment();
        $scope.panier = new Panier();

    };


    $scope.pageReload = function () {
        window.location.reload();
    };

    //Save
    $scope.commenter = function () {
        var movie = {};
        movie = $scope.movieDetail.id;
        $scope.newComment.movie = movie;
        $scope.newComment.$save();
        $scope.comments.push($scope.newComment);
        $scope.newComment = new Comment();
    };

    $scope.louer = function ($event) {
        $event.preventDefault();
        var currentMovie = {};
        currentMovie = $scope.movieDetail.id;
        $scope.panier.movie = currentMovie;
        $scope.panier.$save();
        alert('Panier create');
        $location.path('#/');
    }
});


/*$scope.search = function () {
 Chain.query().$promise.then(function (data) {
 $scope.chains = data;
 for (i = 0; i < $scope.chains.length; i++) {

 if ($scope.chains[i].name == $scope.name || $scope.chains[i].description == $scope.name) {
 $scope.chain = $scope.chains[i];
 }
 }

 });
 };
 */



/* Movie.query().$promise.then(function (data) {

 angular.forEach(data, function (value,key) {
 if(value.id == $routeParams.id){
 $scope.movie = value;
 }
 } );


 });*/
/*var movies  =   Movie.query(function(){
 $scope.movie = movies[$routeParams.id];

 console.log('les movies ' + movies);
 console.log('un movie ' + $scope.movie);*/


/* Movie.get({id: $routeParams.id}).$promise.then(function (data) {
 $scope.movie = data;
 console.log($routeParams.id);
 console.log(data);
 });*/

/*def viw(request):
 if request.user.is_authenticated():
 user = request.user

 OU

 {% if request.user.is_authenticated%} '{{request.user.username}}'
 {%else%}

 SETTING
 TEMPLATE_CONTEXT_PROCESSORS = (
 'django.core.context_processors.request',

 */