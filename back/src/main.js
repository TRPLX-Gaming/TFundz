"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const ran_1 = __importDefault(require("@utils/ran"));
const app = (0, express_1.default)();
app.get('/', async (req, res) => {
    res.json({ message: 'okay' });
});
console.log((0, ran_1.default)(), ': from module');
app.listen(7000, () => {
    console.log('server running on port 7000');
});
