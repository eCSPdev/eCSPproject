module.exports = {
    standardversion: {
        files: [
            {expand: true, src: "**", cwd: 'bower_components/bootstrap/fonts', dest: "standardversion/assets/fonts"},
            {expand: true, src: "**", cwd: 'bower_components/font-awesome/fonts', dest: "standardversion/assets/fonts"},
            {expand: true, src: "**", cwd: 'bower_components/themify-icons/fonts', dest: "standardversion/assets/css/fonts"},
            {expand: true, src: "**", cwd: 'templates',     dest: "standardversion/templates"},
            {expand: true, src: "**", cwd: 'assets/api',     dest: "standardversion/assets/api"},
            {expand: true, src: "**", cwd: 'assets/i18n',    dest: "standardversion/assets/i18n"},
            {expand: true, src: "**", cwd: 'assets/images',     dest: "standardversion/assets/images"},
            {expand: true, src: "**", cwd: 'assets/js/config',      dest: "standardversion/assets/js/config"},
            {expand: true, src: "**", cwd: 'assets/js/directives',      dest: "standardversion/assets/js/directives"},
            {expand: true, src: "**", cwd: 'assets/js/controllers',      dest: "standardversion/assets/js/controllers"},
            {expand: true, src: "**", cwd: 'assets/js/filters',      dest: "standardversion/assets/js/filters"},
            {expand: true, src: "**", cwd: 'assets/views',     dest: "standardversion/assets/views"},
            {expand: true, src: "**", cwd: 'assets/css/themes',     dest: "standardversion/assets/css/themes"},
            {src: 'master/_index.min.html', dest : 'standardversion/index.html'},
            {src: 'upload.php', dest : 'standardversion/upload.php'}
        ]
    }

};
