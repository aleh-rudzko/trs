module.exports = function(grunt) {

    // Задачи
    grunt.initConfig({
        // Склеиваем
        ngtemplates: {
            TimeSystemApp: {
                src: ['ui/src/templates/*.html', 'ui/src/templates/**/**.html'],
                dest: 'static/js/templates.js'
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
                    'bower_components/angular-ui-router/release/angular-ui-router.js',
                    'bower_components/bootstrap/dist/bootstrap.js'
                ],
                dest: 'static/common.js'
            },
            application: {
                src: [
                    'ui/src/*.js',
                    'ui/src/**/**.js',
                    'static/js/templates.js'
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

        // Сжимаем
        //uglify: {
        //    main: {
        //        files: {
        //            // Результат задачи concat
        //            'build/scripts.min.js': '<%= concat.main.dest %>'
        //        }
        //    }
        //},
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
            templates: {
                options: {
                    livereload: true,
                    spawn: false
                },
                files: ['ui/src/templates/**/**.html'],
                tasks: ['ngtemplates', 'concat']
            }
        }
    });

    // Загрузка плагинов, установленных с помощью npm install
    grunt.loadNpmTasks('grunt-contrib-concat');
    //grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-angular-templates');

    // Задача по умолчанию
    grunt.registerTask('default', ['ngtemplates','concat', 'watch']);//, 'uglify'*/]);
};