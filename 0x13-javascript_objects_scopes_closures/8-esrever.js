#!/usr/bin/node
module.exports = {
	esrever (list) {
		newlist = []
		for (el of list) {
			newlist = [el, ...newlist]
		}
		return newlist;
	}
}
