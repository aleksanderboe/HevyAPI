import { ref, watchEffect } from 'vue'

// Global reactive state
const isDark = ref(true)
const isInitialized = ref(false)

// Apply theme to DOM immediately
const applyTheme = (dark) => {
  if (typeof document !== 'undefined') {
    const htmlElement = document.documentElement
    if (dark) {
      htmlElement.classList.add('dark')
    } else {
      htmlElement.classList.remove('dark')
    }
  }
}

// Initialize theme on first load
const initializeTheme = () => {
  if (typeof window === 'undefined' || isInitialized.value) return

  const savedTheme = localStorage.getItem('theme')
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches

  let shouldBeDark = false
  if (savedTheme) {
    shouldBeDark = savedTheme === 'dark'
  } else {
    shouldBeDark = prefersDark
  }

  // Set both values together to avoid triggering watchEffect prematurely
  isDark.value = shouldBeDark
  applyTheme(shouldBeDark)
  isInitialized.value = true
}

// Watch for changes and update localStorage and document class (only after initialization)
watchEffect(() => {
  if (!isInitialized.value || typeof window === 'undefined') return

  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
  applyTheme(isDark.value)
})

export const useDarkMode = () => {
  const toggleDarkMode = () => {
    isDark.value = !isDark.value
  }

  return {
    isDark,
    toggleDarkMode,
    initializeTheme,
  }
}
