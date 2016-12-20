module.exports = function(grunt) {

    //
    grunt.initConfig({
        //
        //ngtemplates: {
        //    trs: {
        //        src: ['ui/src/templates/*.html', 'ui/src/templates/**/**.html'],
        //        dest: 'static/js/templates.js'
        //    }
        //},
        copy: {
            files: {
                cwd: 'ui/src/templates',  // set working folder / root to copy
                src: '**/*',           // copy all files and subfolders
                dest: 'static/views',    // destination folder
                expand: true           // required when using cwd
            }
        },
        concat: {
            options: {
                separator: ';'
            },
            common: {
                src: [
                    'bower_components/jquery/dist/jquery.js',
                    'bower_components/angular/angular.js',
                    'bower_components/angular-resource/angular-resource.js',
                    'bower_components/angular-ui-router/release/angular-ui-router.min.js',
                    'bower_components/bootstrap/dist/bootstrap.js',
                    'bower_components/angular-bootstrap/ui-bootstrap.min.js',
                    'bower_components/angular-bootstrap/ui-bootstrap-tpls.min.js'
                ],
                dest: 'static/common.js'
            },
            application: {
                src: [
                    'ui/src/*.js',
                    'ui/src/**/**.js',
                    //'ui/src/app/**/*.js'
                ],
                dest: 'static/application.js'
            },
            css: {
                options: {
                    separator: '\n'
                },
                src: [
                    'bower_components/bootstrap/dist/css/bootstrap.css',
                    'ui/css/*.css'
                ],
                dest: 'static/main.css'
            }
        },
        watch: {
            css: {
                options: {
                    livereload: true,
                    spawn: false
                },
                files: [
                    'ui/css/*.css'
                ],
                tasks: ['concat']
            },
            js: {
                options: {
                    livereload: true,
                    spawn: false
                },
                files: [
                    'ui/src/**/*.js',
                    'Gruntfile.js',
                    'bower.json'
                ],
                tasks: ['concat']
            },
            //templates: {
            //    options: {
            //        livereload: true,
            //        spawn: false
            //    },
            //    files: ['ui/src/templates/**/**.html'],
            //    tasks: ['ngtemplates', 'concat']
            //}
        }
    });

    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-copy');
    //grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-angular-templates');

    grunt.registerTask('default', ['concat', 'copy', 'watch']);//'ngtemplates', 'uglify'*/]);
};