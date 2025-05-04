// netlify/functions/get-workouts.js
import fetch from 'node-fetch'

export async function handler(event) {
  try {
    const { page = 1, pageSize = 5 } = event.queryStringParameters || {}
    const response = await fetch(
      `https://api.hevy.com/v1/workouts?page=${page}&pageSize=${pageSize}`,
      {
        method: 'GET',
        headers: {
          'api-key': process.env.HEVY_API_KEY,
          'Content-Type': 'application/json',
          accept: 'application/json',
        },
      },
    )

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    const data = await response.json()
    return {
      statusCode: 200,
      body: JSON.stringify(data),
    }
  } catch (error) {
    console.error('Error fetching workouts:', error)
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Failed to fetch workouts' }),
    }
  }
}
