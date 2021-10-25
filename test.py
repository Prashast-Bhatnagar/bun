import surfshop, unittest
# Write your code below:
 
class tests(unittest.TestCase):
	def setUp(self):
		self.cart = surfshop.ShoppingCart()

	def test_add_surfboards1(self):
		msg = self.cart.add_surfboards(1)
		self.assertEqual(msg, 'Successfully added 1 surfboard to cart!')

	def test_add_surfboards234(self):
		for i in range(2,5): 
			msg = self.cart.add_surfboards(i)
			self.assertEqual(msg, f'Successfully added {i} surfboards to cart!')
			self.cart = surfshop.ShoppingCart() # to update self.cart as previous one will already have the previously added surfboards 

	@unittest.skip 
	def test_TooManyBoardsError(self):
		self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards(5))

	# @unittest.expectedFailure 
	def test_apply_locals_discount(self):
		self.cart.apply_locals_discount()
		self.assertTrue(self.cart.locals_discount)

unittest.main()
