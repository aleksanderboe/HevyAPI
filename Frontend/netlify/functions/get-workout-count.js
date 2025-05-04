// netlify/functions/get-workouts-count.js
const fetch = require('node-fetch')

exports.handler = async () => {
  try {
    const response = await fetch('https://api.hevy.com/v1/workouts/count', {
      method: 'GET',
      headers: {
        'api-key': process.env.HEVY_API_KEY,
        'Content-Type': 'application/json',
        accept: 'application/json',
      },
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const data = await response.json()
    return {
      statusCode: 200,
      body: JSON.stringify(data),
    }
  } catch (error) {
    console.error('Error fetching workout count:', error)
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Failed to fetch workout count' }),
    }
  }
}
