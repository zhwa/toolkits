#!/usr/bin/env python
"""
Basic data structures

Z. Wang
wangzhe0543@gmail.com
"""
class Stack(object):
	def __init__(self):
		self.items = []
	
	def __contains__(self, item):
		if item in self.items:
			return True
		return False

	def __len__(self):
		return len(self.items)

	def isEmpty(self):
		return self.items is []

	def push(self, item):
		self.items.append(item)
	
	def pop(self):
		return self.items.pop()

	def peak(self):
		return self.items[-1]

	def size(self):
		return len(self.items)


class Queue(object):
	def __init__(self):
		self.items = []
	
	def __contains__(self, item):
		if item in self.items:
			return True
		return False

	def __len__(self):
		return len(self.items)

	def isEmpty(self):
		return self.items is []

	def enqueue(self, item):
		self.items.insert(0, item)
	
	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


