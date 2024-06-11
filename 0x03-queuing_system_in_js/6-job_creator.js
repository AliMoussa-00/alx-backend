const kue = require('kue');

const queue = kue.createQueue();

const noti = {
  phoneNumber: '123456789',
  message: 'Notification Message',
};

const job = queue.create('push_notification_code', noti)
  .save((err) => {
    if (!err) console.log(`Notification job created: ${job.id}`);
  });

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
