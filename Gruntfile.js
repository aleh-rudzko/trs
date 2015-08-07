module.exports = function(grunt) {

    // Задачи
    grunt.initConfig({
        // Склеиваем
        concat: {
            options: {
                separator: ';'
            },
            common: {
                src: [
                    'bower_components/jquery/dist/jquery.js'
                ],
                dest: 'static/common.js'
            },
            application: {
                src: [
                    'ui/src/app/**/*.js'
                ],
                dest: 'static/application.js'
            },
            css: {
                options: {
                    separator: '\n'
                },
                src: [
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
            concat: {
                files: '<%= concat.main.src %>',
                tasks: 'concat'  // Можно несколько: ['lint', 'concat']
            }
        }
    });

    // Загрузка плагинов, установленных с помощью npm install
    grunt.loadNpmTasks('grunt-contrib-concat');
    //grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Задача по умолчанию
    grunt.registerTask('default', ['concat', 'watch']);//, 'uglify'*/]);
};