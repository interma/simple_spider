var system = require('system');
var webPage = require('webpage');
var page = webPage.create();
var url = system.args[1];
console.log('Url: ' + url);


page.open(url);
page.onLoadFinished = function(status) {
	var content = page.content;
	console.log('Content: ' + content);
	phantom.exit();
};
