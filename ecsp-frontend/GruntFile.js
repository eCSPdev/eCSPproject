module.exports = function(grunt) {
	var gtx = require('gruntfile-gtx').wrap(grunt);

    gtx.loadAuto();

    var gruntConfig = require('./grunt');
    gruntConfig.package = require('./package.json');

    gtx.config(gruntConfig);

    // We need our bower components in order to develop
    gtx.alias('build:standardversion', ['compass:standardversion', 'clean:standardversion', 'copy:standardversion', 'concat:standardversion', 'cssmin:standardversion', 'uglify:standardversion']);

    gtx.alias('release', ['bower-install-simple', 'build:dev', 'bump-commit']);


    // --- Development tasks
    gtx.alias('build:standardcss', ['compass:standardversion']);

    gtx.finalise();
};
