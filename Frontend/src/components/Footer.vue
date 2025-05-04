<template>
  <footer class="footer">
    <p>
      Workout data from
      <a href="https://hevy.com" target="_blank" rel="noopener noreferrer">Hevy API</a>
    </p>
  </footer>
</template>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1rem;
  text-align: center;
  background-color: rgba(255, 255, 255, 0.9);
  font-size: 0.875rem;
  color: #666;
}

.footer a {
  color: #2c3e50;
  text-decoration: none;
  font-weight: 500;
}

.footer a:hover {
  text-decoration: underline;
}
</style>
