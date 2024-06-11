import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', err => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

const listProducts = [
    { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

const getItemById = (id) => {
    return listProducts.find(product => product.Id === id);
};

const reserveStockById = async (itemId, stock) => {
    await setAsync(itemId, stock);
};

const getCurrentReservedStockById = async (itemId) => {
    const stock = await getAsync(itemId);
    return stock ? parseInt(stock, 10) : null;
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
    res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
    const product = getItemById(parseInt(req.params.itemId, 10));
    if (product) {
        const currentStock = await getCurrentReservedStockById(product.Id);
        res.json({
            "itemId": product.Id,
            "itemName": product.name,
            "price": product.price,
            "initialAvailableQuantity": product.stock,
            "currentQuantity": currentStock !== null ? currentStock : product.stock
        });
    } else {
        res.json({ "status": "Product not found" });
    }
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const product = getItemById(parseInt(req.params.itemId, 10));
    if (product) {
        const currentStock = await getCurrentReservedStockById(product.Id) || product.stock;
        if (currentStock < 1) {
            res.json({ "status": "Not enough stock available", "itemId": product.Id });
        } else {
            try {
                await reserveStockById(product.Id, currentStock - 1);
                res.json({ "status": "Reservation confirmed", "itemId": product.Id });
            } catch (err) {
                res.json({ "status": "Failed to store stock in redis", "error": err.message });
            }
        }
    } else {
        res.json({ "status": "Product not found" });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

