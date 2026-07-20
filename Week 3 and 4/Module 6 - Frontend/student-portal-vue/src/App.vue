<template>

  <Header/>

  <nav>

    <RouterLink to="/courses">

      Courses

    </RouterLink>

    |

    <RouterLink to="/profile">

      Profile

    </RouterLink>

  </nav>

  <br>

  <RouterView/>

</template>

<script setup>

import Header from './components/Header.vue'

import { RouterLink, RouterView } from 'vue-router'

</script>