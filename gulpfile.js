var autoprefixer = require('autoprefixer-core');
var babelify = require('babelify');
var browserify = require('browserify');
var browserifyShim = require('browserify-shim');
var concat = require('gulp-concat');
var gulp = require('gulp');
var haml = require('gulp-haml');
var less = require('gulp-less');
var livereload = require('gulp-livereload');
var notify = require('gulp-notify');
var path = require('path');
var source = require('vinyl-source-stream');
var watchify = require('watchify');
var $ = require('gulp-load-plugins')();
var _ = require('underscore');

const files = {
    bundle: 'app.js',
    bundle_min: 'app.min.js',
    entry: 'main.js',
    lib: 'lib.min.js',
    less_entry: 'application.less'
};


ROOT = './andalen'
PROJ_ROOT = ROOT + '/static'

const paths = {
    bower: PROJ_ROOT + '/js/bower_components/**/*.*',
    bundle: PROJ_ROOT + '/js/dist/' + files.bundle,
    bundle_min: PROJ_ROOT + '/js/dist/' + files.bundle_min,
    css: PROJ_ROOT + '/css',
    less: PROJ_ROOT + '/less/**/*.less',
    less_entry: PROJ_ROOT + '/less/' + files.less_entry,
    dist: PROJ_ROOT + '/js/dist',
    haml: ROOT + '/templates/haml/**/*.haml',
    html: ROOT + '/templates/html',
    lib: PROJ_ROOT + '/js/lib',
    react: PROJ_ROOT + '/js/app/**/*.jsx',
    root: PROJ_ROOT + '/js/app',
    scripts: PROJ_ROOT + '/js/app/**/*.js',
    styles: PROJ_ROOT + '/less/*.less',
    tests: PROJ_ROOT + '/js/app/**/*.test.*'
};

var dependencies = [
  'jquery.min.js',
  'lodash.min.js',
  'pubsub.js',
  'chance.min.js',
  'backbone.min.js',
  'react-addons.js',
  'semantic.min.js',
  'mustache.min.js',
  'moment.min.js',
  'highcharts.src.js'
  //'highmaps.js'
]
dependencies = _.map(dependencies, function(x) { return paths.lib + '/' + x });

function not(path) {
    return '!' + path;
}

gulp.task('styles', function() {
  return gulp.src(paths.less_entry)

    .pipe(less({
          paths: [ path.join(__dirname, 'less', 'includes') ]
        }))
    .pipe(gulp.dest(paths.css))
    .pipe(notify({ message: 'styles task complete' }));
}); 

gulp.task('templates', function() {
  return gulp.src(paths.haml)
    .pipe(haml({ ugly: false }))
    .pipe(gulp.dest(paths.html))
    .pipe(notify({ message: 'templates task complete' }));
});

//gulp.task('lint', function() {
  //gulp.src([paths.scripts, paths.react, not(paths.tests), not(path.resolve(paths.root, files.bundle)), not(paths.bower)])
    //.pipe($.babel())
    //.pipe($.jshint())
    //.pipe($.jshint.reporter('default', { verbose: true }))
    //.pipe($.jshint.reporter('fail'));
//});

gulp.task('js:lib', function() {
  return gulp.src(dependencies)
    .pipe(concat(files.lib))
    .pipe(gulp.dest(paths.dist))
    .pipe(notify({ message: 'js:lib task complete' }));
});

gulp.task('bundle', function() {
    var bundle = browserify({
            debug: true,
            extensions: ['.js', '.jsx'],
            entries: path.resolve(paths.root, files.entry)
        });

    return executeBundle(bundle);
});

gulp.task('js:app', function() {
    var bundle = browserify({
        debug: true,
        extensions: ['.js', '.jsx'],
        entries: path.resolve(paths.root, files.entry),
        cache: {},
        packageCache: {}
    });
    bundle = watchify(bundle, { poll: 100 });
    bundle.transform(babelify.configure({
        //ignore: /(lib)/
    }));
    bundle.on('update', function(){
        console.log('starting rebundle..');
        executeBundle(bundle);
    });
    return executeBundle(bundle);
});

function executeBundle(bundle) {
    var start = Date.now();
    bundle
        .bundle()
        .on("error", function (err) { console.log("Error : " + err.message); })
        .pipe(source(files.bundle))
        .pipe(gulp.dest(paths.dist))
        .pipe($.notify(function() {
            console.log('bundle finished in ' + (Date.now() - start) + 'ms');
        }))
        .pipe($.filter(files.bundle));
}

gulp.task('clean', function() {
    gulp.src(path.resolve(paths.dist, '*'))
        .pipe($.clean({force: true}));
});

gulp.task('js:app:minify', function() {
    gulp.src(paths.bundle)
        .pipe($.uglify())
        .pipe(concat(files.bundle_min))
        .pipe(gulp.dest(paths.dist))
        .pipe($.size({
            showFiles: true,
            title: 'js:app:minify:'
        }));
});

gulp.task('watch', function() {
  gulp.watch([paths.scripts, paths.react, '!'+ PROJ_ROOT +'js/app/main.js'], ['js:app']);
  // gulp.watch([paths.scripts, paths.react, '!'+ PROJ_ROOT +'js/app/main.js'], ['js:app', 'js:app:minify']);
  gulp.watch([paths.lib], ['js:lib']);
  gulp.watch([paths.haml], ['templates']);
  gulp.watch([paths.less], ['styles']);

  livereload.listen();
  dirs = [
      ROOT + '/**/*.py',
      PROJ_ROOT + '/js/**/*.js',
      PROJ_ROOT + '/css/**/*.css',
      ROOT + '/templates/html/**/*.html',
    ]
  gulp.watch(dirs).on('change', livereload.changed);

});

gulp.task('dev',
    ['watch']
);

gulp.task('default', ['dev']);

