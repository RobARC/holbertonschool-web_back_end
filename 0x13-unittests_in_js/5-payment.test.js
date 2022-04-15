const sinon = require('sinon');
const { expect } = require('chai');

const sendPaymentRequestToApi = require('./5-payment');
const Utils = require('./utils');

describe('Hooks',  () => {
  let spyConsole;
  beforeEach( () => {
    spyConsole = sinon.spy(console, 'log');
  });

  afterEach( () => {
    spyConsole.restore();
  });

  it('logs correctly with 100, 20', () => {
    sendPaymentRequestToApi(100, 20);

    expect(spyConsole.calledOnceWithExactly('The total is: 120')).to.be.true;
    expect(spyConsole.calledOnce).to.be.true;
  });

  it('logs correctly with 10, 10', () => {
    sendPaymentRequestToApi(10, 10);

    expect(spyConsole.calledOnceWithExactly('The total is: 20')).to.be.true;
    expect(spyConsole.calledOnce).to.be.true;
  });
});