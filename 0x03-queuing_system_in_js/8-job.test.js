import createPushNotificationsJobs from './8-job';
import  {expect} from 'chai'


const queue = require('kue').createQueue();

describe('createPushNotificationsJobs', () => {

before(() => {
	queue.testMode.enter();
})

afterEach(() =>{
	queue.testMode.clear();
})

after(() => {
	queue.testMode.exit();
})

it ('testing invalid input', () => {

	 expect(() => createPushNotificationsJobs('not an Array', queue)).to.throw(Error, 'Jobs is not an array');
})

it('testing createPushNotificationsJobs', () => {
	const list = [
    	{
  		phoneNumber: '4153518780',
    		message: 'This is the code 1234 to verify your account'
    	}
	];

	createPushNotificationsJobs(list, queue);

	expect(queue.testMode.jobs.length).to.equal(1);
  	expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  	expect(queue.testMode.jobs[0].data).to.eql(
    	{
  		phoneNumber: '4153518780',
    		message: 'This is the code 1234 to verify your account'
    	}
	);
})
})
