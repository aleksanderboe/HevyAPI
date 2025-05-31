<template>
  <div class="bg-gray-50 dark:bg-gray-700 p-6 rounded-xl shadow-sm transition-colors duration-300">
    <h3 class="text-2xl font-semibold text-gray-900 dark:text-white mb-6">Exercises</h3>
    <div class="space-y-6">
      <div
        v-for="exercise in exercises"
        :key="exercise.exercise_template_id"
        class="bg-white dark:bg-gray-600 p-6 rounded-lg shadow-sm transition-all duration-300"
      >
        <h4 class="text-xl font-semibold text-gray-800 dark:text-white mb-5">
          {{ exercise.title }}
        </h4>

        <!-- Sets -->
        <div class="space-y-3">
          <div
            v-for="set in exercise.sets"
            :key="set.index"
            class="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-500 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-450 transition-colors duration-200"
          >
            <!-- Left side: Set number and reps -->
            <div class="flex items-center space-x-4">
              <div
                class="w-10 h-10 flex items-center justify-center rounded-full bg-gradient-to-r from-blue-500 to-indigo-500 text-white font-bold text-sm shadow-md"
              >
                {{ set.index + 1 }}
              </div>
              <div class="flex items-baseline space-x-1">
                <span class="text-2xl font-bold text-gray-900 dark:text-white">
                  {{ set.reps }}
                </span>
                <span class="text-sm text-gray-500 dark:text-gray-400 font-medium"> reps </span>
              </div>
            </div>

            <!-- Right side: Weight -->
            <div class="flex items-baseline space-x-1">
              <span
                v-if="set.weight_kg"
                class="text-xl font-semibold text-gray-900 dark:text-white"
              >
                {{ set.weight_kg }}
              </span>
              <span
                v-if="set.weight_kg"
                class="text-sm text-gray-500 dark:text-gray-400 font-medium"
              >
                kg
              </span>
              <span v-else class="text-gray-400 dark:text-gray-500 text-sm italic">
                Body weight
              </span>
            </div>
          </div>
        </div>

        <!-- Exercise Summary -->
        <div
          class="mt-5 pt-4 border-t border-gray-200 dark:border-gray-500 flex justify-between items-center"
        >
          <div class="text-sm text-gray-600 dark:text-gray-400">
            <span class="font-medium">{{ exercise.sets.length }}</span> sets completed
          </div>
          <div
            v-if="getTotalVolume(exercise.sets) > 0"
            class="text-sm text-gray-600 dark:text-gray-400"
          >
            <span class="font-medium">{{ getTotalVolume(exercise.sets) }} kg</span> total volume
          </div>
        </div>
      </div>

      <div v-if="exercises.length === 0" class="text-center py-16">
        <div class="text-gray-400 dark:text-gray-500 mb-4">
          <svg class="w-20 h-20 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="1.5"
              d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
            />
          </svg>
        </div>
        <p class="text-gray-500 dark:text-gray-400 text-lg">
          No exercises recorded for this workout
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  exercises: {
    type: Array,
    required: true,
    default: () => [],
  },
})

// Calculate total volume for an exercise
const getTotalVolume = (sets) => {
  return sets.reduce((total, set) => {
    const weight = set.weight_kg || 0
    const reps = set.reps || 0
    return total + weight * reps
  }, 0)
}
</script>
