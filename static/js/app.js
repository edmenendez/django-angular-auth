// Declare app level module which depends on filters, and services
angular.module(
    'myApp', [
        'myApp.filters', 'myApp.services', 'myApp.directives',
        'http-auth-interceptor', 'ngCookies'
    ]
)

.config(function($httpProvider) {
  $httpProvider.defaults.headers.common['Authorization'] = 'ApiKey ' +
    $.cookie('username') + ':' + $.cookie('key');
})

.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/view1', {templateUrl: 'partials/partial1.html', controller: MyCtrl1});
    $routeProvider.when('/view2', {templateUrl: 'partials/partial2.html', controller: MyCtrl2});
    $routeProvider.otherwise({redirectTo: '/view1'});
}])

.directive('authDemoApplication', function() {
    return {
      restrict: 'C',
      link: function(scope, elem, attrs) {
        //once Angular is started, remove class:
        elem.removeClass('waiting-for-angular');

        var login = elem.find('#login-holder');
        var main = elem.find('#content');

        login.hide();

        scope.$on('event:auth-loginRequired', function() {
          login.slideDown('slow', function() {
            main.hide();
          });
        });
        scope.$on('event:auth-loginConfirmed', function() {
          main.show();
          login.slideUp();
        });
      }
    };
  });
