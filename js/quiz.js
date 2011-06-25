var getResults = (function () {
	var arr = ['\x62', '\x61', '\x63', '\x63', '\x64', '\x63', '\x62', '\x64', '\x64', '\x62'];
	return function () {
		var result = document.getElementById('results'),
			count = 0,
			mistakes = [],
			i, len;
			
		for (i = 0, len = arr.length; i < len; i++) {
			if (!document.getElementById('answer_' + i + '_' + arr[i]).checked) {
				count++;
				mistakes.push(' #' + (i + 1)); 
			}  
		}
		result.innerHTML = 'You have got ' + count + ' mistake' + (count == 1 ? '' : 's') +
						   '<br \/>' + mistakes.join();   
	};
})();
