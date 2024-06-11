const kue = require('kue');

const queue = kue.createQueue();

const blacklistedPhones = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (blacklistedPhones.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
        	return;
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
};

queue.process('push_notification_code_2', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
