const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
    describe('Two Integers', () => {
        it('should return 4',() => {
            assert.strictEqual(calculateNumber(1,3), 4);
        });
    });
    describe('One round floor', () => {
        it('should return 5',() => {
            assert.strictEqual(calculateNumber(1, 3.7), 5);
        });
    });
    describe('One round floor 2', () => {
        it('should return 4',() => {
            assert.strictEqual(calculateNumber(3.3, 1), 4);
        });
    });
    describe('Two round', () => {
        it('should return 5',() => {
            assert.strictEqual(calculateNumber(1.2, 3.7), 5)
        });
    });
    describe('Two round again', () => {
        it('should return 5',() => {
            assert.strictEqual(calculateNumber(1.5, 3,7), 5);
        });
    });
    describe('Two round reversed', () => {
        it('should return 5',() => {
            assert.strictEqual(calculateNumber(3.7, 1.2), 5);
        });
    });
    describe('Two round again floor both', () => {
        it('should return 3',() => {
            assert.strictEqual(calculateNumber(1.2, 2.1), 3)
        });
    });
});