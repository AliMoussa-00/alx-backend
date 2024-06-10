import { createClient, print } from 'redis';

const client = createClient();

client.on('connect', () => {
	console.log('Redis client connected to the server');
});
client.on('error', err => {
	console.error(`Redis client not connected to the server: ${err.message}`);
});

const setNewSchool = (schoolName, value) => {
	client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
	client.get(schoolName, (_err, result) => {
		console.log(result);
	});
};


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

