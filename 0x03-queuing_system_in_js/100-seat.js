import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
const kue = require('kue');

const client = createClient();
const queue = kue.createQueue();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', err => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

let reservationEnabled = true;

const reserveSeat = async (number) => {
    await setAsync('available_seats', number);
};

const getCurrentAvailableSeats = async () => {
    const seats = await getAsync('available_seats');
    return seats ? seats.toString() : null;
};

const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
    // await reserveSeat(3)
    const seats = await getCurrentAvailableSeats();
    res.json({ "numberOfAvailableSeats": seats !== null ? seats : "50" });
});

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        res.json({ "status": "Reservations are blocked" });
    } else {
        const job = queue.create('reserve_seat').save((err) => {
            if (!err) {
                res.json({ "status": "Reservation in process" });
            } else {
                res.json({ "status": "Reservation failed" });
            }
        });

        job.on('complete', () => {
            console.log(`Seat reservation job ${job.id} completed`);
        });

        job.on('failed', (err) => {
            console.log(`Seat reservation job ${job.id} failed: ${err}`);
        });
    }
});

app.get('/process', async (req, res) => {
    res.json({ "status": "Queue processing" });

    queue.process('reserve_seat', async (job, done) => {
        try {
            let seats = await getCurrentAvailableSeats();
            seats = seats !== null ? parseInt(seats, 10) : 50;
            seats -= 1;

            if (seats < 0) {
                throw new Error('Not enough seats available');
            }

            await reserveSeat(seats);

            if (seats === 0) {
                reservationEnabled = false;
            }

            done();
        } catch (err) {
            done(err);
        }
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

