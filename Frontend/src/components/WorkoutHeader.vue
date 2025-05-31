<template>
  <div class="text-center">
    <h1
      class="text-6xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-indigo-600 dark:from-blue-400 dark:to-indigo-400 tracking-tight"
    >
      Latest Workout
    </h1>
    <p
      v-if="totalWorkouts !== null"
      class="mt-4 text-xl text-gray-600 dark:text-gray-300 font-medium transition-colors duration-300"
    >
      Workout {{ totalWorkouts > 0 ? `#${totalWorkouts}` : '' }} of {{ totalWorkouts }} total
      workouts
    </p>
  </div>
</template>

<script setup>
defineProps({
  totalWorkouts: {
    type: Number,
    default: null,
  },
})
</script>
