import express from 'express';


const listProducts = [
	{Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
	{Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
	{Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
	{Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
];

const getItemById = (id) => {
	return listProducts.find(product => product.Id === id)
};


const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
	const products = listProducts.map(product => ({
		"itemId": product.Id,
		"itemName": product.name,
		"price": product.price,
		"initialAvailableQuantity": product.stock
	}));
  res.send(products);
});

app.get('/list_products/:itemId', (req, res) => {

	const product = getItemById(parseInt(req.params.itemId, 10))
	if (product){
		res.send({
			"itemId": product.Id,
			"itemName": product.name,
			"price": product.price,
			"initialAvailableQuantity": product.stock,
			"currentQuantity": product.stock
		});
	}
	else {
		res.send({"status":"Product not found"})
	}
})

app.listen(port);

