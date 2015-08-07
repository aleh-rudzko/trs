module.exports = function(grunt) {

    // ������
    grunt.initConfig({
        // ���������
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
        // �������
        //uglify: {
        //    main: {
        //        files: {
        //            // ��������� ������ concat
        //            'build/scripts.min.js': '<%= concat.main.dest %>'
        //        }
        //    }
        //},
        watch: {
            concat: {
                files: '<%= concat.main.src %>',
                tasks: 'concat'  // ����� ���������: ['lint', 'concat']
            }
        }
    });

    // �������� ��������, ������������� � ������� npm install
    grunt.loadNpmTasks('grunt-contrib-concat');
    //grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // ������ �� ���������
    grunt.registerTask('default', ['concat', 'watch']);//, 'uglify'*/]);
};