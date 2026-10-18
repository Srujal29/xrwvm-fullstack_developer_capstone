const express = require('express');
const fs = require('fs');
const cors = require('cors');

const app = express();
const port = 3030;

app.use(cors());
app.use(express.json());

// Raw JSON parse karo
const raw_reviews = JSON.parse(fs.readFileSync('reviews.json', 'utf8'));
const raw_dealerships = JSON.parse(fs.readFileSync('dealerships.json', 'utf8'));

// Object keys handle karne ka safety check
const reviews_data = Array.isArray(raw_reviews) ? raw_reviews : (raw_reviews.reviews || []);
const dealerships_data = Array.isArray(raw_dealerships) ? raw_dealerships : (raw_dealerships.dealerships || []);

// Fetch all dealers
app.get('/fetchDealers', (req, res) => {
    res.json(dealerships_data);
});

// Fetch dealers by state
app.get('/fetchDealers/:state', (req, res) => {
    const state = req.params.state.toLowerCase();
    const filtered = dealerships_data.filter(d => d.state && d.state.toLowerCase() === state);
    res.json(filtered);
});

// Fetch dealer by ID
app.get('/fetchDealer/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const dealer = dealerships_data.find(d => d.id === id);
    res.json(dealer ? [dealer] : []);
});

// Fetch reviews for a dealer
app.get('/fetchReviews/dealer/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const reviews = reviews_data.filter(r => r.dealership === id);
    res.json(reviews);
});

// Post a review
app.post('/insert_review', (req, res) => {
    const newReview = req.body;
    reviews_data.push(newReview);
    res.json({ status: 200, message: "Review added successfully", review: newReview });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});